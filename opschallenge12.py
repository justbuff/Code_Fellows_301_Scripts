#!/usr/bin/env python3

# Script: Ops 301 Class 12 Ops Challenge Solution
# Author: Justin Buffington
# Date of latest revision: 9/14/2022
# Purpose: Use Psutil to get specific CPU info

# Main

import psutil

psutil.cpu_times().user, psutil.cpu_times().system, psutil.cpu_times().idle, psutil.cpu_times().nice, psutil.cpu_times().iowait, psutil.cpu_times().irq, psutil.cpu_times().softirq, psutil.cpu_times().steal, psutil.cpu_times().guest

# End
