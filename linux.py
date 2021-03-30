from os import system
import speech_recognition as sr
import cgi
import pyaudio
import subprocess as sp
from os import system

def banner():
	system("clear;tput setaf 1; tput cup 3 15;tput bold;tput rev")
	print("Python Automation")
	system("tput sgr0;tput bold;tput cup 5 15 ; ")
	print("Linux Automation")
	system("tput cup 7 0;tput sgr0")


def main():
	banner()
	
	print('''
	1. Local system
	2. Remote system

	99. Back...''')
	system("tput bold;tput cup 50 0")
	print("Enter your choice [1-2]\t : ",end='')
	r=sr.Recognizer()

	with sr.Microphone() as source:
		print("Speak Your choice")
		audio=r.listen(source)
		print("Input Recieved...Please Wait")
	ch= r.recognize_google(audio)
	sys = int(ch)
	if sys == 99:
		return 

	system("tput sgr0")

	banner()
	print('''
	1.  Get Network Interface Info
	2.  Ping
	3.  Start / Stop Firewall
	4.  Check Process
	5.  Shutdown / Reboot
	6.  Get Calender
	7.  Get Date
	8.  Get Calculator

	99.  Back.. ''')

	system("tput bold; tput cup 50 0")
	rw=sr.Recognizer()
	with sr.Microphone() as source:
		print("Speak Your choice")
		audiow=rw.listen(source)
		print("Input Recieved...Please Wait")
	chw= rw.recognize_google(audiow)
	choice= int(chw)
	system("tput sgr0")

	banner()

	command = ""

	if choice == 99:
		return
	elif choice == 1:
		command = "ifconfig"
	elif choice == 2:
		rww=sr.Recognizer()
		with sr.Microphone() as source:
			print("Speak IP to ping")
			audiow=rww.listen(source)
			print("Input Recieved...Please Wait")
			temp= rww.recognize_google(audiow)
		command = "ping " + temp
		
	elif choice == 3:
		rww=sr.Recognizer()
		with sr.Microphone() as source:
			print("Speak Start or Stop")
			audiow=rww.listen(source)
			print("Input Recieved...Please Wait")
		temp= rww.recognize_google(audiow)
		if "stop" in temp:
			command = "systemctl stop firewalld"
		else:
			command = "systemctl start firewalld"
	elif choice == 4:
			command = "ps -a -u -x"
	elif choice == 5:
		rww=sr.Recognizer()
		with sr.Microphone() as source:
			print("Speak Start or Stop")
			audiow=rww.listen(source)
			print("Input Recieved...Please Wait")
		temp= rww.recognize_google(audiow)
		if "shutdown" in temp:
			command = "shutdown now"
		else:
			command = "reboot"
	elif choice == 6:
			choicecommand = "cal"
	elif choice == 7:
			command = "date"
	elif choice == 8:
			command = "bc"

	if sys == 1:
			system(command)
	else :
			ip = ""
			username = ""
			pas = ""
			rww=sr.Recognizer()
			with sr.Microphone() as source:
					print("Speak IP")
					audiow=rww.listen(source)
					print("Input Recieved...Please Wait")
			ip= rww.recognize_google(audiow)
			with sr.Microphone() as source:
					print("Speak Username")
					audiow=rww.listen(source)
					print("Input Recieved...Please Wait")
			username= rww.recognize_google(audiow)
			with sr.Microphone() as source:
					print("\tSpeak 1 to use Password\n\tSpeak 2 to use key\nEnter Your choice\t\t :")
					audiow=rww.listen(source)
					print("Input Recieved...Please Wait")
			temp= rww.recognize_google(audiow)
			
			if temp == "1":
				system("ssh " + username+"@"+ip+" "+command)

			elif temp == "2":
				rww=sr.Recognizer()
				with sr.Microphone() as source:
					print("Speak Location of key")
					audiow=rww.listen(source)
					print("Input Recieved...Please Wait")
				pas = rww.recognize_google(audiow)
				banner()
				system("ssh " + username+"@"+ip+" -i "+pas+" " +command)

	system("tput bold; tput cup 50 0")
	input("Enter Enter key to exit..")

	# main()

