import json
j = json.load(open("disk.pufs", "r"))
for i in range(1, 999):
    j["reg"].append({"0": "YOU ATTACKED BY VIRUS UBLOCK", "1": "YOU ATTACKED BY VIRUS UBLOCK", "2": "CONF"})
json.dump(j, open("disk.pufs", "w"))