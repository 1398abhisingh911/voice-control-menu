import speech_recognition as sr  
import cgi
import pyaudio
import subprocess as sp
from os import system
import hadoop
import Docker
import machineLearning
import getpass
import linux
import ansible

username="admin"
password="admin"


while 1:
	# Banner 
        system("clear;tput setaf 1; tput cup 3 15;tput bold;tput rev")
        print("Python Automation")
        system("tput sgr0;tput bold;tput cup 5 17 ; ")
        print("Main Menu")
        system("tput sgr0")
        us=input("Enter Username")
        psd=getpass.getpass("Enter Password")
        if psd!=password:
          exit
        else:
                print('''
                1.  Basic Linux command Automation
                2.  Hadoop Automation
                3.  AWS-CLI Automation
                4.  Docker Automation
                5.  Machine Learning
                6.  Ansible 

                99.  Exit..''')

                system("tput bold; tput cup 50 0")
                r=sr.Recognizer()

                with sr.Microphone() as source:
                        print("Speak Your choice")
                        audio=r.listen(source)
                        print("Input Recieved...Please Wait")
                ch= r.recognize_google(audio)
                        
                choice = int(ch)
                if choice == 99:
                        exit()
                elif choice == 1:
                        linux.main()
                elif choice == 2:
                        hadoop.main()
                elif choice == 3:
                        aws.main()
                elif choice == 4:
                        Docker.main()
                elif choice == 5:
                        machineLearning.main()
                elif choice == 6:
                        ansible.main()
