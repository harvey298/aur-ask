class help:
    search_types: list = ["name","name-desc","maintainer","depends","makedepends","checkdepends"]
    support_searches: list = ["name","maintainer"]
    help_msg: str = """Welcome to aur-ask documentation can be found on the github repo!"""


class search_by:
        name: str = help.search_types[0]
        name_desc: str = help.search_types[1]
        maintainer: str = help.search_types[2]
        depends: str = help.search_types[3]
        makedepends: str = help.search_types[4]
        checkdepends: str =  help.search_types[5]            

class aur_util:
    aur_link: str = "https://aur.archlinux.org"
    header: str = aur_link+"/rpc/?v=5&type=search&by=[Search_Type_Here]&arg="
    header_info: str = aur_link+"/rpc/?v=5&type=info&arg[]="