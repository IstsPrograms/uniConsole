import json
import colorama
from colorama import Fore, init
colorama.init()
def Disk(operation: str, disk: dict, args: dict):
    if operation == "FFIND":
        fn = args["file"]
        dr = args["razdel"]

        for i in range(len(disk[dr])):
            if disk[dr][i]["0"] == fn and "FILE" in disk[dr][i]["2"]:
                return disk[dr][i]["1"]
    elif operation == "FCREATE":
        breaked = False
        for i in range(len(disk[args["razdel"]])):
            if args["file"] == disk[args["razdel"]][i]["0"]:
                disk[args["razdel"]][i]["1"] = args["desc"]
                breaked = True
                break
        if breaked == False:
            new_file = {"0": args["file"], "1": args["desc"], "2": "FILE"}
            disk[args["razdel"]].append(new_file)
    elif operation == "CONFCREATE":
        breaked = False
        for i in range(len(disk["reg"])):
            if args["param"] == disk["reg"][i]["0"]:
                disk["reg"][i]["1"] = args["desc"]
                breaked = True
                break
        if breaked == False:
            new_file = {"0": args["param"], "1": args["desc"], "2": "CONF"}
            disk["reg"].append(new_file)
            
       
    elif operation == "RCREATE":
        disk[args["razdel"]] = []
    elif operation == "DSAVE":
        dsk = open("disk.pufs", "w")
        json.dump(disk, dsk)
        dsk.close()
    elif operation == "FREMOVE":
        for i in range(len(disk[args["razdel"]])-1):
            if disk[args["razdel"]][i]["0"] == args["file"]:
                disk[args["razdel"]].remove(disk[args["razdel"]][i])
    elif operation == "DRESET":
        disk = {"C": [], "reg": []}
    
def run():
    print("Help: \n file read (Partition name)/(file name) - read file \n file create (partition name)/(file) (content) - create file")
    print(" file remove (Partition name)/(file name) - remove file \n partition create (partition name) - create partition \n disk save - save disk")
    js = json.load(open("disk.pufs", "r"))
    print("Hello, user!")
    while True:
        action = input(">> ")

        sa = action.split()
        if sa[0] == "file":
            if sa[1] == "read":
                sa = sa[2].replace("/", " ")
                sa = sa.split()
                print(Disk("FFIND", js, {"file": sa[1], "razdel": sa[0]}))
            elif sa[1] == "create":
                ss = sa[2].replace("/", " ")
                ss = ss.split()
                Disk("FCREATE", js, {"file": ss[1], "razdel": ss[0], "desc": sa[3]})
                print(f"File {ss[1]} succesfully created! ")
            elif sa[1] == "remove":
                sa = sa[2].replace("/", " ")
                sa = sa.split()
                Disk("FREMOVE", js, {"file": sa[1], "razdel": sa[0]})
                print(f"File {sa[1]} succesfully removed! ")
        elif sa[0] == "partition":
            if sa[1] == "create":
                Disk("RCREATE", js, {"razdel": sa[2]})
                print("Partition created!")

        elif sa[0] == "disk":
            if sa[1] == "save":
                Disk("DSAVE", js, {})
                print("Disk succefully saved! ")
            
