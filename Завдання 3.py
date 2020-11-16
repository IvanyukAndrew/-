import math
x1 = float(input("x1=")) #точ. А
y1 = float(input("y1="))

x2 = float(input("x2=")) #точ. B
y2 = float(input("y2="))

x3 = float(input("x3=")) #точ. С
y3 = float(input("y3="))


AB = math.sqrt((x2-x1)**2 + (y2-y1)**2)
BC = math.sqrt((x3-x2)**2 + (y3-y2)**2)
AC = math.sqrt((x3-x1)**2 + (y3-y1)**2)

if AB+BC>AC:
    print("Трикутник гострьокутній")
else:
    print("Трикутник не гострьокутній")