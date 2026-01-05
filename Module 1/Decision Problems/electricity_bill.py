units = int(input("Enter units consumed: "))
if units <= 200:
    bill = units * 0.50
elif units <= 400:
    bill = 100 + (units - 200) * 0.65
elif units <= 600:
    bill = 230 + (units - 400) * 0.80
else:
    bill = 425 + (units - 600) * 1.25
print("Electricity Bill: Rs.", bill)

"""
output:
Enter units consumed: 350
Electricity Bill: Rs. 197.5
"""