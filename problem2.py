'''
--------------------------
Name: problem2.py
Purpose: Calculates the number of chickens shared between students and Mr. Fabroa

Author: James Bian

Created date: 07/12/2020
--------------------------
'''

#Gets input for amount of students
students = float(input('How many students are in you class, Mr Fabroa?: '))
#Gets input for amount of chicken
chicken = int(input("how many pieces of chicken from Popeyes did you get?: "))
#Calculates the amount of chicken each student gets
divide = chicken // students
#Calculates the amount of chicken Mr. Fabroa gets
fabroa = chicken % students
#Prints calculations
print("Each student gets this many chickens: ", divide)
print("Mr. Fabroa gets: ", fabroa)
