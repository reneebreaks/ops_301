#!/usr/bin/env python3

#Renee Stanley
#File Handling in Python

import os



#create a new empty text file
with open("my_document.txt", "w") as document:
  pass

#my_document = "my_document.txt"

#add three lines to the document
with open("my_document", "w") as document:
    document.write("There is an important idea that we must consider.\n")
    document.write("The first thing is that you must use your powers for good and not evil.\n")
    document.write("For we now wield power that is unparalleled, and we use it resolutely and with virtuous intent.\n")

#read contents of newly appended file
ramblings = open("my_document", "r")
ramblings = ramblings.read()
print(ramblings)    

#read and print each line of the document
with open("my_document", "r") as document:   
    firstline = document.readline().strip('\n')
    print("The First Line:", firstline)

#now we will delete our precious transcript

os.remove("/home/reneebreaks/ops_301/challenge_301/my_document.txt")
os.remove("/home/reneebreaks/ops_301/challenge_301/my_document")
