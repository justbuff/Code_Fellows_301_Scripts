#!/usr/bin/env python3

# Script: Ops 301 Class 11 Ops Challenge Solution
# Author: Justin Buffington
# Date of latest revision: 9/11/2022
# Purpose: Opens and manipulates an existing file

# Main

# Creates txt file and adds 3 lines

file = open("newfile.txt", "w") # write mode
lines = ["This is line 1 \n", "This is line 2 \n", "This is line 3"]
file.writelines(lines)

# Prints line 1

printline = file.readlines(1)
print(printline)

# Deletes file
import os
os.remove("newfile.txt")

# End
