import sys

weight = float(input("What is your weight? (in pounds) \n"))
height = float(input("What is your height? (in inches) \n"))

bmi = ((703 * weight)/(height*height))
bmi = str(bmi)

print("Your body mass index (BMI) is " + bmi+"%")