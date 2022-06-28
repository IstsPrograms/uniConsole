
import asyncio
import socket
import json
import uExplorer
import random
import threading



args = {}
args_client = {}
def server():
    
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((args["ip"], int(args["port"])))
    srv.listen()
    print("Server started!")
    while True:
            
        user, adres = srv.accept()
        print(f"User was connected")
        print(f"Variable 'adres': {adres}")
        print(f"Variable 'user': {user}")
        print(f"Sending package...")
        user.send(args["pkg"].encode("utf-8"))
        print(f"User was received package! ({adres})")
    
    
def client():
    
    clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clnt.connect((args_client["ip"], int(args_client["port"])))
    print("Connected!")
    while True:
        print("Downloading package... ")

        data = clnt.recv(1024)
        dsk = json.load(open("disk.pufs", "r"))
        pkg_name = f"pkg{random.randint(1, 1000000)}"
        uExplorer.Disk("FCREATE", dsk, {"file": pkg_name, "razdel": "C", "desc": data.decode("utf-8")})
        json.dump(dsk, open("disk.pufs", "w"))
        print(f"Succesfully downloaded as {pkg_name}!")
        break
    











def run():
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
