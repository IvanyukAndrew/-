import math
x = float(input("Ведіть знаячення x = "))

if x**2+math.log(x)>0:
    print("y = cos(x**2+ln(x))")
elif x**2+math.log(x)<0:
    print("y = 1/(x**2+ln(x))")
else:
    print("cos(x)")