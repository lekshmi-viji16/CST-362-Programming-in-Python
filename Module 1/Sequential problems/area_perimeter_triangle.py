import math
a=float(input("enter side a:"))
b=float(input("enter side b:"))
c=float(input("enter side c:"))
p=a+b+c
s=p/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Perimeter=",p)
print("Area=",area)

"""
Output:
enter side a:3
enter side b:3
enter side c:5
Perimeter= 11.0       
Area= 4.14578098794425
"""