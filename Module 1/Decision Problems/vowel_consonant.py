ch = input("Enter a character:")
if ch.isalpha():
    if ch.lower() in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")

"""
output:
Enter a character:b
Consonant
"""