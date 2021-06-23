# Secondary Aur_Handler

# Why have a secondary aur_handler? it keeps everything neat and tidy
# Prevents clutter essentially

# Imports
#from tertiary_aur_handler import invalid_search
from tertiary_aur_handler import does_aur_pkg_have_deps
from colour_lib import info
from util import aur_util,help,search_by
from QuickRequest import req
import threading,sys,time

def is_on_aur(depends):
    offical_pkgs = []
    aur_pkgs = []
    seek = []
    for depn in depends:
        res =req("https://archlinux.org/packages/search/json/?name="+str(depn))
        if res["results"] == []:
            aur_pkgs.append(depn)
            thread_feedback = does_aur_pkg_have_deps(depn,offical_pkgs)#threading.Thread(target=).run() 
            seek.append(thread_feedback)
            #print(depn)
        else:
            offical_pkgs.append(res["results"][0]["pkgname"])
    
    invalids = []
    valids = []
    for is_exists in seek[0]:
        if is_exists["exsits"] == False:
            invalids.append(is_exists["pkgname"])
        else: valids.append(is_exists["pkgname"])

    return_var = {"offical_pkgs":offical_pkgs,"aur_pkgs":{"invailds":invalids,"vailds":valids}}
    return return_var
        

#req("https://archlinux.org/packages/search/json/?name=mcpelauncher-ui-git")

def dep_checks(pkg):
    url = aur_util.header_info+pkg
    info_result = req(url)
    depends = info_result["results"][0]["Depends"]
    makedepends = info_result["results"][0]["MakeDepends"]
    #makedepends = info_result["results"][0]["MakeDepends"]

    pkg_info = is_on_aur(depends)
    #for invalids in pkg_info['aur_pkgs']["invailds"]:
        #print(invalids)
    #    invalid_search(invalids)
    #print(depends)
    return pkg_info

    #print("dep check")

#dep_checks("mcpelauncher-ui-git")
#dep_checks("mcpelauncher-client")