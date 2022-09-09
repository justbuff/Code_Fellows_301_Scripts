# Script: Ops 301 Class 08 Ops Challenge Solution
# Author: Justin Buffington
# Date of latest revision: 9/8/2022
# Purpose: Creates a new Active Directory User with specific parameters using PowerShell

# Main

Import-Module ActiveDirectory

New-ADUser -Name "Franz Ferdinand" -Title "TPS Reporting Lead" -EmailAddress "ferdi@globexpower.com" -Department "TPS Department" -Company "GlobeX USA" -City "Springfield" -State "OR"

# End
