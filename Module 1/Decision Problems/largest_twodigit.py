n = int(input("Enter a two-digit number: "))
d1 = n//10
d2 = n%10

if d1>d2:
    print("largest digit:", d1)
else:
    print("largest digit:", d2)

"""
output:
Enter a two-digit number: 27
largest digit: 7
"""