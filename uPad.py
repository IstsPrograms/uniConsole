import colorama
from colorama import init, Back, Fore
import os
import uExplorer
import json
colorama.init()
r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE 
s = Fore.RESET
w = Fore.WHITE
print(f"{g}Hello, user!{r}")
print(f"{g} -RESET for reset text \n -SAVE for save text \n -EDIT for edit line \n -OPEN for open file \n -QUIT for exit{s}")
text = []
_lnum = 0
dsk = json.load(open("disk.pufs", "r"))
while True:
	_line = input(f"{_lnum} ")
	_lnum += 1
	if "-SAVE" in _line:
		_fp = input(f"{w} {s} File name and path...   ")
		_fp = _fp.replace("/", " ")
		_fp = _fp.split()
		_t = ""
		for i in range(len(text)):

			_t += text[i]
			_t += "\n"
		
		uExplorer.Disk("FCREATE", dsk, {"file": _fp[1], "razdel": _fp[0], "desc": _t})
		json.dump(dsk, open("disk.pufs", "w"))
		print("  Succesfly saved!")
		os.system("cls")
	elif "-RESET" in _line:
		text = ""
		os.system("cls")
	elif "-OPEN" in _line:
		_fl1 = input("Path to file... ")
		_fl1 = _fl1.replace("/", " ")
		_fl1 = _fl1.split()

		_fl = uExplorer.Disk("FFIND", dsk, {"file": _fl1[1], "razdel": _fl1[0]})
		text = _fl.splitlines()
		__t = ""
		os.system("cls")
		for i in range(len(text)):
			__t += f"{i} "
			__t += text[i]
			__t += "\n"
		print(__t)
	elif "-EDIT" in _line:
		_l = int(input("  Line...   "))
		text[_l] = input(f"{_l} ")
		os.system("cls")
		__t = ""
		for i in range(len(text)):
			__t += f"{i} "
			__t += text[i]
			__t += "\n"
		print(__t)
		_lnum -= 1
	elif "-QUIT" in _line:
		print(f"{g}Bye!{s}")
		quit(0)
	else:
		text.append(_line)