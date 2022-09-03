#!/bin/bash

# Script: Ops 301 Class 04 Ops Challenge Solution
# Author: Justin Buffington
# Date of latest revision: 9/1/2022
# Purpose: Provides a user with a set of options to chose from and executes the selected option

# Main

PS3='Please select an option: ' # PS3 is the parameter for the select command

select opt in "Hello World" "Ping self" "IP info" "Exit" # this creates the option menu using the select loop
do
    case $opt in
        "Hello World") # this prints Hello World! to the terminal
            echo "Hello World!"
            ;;
        "Ping self") # this pings the local loopback address
            ping -c 3 localhost
            ;;
        "IP info") # this displays the network adapter info
            lspci | grep -1 net
            ;;
        "Exit") # this exits the loop and stops the script
            break
            ;;
    esac
    REPLY= # this makes the menu appear after picking an option
done

# Main
