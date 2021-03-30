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
	print("AWS Automation")
	system("tput cup 7 0;tput sgr0")
	
def main():
	banner()

	print("""
	1.  Create Key-pair
	2.  Create Security Group
	3.  Launch instance
	4.  Create EBS volume
	5.  Attach EBS volume to running Instance
	6.  Create S3 bucket
	7.  Delete all running instances

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
		key = input("Enter your Key Name: ")
		system("aws ec2 create-key-pair --key-name {}".format(key))
	elif a == 2:
		sec = input("Enter your Security Group Name:     ")
		system("aws ec2 create-security-group --description 'ALL traffic allowed' --group-name {}".format(sec))
	elif a == 3:
		ins = input("Enter your Instance type:     ")
		count = input("Number of instances:   ")
		keyn = input("Enter your key Name:  ")
		secgig = input("Enter your security group id:  ")
		imgid =  input("Enter your image-id:  ")
		system("aws ec2 run-instances --security-group-ids {} {} --count {} --image-id {} --key-name {}".format(secgig,imgid,ins,count,keyn))
	elif a == 99:
		return
	else:
		print("Wrong Choice...")
	system("tput bold; tput cup 50 0")
	input("Enter Enter key to exit.. ")


# main()

