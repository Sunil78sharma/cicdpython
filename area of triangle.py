import math

a=float(input("enter first side"))
b=float(input("enter second side"))
c=float(input("enter third side"))
s=(a+b+c)/2
z=(s*(s-a)*(s-b)*(s-c))
d=math.sqrt(z)
print(d) 