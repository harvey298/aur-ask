# its the 3rd and finail aur handler!
# Don't worry lol

from colour_lib import info,error
from util import aur_util,help,search_by
from QuickRequest import req
import threading,sys,time

def does_aur_pkg_have_deps(aur_pkgs,offical_pkgs):
    url = aur_util.header_info#+aur_pkgs
    feedback = []
    depn = aur_pkgs
    res =(req(url+str(depn)))
    if res["resultcount"] == 0:
        feedback.append({"pkgname":depn,"exsits":False})
    #depends = res["results"][0]["Depends"]
        #print(depends)
    return feedback

def invalid_search(pkg):
    url = aur_util.header + str(pkg)
    url = url.replace("[Search_Type_Here]",search_by.name,1)
    #print(url)

    results = req(url)

    if results["type"] == "error":
        error(results["error"],0)
        error("Given Url: "+url,0)
        return False
    print(pkg)
    
    print(results)

def pkg_info(pkg,provides=True,conflicts=True,raw=False,debug=False):
    url = aur_util.header_info+str(pkg)
    results = req(url)

    if results["type"] == "error":
        error(results["error"],0)
        error("Given Url: "+url,0)
        return False

    if results["resultcount"] == 0:
        if debug == True:
            return results
        else:
            return False

    if provides == True:
        if conflicts == True:
            feedback = {"pkg_name":results["results"][0]["Name"],"provides":results["results"][0]["Provides"],"conflicts":results["results"][0]["Conflicts"]}
            #print(feedback)
        elif conflicts == False:
            feedback = {"pkg_name":results["results"][0]["Name"],"provides":results["results"][0]["Provides"],"conflicts":[]}

    if conflicts == True:
        if provides == True:
            feedback = {"pkg_name":results["results"][0]["Name"],"provides":results["results"][0]["Provides"],"conflicts":results["results"][0]["Conflicts"]}
        elif provides == False:
            feedback = {"pkg_name":results["results"][0]["Name"],"provides":[],"conflicts":results["results"][0]["Conflicts"]}

    if conflicts == False:
        if provides == False:
            return results

    if raw == True:
        return results

    return feedback
