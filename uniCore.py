import json
import colorama
from colorama import Fore, init

import socket


import random
import threading
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
def runUEXP():
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
def Check(razdel: str):
    removd = 0
    repaired = 0
    
    for i in range(len(json.load(open("disk.pufs", "r"))["reg"])):
        try:
            if json.load(open("disk.pufs", "r"))["reg"][i]["2"] != "CONF":
            
                dsk = json.load(open("disk.pufs", "r"))
                dsk["reg"].remove(dsk["reg"][i])
                json.dump(dsk, open("disk.pufs", "w"))
                removd += 1
        except:
            pass
    for i in range(len(json.load(open("disk.pufs", "r"))[razdel])):
        if json.load(open("disk.pufs", "r"))[razdel][i]["2"] != "FILE" or json.load(open("disk.pufs", "r"))[razdel][i]["2"] != "CONF" or json.load(open("disk.pufs", "r"))[razdel][i]["2"] != "PROGRAM":
            dsk = json.load(open("disk.pufs", "r"))
            
            print(f"Finded {dsk[razdel][i]['0']} with extension '{dsk[razdel][i]['2']}'")
            a = input("Repair file? [N/Y] ")
            if a == "Y":
                dsk[razdel][i]["2"] = "FILE"
                json.dump(dsk, open("disk.pufs", "w"))
                repaired += 1
            else:
                pass
def runANTIVIRUS():
    print("Help: \n check (partition name) - check partition")
    a = input("Antivirus > ")
    sa = a.split()
    if sa[0] == "check":
        Check(sa[1])
def runREGEDIT():
    dsk = json.load(open("disk.pufs", "r"))
    print(f"{Fore.BLUE} commands: \n config create (config name) (value) - create config \n config save - save configuration \n config delete (config name) - delete configuration {Fore.RESET}")
    while True:
       
        _in = input(">>> ")
        _in = _in.split()
        if _in[0] == "config":
            if _in[1] == "create":
                Disk("CONFCREATE", dsk, {"param": _in[2], "desc": _in[3]})
                print(f"Succesfully created configuration {_in[2]}")
                
            elif _in[1] == "save":
                
                Disk("DSAVE", dsk, {})
                print("Config succefully saved!")
            elif _in[1] == "delete":
                for i in range(len(dsk["reg"])):
                    if dsk["reg"][i]["0"] == _in[2]:
                        dsk["reg"].remove(dsk["reg"][i])
                        print(f"Succesfully removed configuration {_in[2]}")
args = {}
args_client = {}
def server():
    try:
        srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv.bind((args["ip"], int(args["port"])))
        srv.listen()
        print("Server started!")
        while True:
            
            user, adres = srv.accept()
            print(f"User was connected ({adres})")
            print(f"Sending package...")
            user.send(args["pkg"].encode("utf-8"))
            print(f"User was received package! ({adres})")
    except:
        print("Error")
def client():
    try:
        clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clnt.connect((args_client["ip"], int(args_client["port"])))
        print("Connected!")
        while True:
            print("Downloading package... ")

            data = clnt.recv(1024)
            dsk = json.load(open("disk.pufs", "r"))
            pkg_name = f"pkg{random.randint(1, 1000000)}"
            Disk("FCREATE", dsk, {"file": pkg_name, "razdel": "C", "desc": data.decode("utf-8")})
            json.dump(dsk, open("disk.pufs", "w"))
            print(f"Succesfully downloaded as {pkg_name}!")
            break
    except:
        print("Error")











def runPKG():
    global args
    dsk = json.load(open("disk.pufs", "r"))
    print("Hello, user!")
    print(" Help: \n program import (file name) (partition name) - import program to your virtual disk \n program run (Partition name)/(file name) - run program from your virtual disk")
    print(" package send (host ip) (host port) (partition of package) (name of package) - send package \n package recv (server ip) (server port) - receive package")
    while True:
        ac = input("-> ")
        ac = ac.split()
        if ac[0] == "program":
            if ac[1] == "import":
                fi = open(ac[2] + ".py", "r").read()
                new_program = {"0": ac[2], "1": fi, "2": "PROGRAM"}
                dsk[ac[3]].append(new_program)
                json.dump(dsk, open("disk.pufs", "w"))
                print(f"Program {ac[2]} succesfully imported to disk!")
            elif ac[1] == "run":
                ac = ac[2].replace("/", " ")
                ac = ac.split()
                for i in range(len(dsk[ac[0]])):
                   
                    if dsk[ac[0]][i]["0"] == ac[1]:
                        exec(dsk[ac[0]][i]["1"])
        if ac[0] == "package":
            if ac[1] == "send":
                args["ip"] = ac[2]
                args["port"] = ac[3]
                for i in range(len(dsk[ac[4]])):
                    if dsk[ac[4]][i]["0"] == ac[5]:
                        args["pkg"] = dsk[ac[4]][i]["1"]
                
                th = threading.Thread(target=server)
                th.run()
            if ac[1] == "recv":
                args_client["ip"] = ac[2]
                args_client["port"] = ac[3]
                th = threading.Thread(target=client)
                th.run()
