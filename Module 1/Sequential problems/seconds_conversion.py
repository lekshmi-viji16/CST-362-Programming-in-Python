seconds=int(input("Enter total seconds:"))
hours=seconds//3600
minutes=(seconds%3600)//60
sec=seconds%60
print("Time=",hours,":",minutes,":",sec)

"""
output:
Enter total seconds:3671
Time= 1 : 1 : 11
"""