
height = float(input("Height: "))
weight = int(input("Weihgt: "))

if height > 3:
    raise ValueError("Human height does not exceed 3 meters")

bmi = weight / height ** 2
print(bmi)