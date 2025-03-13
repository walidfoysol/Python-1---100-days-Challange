print("    ********BMI  CALCULATOR**********    ")

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height**2),1)

print(f"Your BMI is {bmi}")
if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You have normal weight")
elif bmi < 30:
    print("You are slightly overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")

