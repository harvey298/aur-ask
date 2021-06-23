# aur-ask Documentation

### Basic useage
to get basic information about a package or pkg from the aur use
"""
ask_aur("mcpelauncher-ui-git")
"""

if you want more control over what you get back you can do
"""
ask_aur("mcpelauncher-ui-git",search_type = search_by.name,dep_check=True)
"""
How does that work you may ask well heres how:
    Argument 1: Pkg name/keyword
    Argument 2: What to search by all types can be found [here](https://aur.archlinux.org/rpc.php), it can be any text or the class
    Argument 3: Dep_check checks what the pkg depends on, it gets pkgs from the offical repos too! as of currently all [aur](https://aur.archlinux.org/) come up in the invaild scope
