import sys
inches = input("Enter your height (inches): ")
weight = input("Enter your weight (pounds): ")

inches = float(inches)
weight = float(weight)

BMI =  (weight /(inches*inches)) * 703

print ("Your body mass index (BMI) is ", BMI)
