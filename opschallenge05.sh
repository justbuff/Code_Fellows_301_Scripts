#!/bin/bash

# Script: Ops 301 Class 05 Ops Challenge Solution
# Author: Justin Buffington
# Date of latest revision: 9/2/2022
# Purpose: Prints and clears specific log files

# Main

# This displays the contents of the log files
cat /var/log/syslog
cat /var/log/wtmp

# This deletes the contents of the log files

cat /dev/null > /var/log/syslog
cat /dev/null > /var/log/wtmp

# This displays the contents again (empty)

cat /var/log/syslog
cat /var/log/wtmp

# End
