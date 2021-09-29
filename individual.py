# Variant 1
from math import fabs, sqrt

num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
arithmetic = (fabs(num1) + fabs(num2)) / 2
geometric = sqrt(fabs(num1) * fabs(num2))
print(f"Arithmetical mean = {arithmetic}")
print("Geometric mean = %.3f" % geometric)
