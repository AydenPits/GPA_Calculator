#
# Program Name: GPA Calculator
#
# Author: Ayden Pitstick
#
# SDEV220
#
# 11/8/2022
#
# Description: Program accepts lastname, firstname, and GPA from a user to calculate 
# whether the student has made the Honor List, Dean's List, or Niether.
# 
# Variables:
# 
# lastname - User input for last name
# firstname - User input for first name
# gpa - User input for GPA
# deanGPA - GPA to make dean's list
# honorGPA - GPA to make honor list

deanGPA = 3.5
honorGPA = 3.25

lastname = input("Enter Student's Lastname or type ZZZ to exit: ")

while lastname != ("ZZZ"):
    firstname = input("Enter Student's Firstname: ")
    gpa = float(input("Enter Student's GPA: "))
    if gpa >= deanGPA:
        print("You have made the Dean's List!")
        break
    elif gpa >= honorGPA:
        print("You have made the Honor List!")
        break
    elif gpa <= honorGPA:
        print("You have not qualified for the Honor list or the Dean's List.")
        break