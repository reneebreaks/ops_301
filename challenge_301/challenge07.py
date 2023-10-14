#!/usr/bin/env python3

# Script Name:              Ops Challenge 07
# Author:                   Renee Stanley
# Date of last revision:    Wicked Late
# Description of purpose:   Functions in Python, os.walk

import os

testdir = input("Please provide a filepath of a directory, thank you. ")


def my_function(x):
    for (root, dirs, files) in os.walk(testdir):
        print(root)
        print(dirs)
        print(files)



my_function("testdir")