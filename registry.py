import uExplorer
import json
import colorama
from colorama import Fore, init
colorama.init()
def run():
    dsk = json.load(open("disk.pufs", "r"))
    print(f"{Fore.BLUE} commands: \n config create (config name) (value) - create config \n config save - save configuration \n config delete (config name) - delete configuration \n config reset - resets config{Fore.RESET}")
    while True:
       
        _in = input(">>> ")
        _in = _in.split()
        if _in[0] == "config":
            if _in[1] == "create":
                uExplorer.Disk("CONFCREATE", dsk, {"param": _in[2], "desc": _in[3]})
                print(f"Succesfully created configuration {_in[2]}")
                
            elif _in[1] == "save":
                
                uExplorer.Disk("DSAVE", dsk, {})
                print("Config succefully saved!")
            elif _in[1] == "delete":
                for i in range(len(dsk["reg"])):
                    if dsk["reg"][i]["0"] == _in[2]:
                        dsk["reg"].remove(dsk["reg"][i])
                        print(f"Succesfully removed configuration {_in[2]}")
            elif _in[1] == "reset":
                dsk["reg"] = []
                print("Registry reset succefully!")
                    

    

