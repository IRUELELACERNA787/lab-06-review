import sys

weight = input("What is your weight? (in pounds) \n")
height = input("What is your height? (in inches) \n")

bmi = ((703 * float(weight))/pow(float(height),2))

print("Your body mass index (BMI) is " + str(bmi)+"%")