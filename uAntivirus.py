import json
import uExplorer


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
            


    
    print(f"Removed {removd} threats, repaired {repaired} files")
def run():
    print("Help: \n check (partition name) - check partition")
    a = input("Antivirus > ")
    sa = a.split()
    if sa[0] == "check":
        Check(sa[1])

