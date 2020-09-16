import os,sys,time
from time import sleep
m = '\033[1;31m' # merah
b = '\033[1;36m' # biru
k = '\033[1;33m' # kuning
h = '\033[1;32m' # hijau
u = '\033[1;35m' # ungu
p = '\033[1;37m' # putih
ut = '\033[1;34m' # ungu tua

os.system('clear')
sleep(2)
print(u+"====="+k+"Login SC"+u+"=====\n"+p+"["+h+"1"+p+"]"+b+" Login SC\n"+p+"["+h+"2"+p+"]"+b+" install bahan\n"+p+"["+h+"0"+p+"]"+m+" Exit")
pil = raw_input(k+"pilih => ")
if pil == "1":
	os.chdir("X");os.system('python2 yt.py')

elif pil == "2":
	os.system("pkg install ffmpeg python python2 curl figlet &> /dev/null")
	print(h+"Sucses install "+k+"[ffmpeg,curl,figlet]")
	os.system("pip install youtube-dl  &> /dev/null")
	print(h+"Sucses instal "+k+"pip(youtube-dl)")
	os.system("curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /data/data/com.termux/files/usr/bin/youtube-dl  &> /dev/null")
	print(h+"Sucses install "+k+"curl(youtube-dl)")
	os.system("chmod a+rx /data/data/com.termux/files/usr/bin/youtube-dl ")
	rw = raw_input(b+"Tekan enter untuk lanjut : ")
	if raw == " ":
		os.chdir("X");os.system("python2 yt.py")

	else:
		os.chdir("X");os.system("python2 yt.py")

elif pil == "0":
	sys.exit()
