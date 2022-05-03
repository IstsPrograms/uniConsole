import json

import os



def run():
    arp = []
    
    regs = json.load(open("disk.pufs", "r"))["reg"]
    for i in range(len(regs)):
        if regs[i]["0"] == "autoruns":
            arps = regs[i]["1"].replace("_", " ").split()
            
            for u in range(len(arps)):
                fl = list
                fl = arps[u].replace("/", " ").split()
                arp.append(fl)
                
    for i in range(len(arp)):
        for u in range(len(json.load(open("disk.pufs", "r"))[arp[i][0]])):  
            if json.load(open("disk.pufs", "r"))[arp[i][0]][u]["0"] == arp[i][1]:
                exec(json.load(open('disk.pufs', 'r'))[arp[i][0]][u]['1'])
                
                
       