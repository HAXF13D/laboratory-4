# Variant 5

h = int(input("Hours = "))
m = int(input("Minutes = "))
s = int(input("Seconds = "))
one_hour = 30
one_min = one_hour / 60
one_sec = one_min / 60
deg = h * one_hour + m * one_min + s * one_sec
print("Degrees = %.2f" % deg)
