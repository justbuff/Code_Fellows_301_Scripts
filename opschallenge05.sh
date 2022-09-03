#!/bin/bash

# Script: Ops 301 Class 05 Ops Challenge Solution
# Author: Justin Buffington
# Date of latest revision: 9/2/2022
# Purpose: Prints and clears specific log files

# Main

# Sets logs as variables
sysvar=/var/log/syslog
wtmpvar=/var/log/wtmp

# Function to print and delete logs
deletelog() {
  cat $1
  cat /dev/null/ > $1
  cat $1
}

deletelog $sysvar
deletelog $wtmpvar

# End
