'''
--------------------------
Name: problem2.py
Purpose: Calculates the number of chickens shared between students and Mr. Fabroa

Author: James Bian

Created: date 07/12/2020
--------------------------
'''



students = float(input('How many students are in you class, Mr Fabroa?: '))
chicken = int(input("how many pieces of chicken from Popeyes did you get?: "))
divide =  chicken / students
fabroa = chicken % students
print ("Each student gets this many chickens: ", divide)
print ("Mr. Fabroa gets: ", fabroa)

