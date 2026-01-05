password=input("enter password:")
length=len(password)
if length<6:
    print("weak")
elif 6<= length <= 10:
    print("medium")
else:
    print("strong")

"""
output:
enter password:abc@123
medium
"""  