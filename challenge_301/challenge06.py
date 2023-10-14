#!/usr/bin/env python3

#Renee Stanley
#Bash in Python


import subprocess


who = "whoami"
ip = "ip a"
hardware = (["lshw -short"])

first = subprocess.check_output(who, shell=True, text=True)
#print the result?
print("You are: ")
print(first)
second = subprocess.check_output(ip, shell=True, text=True)
print ("Your ip is: ")
print(second)
third = subprocess.check_output(hardware, shell=True, text=True)
print("Your hardware looks like: ")
print(third)

