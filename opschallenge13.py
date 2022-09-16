#!/usr/bin/env python3

# Script: Ops 301 Class 13 Ops Challenge Solution
# Author: Justin Buffington
# Date of latest revision: 9/15/2022
# Purpose: Print user defined HTTP request

import requests
import inquirer

# Ask user to input a web address

destinationvar = input('Please enter URL')

# Ask user to select method from list

httpquestions = [
  inquirer.List('size',
                message="Which HTTP method do you want?",
                choices=['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS'],
               ),
]
httpanswers = inquirer.prompt(questions)

# Prints url and method choice

print(httpanswers["size"], destinationvar)

# Runs specific requests based off selection

if httpanswers == 'GET':
  method = requests.get
elif httpanswers == 'POST':
  method = requests.post
elif httpanswers == 'PUT':
  method = requests.put
elif httpanswers == 'DELETE':
  method = requests.delete
elif httpanswers == 'HEAD':
  method = requests.head
elif httpanswers == 'PATCH':
  method = requests.patch
elif httpanswers == 'OPTIONS':
  method = requests.options
else print('Please re-run script')
  return None

requestvar = method(destinationvar)

if requestvar.status_code == 200:
  print('Success!')
elif requestvar.status_code == 404:
  print('Not Found')
  
print('\nHeader Info\n')
print(requests.headers)
      
run_command()
