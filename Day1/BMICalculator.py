weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
weight = 72.0

bmi = weight/(height * height)
if (bmi < 18):
    status = "Underweight"
elif bmi < 25:
    status = "Ideal"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print("You are %s and your bmi is %.1f"%(status,bmi))
