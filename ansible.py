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
	print("ANSIBLE Automation")
	system("tput cup 7 0;tput sgr0")
	
def main():
	banner()

	print("""
	1.  Setup K8s Cluster on AWS
	2.  Configure Hadoop Cluster on AWS
	

	99. Back... """)

	system("tput bold;tput cup 50 0")
	r=sr.Recognizer()

	with sr.Microphone() as source:
		print("Speak Your choice")
		audio=r.listen(source)
		print("Input Recieved...Please Wait")
	ch= r.recognize_google(audio)
	a = int(ch)
	system("tput sgr0")

	banner()
	if a == 1:
		system("ansible-playbook cluster.yml")


	elif a == 2:
		system("ansible-playbook task11master.yml")
		system("ansible-playbook task11slave.yml")
	elif a == 99:
		return
	else:
		print("Wrong Choice...")
	system("tput bold; tput cup 50 0")
	input("Enter Enter key to exit.. ")

