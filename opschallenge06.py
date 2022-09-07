#!/usr/bin/env python3

# Script: Ops 301 Class 06 Ops Challenge Solution
# Author: Justin Buffington
# Date of latest revision: 9/6/2022
# Purpose: Prints various hardware specs using Bash commands 

# Main

import subprocess
subprocess.run(["whoami"])
subprocess.run(["ip", "a"])
subprocess.run(["lshw", "-short"])

# subprocess.run is used for individual commands, while subprocess.call is used for scripts

# End
