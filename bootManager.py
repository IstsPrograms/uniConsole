import json
boot_devs = []
dsk = json.load(open("disk.pufs", "r"))
try:
	for i in range(len(dsk["reg"])):
		if dsk["reg"][i]["0"] == "boot_devices":
			boot_devs = dsk["reg"][i]["1"]
			boot_devs = boot_devs.replace(",", " ")
			boot_devs = boot_devs.split()
			break
except:
	pass

for i in range(len(boot_devs)):
	print(f"[{i}] {boot_devs[i]}")
print(f"[{len(boot_devs)}] UniConsole")
action = int(input("Select boot device...   "))
if action != len(boot_devs):
	exec(dsk[boot_devs[action]][0]["1"])
else:
	exec(open("uniConsole.py", "r").read())