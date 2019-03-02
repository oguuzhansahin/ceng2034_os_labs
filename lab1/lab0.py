import os
import os.path,time

os.chdir("/home/oguzhan")
os.mkdir("os_lab_0")
os.chdir("/home/oguzhan/os_lab_0")
open("zuerst.txt","w")
open("zweite.txt","w")
open("dritte.py","w")
print("Last modified of zuerst.txt : %s " % time.ctime(os.path.getmtime("zuerst.txt")))
print("Last modified of zweite.txt : %s " % time.ctime(os.path.getmtime("zweite.txt")))
print("Last modified of dritte.py : %s " % time.ctime(os.path.getmtime("dritte.py")))
for file in os.listdir("/home/oguzhan/os_lab_0"):
	if file.endswith(".txt"):
		print(os.path.join("/home/oguzhan",file))
