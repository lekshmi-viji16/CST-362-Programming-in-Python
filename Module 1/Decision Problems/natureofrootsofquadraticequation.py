a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = b*b - 4*a*c
if d>0:
    print("Two distinct real roots")
elif d==0:
    print("Two equal real roots")
else:
    print("No real roots")

"""
output:
Enter a: 2
Enter b: 3
Enter c: 1
Two distinct real roots
"""