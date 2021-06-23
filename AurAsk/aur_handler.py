# Primary aur_handler
from secondary_aur_handler import dep_checks
from util import help,search_by,aur_util
from colour_lib import caution, error,info
from QuickRequest import req
import threading

#class help:
#    search_types: list = ["name","name-desc","maintainer","depends","makedepends","checkdepends"]
#    support_searches: list = ["name","maintainer"]


#class search_by:
#        name: str = help.search_types[0]
#        name_desc: str = help.search_types[1]
#        maintainer: str = help.search_types[2]
#        depends: str = help.search_types[3]
#        makedepends: str = help.search_types[4]
#        checkdepends: str =  help.search_types[5]            

#class aur_util:
#    aur_link: str = "https://aur.archlinux.org"
#    header: str = aur_link+"/rpc/?v=5&type=search&by=[Search_Type_Here]&arg="
#    header_info: str = aur_link+"/rpc/?v=5&type=info&arg[]="

def maintainer_search(keyword,search_type,results):
    feedback = []
    feedback.append({"maintainer":keyword})
    pkgs = []
    for pkg in range(results["resultcount"]):
        name = results["results"][pkg]["Name"]
        #if results["results"][pkg]["OutOfDate"] == "None":
        #    is_out_of_date = False                              # Commented out because a maintainer search won't need a out of date search? right?
        #else: is_out_of_date = True
        
        pkgs.append(name)

    feedback.append({"pkgs":pkgs})
    return feedback

def pkg_name_search(keyword,search_type,results):
    #feedback = []
    pkgs = []
    for pkg in range(results["resultcount"]):
        name = results["results"][pkg]["Name"]
        if results["results"][pkg]["OutOfDate"] != "None":
            is_out_of_date = False
        else: is_out_of_date = True
        pkg_info = {"pkg_name":name,"OutOfDate":is_out_of_date}
        pkgs.append(pkg_info)
        
        #print(results["results"][pkg]["OutOfDate"]) Small Bug here

    feedback = {"Search_Data":{"keyword":keyword,"search_by":search_type},"pkg_data":pkgs}
    return feedback

def dep_checky(pkg,results): # Dep checking function for multi-threading purposes!
    print("dep check")
    #print(results)
    #print(str(req("https://archlinux.org/packages/search/json/?name=mcpelauncher-ui-git")["results"]))
    url = aur_util.aur_link + aur_util.header_info+pkg
    info = req(url)
    print(str(info))

def ask_aur(keyword: str,search_type = search_by.name,dep_check = False,custom_url = False,silence = False,debug = False):
    if custom_url == False:
        url = aur_util.header + keyword
        url = url.replace("[Search_Type_Here]",search_type,1)
    else: url = custom_url + keyword
    #print(url)
    results = req(url)

    if results["type"] == "error":
        error(results["error"],0)
        error("Given Url: "+url,0)
        return False

    if results["resultcount"] == 0:
        if silence == True:
            info("No Vaild Results, Returning False")
        elif debug == True:
            return results
        else:
            return False # Returning false means no useable results

    if debug == True:
        print(results)

    # --------- REMOVE THIS CODE ONCE FULLY COMPLETED! ----------# 
    supported_search = False
    for s_types in range(5):
        if s_types >= 2:
            pass
        else:
            if search_type == help.support_searches[s_types]:
                supported_search = True

    if supported_search == False:
        caution("The Search type "+str(search_type)+". Isn't fully supported and will output raw data!")
        return results
    # --------- END TO BE REMOVED CODE --------------------------#
    
    
    
    #print(results["results"]) # Here for debugging!!
    feedback = []
    if search_type == search_by.name:
        feedback.append(pkg_name_search(keyword,search_type,results))
    
    elif search_type == search_by.maintainer:
        feedback.append(maintainer_search(keyword,search_type,results))

    else: feedback.append(results)

    #print("uwuf")

    if dep_check == True:
        if results["resultcount"] == 1:
            if supported_search == False:
                error("Not Supported search!!",0)
            else:
                return_var = []
                return_var.append({"searchData":feedback[0]["Search_Data"],"pkgData":{"pkgName":feedback[0]["pkg_data"][0]["pkg_name"],"depends":dep_checks(keyword)}})
                return return_var
        else:
            error("Dep checking only works if One package is asked of")
            
        


    return feedback
    
    
#print(str(req("https://archlinux.org/packages/search/json/?name=mcpelauncher-ui-git")["results"]))
#print(str(ask_aur("mcpelauncher-ui-git",search_type = search_by.name,debug = False, silence = False,dep_check=True))) # More debugging!! All comments used for debugging will removed once this section I feel is completed!

# 