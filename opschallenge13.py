#!/usr/bin/env python3

# Script: Ops 301 Class 13 Ops Challenge Solution
# Author: Justin Buffington
# Date of latest revision: 9/15/2022
# Purpose: Print user defined HTTP request

import requests
import inquirer

# Ask user to input a web address

destinationvar = input('Please enter URL')

httpquestions = [
  inquirer.List('size',
                message="Which HTTP method do you want?",
                choices=['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS'],
               ),
]
httpanswers = inquirer.prompt(questions)

print(httpanswers["size"], destinationvar)

requestvar = requests.get(http://www.google.com)

if response.status_code == 200:
  print('Success!')
elif response.status_code == 404:
  print('Not Found')
elif response.status_code == 500:
      

