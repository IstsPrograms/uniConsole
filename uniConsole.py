

import json
import colorama
from colorama import init, Fore
import os
colorama.init()
dsk = json.load(open("disk.pufs", "r"))
safe_mode = 0
try:
	for i in range(len(dsk["reg"])):
		if dsk["reg"][i]["0"] == "safe_mode":
			safe_mode = int(dsk["reg"][i]["1"])
		else:
			print(f"Configuration {dsk['reg'][i]['0']} advertised but not used")
			_in = input("Delete? [Y/N] ")
			if _in == "Y":
				dsk["reg"].remove(dsk["reg"][i])
				json.dump(dsk, open("disk.pufs", "w"))
			elif _in == "N":
				pass




except:
	pass
if not (safe_mode != 0):
	import uExplorer
	import registry
	import packageManager
	import uAntivirus
	import uniOnlineCenter
else:
	print("You entered in safe mode")
print("core help for help")
while True:
	_a = input("> ")
	_sa = _a.split()

	try:
		if _sa[0] == "core":
			if _sa[1] == "echo":
				_echotext = ""
				for i in range(2, len(_sa)):
					_echotext += _sa[i]
					_echotext += " "
				print(_echotext)
			
			elif _sa[1] == "help":
				print("Help: \n core echo (any text) \n system (any command) \nApps: \n regedit \n pkg \n antivirus\n uexplorer")


		elif _sa[0] == "system":
			_command = ""
			for i in range(1, len(_sa)):
				_command += _sa[i]
				_command += " "
			
			os.system(_command)
		if not (safe_mode != 0):
			if _sa[0] == "uexplorer":
				uExplorer.run()
			elif _sa[0] == "regedit":
				registry.run()
			elif _sa[0] == "pkg":
				packageManager.run()
			elif _sa[0] == "antivirus":
				uAntivirus.run()
			elif _sa[0] == "uoc":
				uniOnlineCenter.run()

	except:
		print("Error")
	
					   
	