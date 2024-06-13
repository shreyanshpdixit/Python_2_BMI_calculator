height = input("Enter your height in m:\n")
weight = input("Enter your weight in kg:\n")

w = int(weight)
h = float(height)

ans = w/(h*h)
BMI = int(ans)

print("Your BMI is: " + str(BMI))