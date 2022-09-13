#!/usr/bin/env python3

# Script: Ops 301 Class 10 Ops Challenge Solution
# Author: Justin Buffington
# Date of latest revision: 9/10/2022
# Purpose: Prints logical conditionals

# Assign variables
a = 5
b = 7

# Main

if a == b:
  print("a equals b")
if a != b:
  print("a does not equal b")
if a < b:
  print("a is less than b")
if a <= b:
  print("a is less than or equal to b")
if a > b:
  print("a is greater than b")
if a >= b:
  print("a is greater than or equal to b")

if a == b:
  print("a equals b")
elif a != b:
  print("a does not equal b")

if a > b:
  print("a is greater than b")
elif a < b:
  print("a is less than b")
else: 
  print("a equals b")
  
  # End
