#!/usr/bin/env python3

#Renee Stanley
#Challenge08, lists

space_stuff = ["The Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus","Neptune", "Pluto" ]

#print initial list
print ("My list has 10 space thingies")
print ([space_stuff])
print()


#print the fourth item in list
print ("The fourth value in list is: " )
print(space_stuff[3])
print()

#print values 6-10 in the list
print ("The sixth through tenth values in list are: ")
print(space_stuff[6:])
print()

#changing the value of seventh item 
space_stuff[6] = "onion"
print ("I changed the seventh value in the list. Now it looks like: ")
print (space_stuff)
print()
