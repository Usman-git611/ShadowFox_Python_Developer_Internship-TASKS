#BMI Calculator

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2) # Calculate BMI


if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")

#Output : 
# Enter height in meters: 1.67
# Enter weight in kilograms: 75
# Overweight