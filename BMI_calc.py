# Body mass index is a value derived from the mass and height of a person. 
# The BMI is defined as the body mass divided by the square of the body height, 
# and is universally expressed in units of kg/m², resulting from mass in kilograms and height in metres.
# Make a BMI calculator.
# Formula = mass / height*2

print("Welcome to your BMI calculator")
mass = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in metres: "))

bmi = mass / (height * height)

if bmi < 18.5:
  print(f"with a BMI of {bmi:.0f} You are Underweight")
elif bmi <= 25:
  print(f"with a BMI of {bmi:.0f} You have Normal Weight")
elif bmi <= 30:
  print(f"with a BMI of {bmi:.0f} You are Overweight")
elif bmi <= 35:
  print(f"with a BMI of {bmi:.0f} You are Obese")
else:
  print(f"with a BMI of {bmi:.0f} You are clinically Obese")

#print(f'Your BMI is : {bmi:.2f}')



