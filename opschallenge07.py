#!/usr/bin/env python3

# Script: Ops 301 Class 07 Ops Challenge Solution
# Author: Justin Buffington
# Date of latest revision: 9/7/2022
# Purpose: Generates all directories, sub-directories and files for a user-provided directory path

# Import libraries

import os

# Read user input here into a variable

directoryvar = input("Please enter directory path: ")

# Declare a function here

def directoryfunc():
    for (root, dirs, files) in os.walk(directoryvar):
    ### Add a print command here to print ==root==
    print(root)
    ### Add a print command here to print ==dirs==
    print(dirs)
    ### Add a print command here to print ==files==
    print(files)

# Main

# Pass the variable into the function here
directoryfunc()

# End
