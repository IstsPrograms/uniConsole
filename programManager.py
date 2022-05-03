

import json

def run():
    dsk = json.load(open("disk.pufs", "r"))
    print("Hello, user!")
    print(" Help: \n program import (file name) (partition name) - import program to your virtual disk \n program run (Partition name)/(file name) - run program from your virtual disk")
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
                        
