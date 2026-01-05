a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("Largest:", a)
elif b > c:
    print("Largest:", b)
else:
    print("Largest:", c)

"""
output:
Enter first number: 20
Enter second number: 98
Enter third number: 35
Largest: 98
"""