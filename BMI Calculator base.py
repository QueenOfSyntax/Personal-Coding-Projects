height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight kilograms: "))

bmi = weight / (height ** 2)
 
print(f"Your BMI is {bmi}")

if bmi < 18.5:
   print("You are underweight")
elif 18.5 <= bmi < 25:
   print("You are a normal weight")
elif 25 <= bmi < 30:
   print("You are overweight")
else:
   print("You are obese")
     