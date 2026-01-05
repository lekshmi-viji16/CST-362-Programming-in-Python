p = float(input("Enter percentage: "))
if p >= 90:
    grade = "O (Outstanding)"
elif p >= 85:
    grade = "A+ (Excellent)"
elif p >= 80:
    grade = "A (Very Good)"
elif p >= 70:
    grade = "B+ (Good)"
elif p >= 60:
    grade = "B (Above Average)"
elif p >= 50:
    grade = "C (Average)"
elif p >= 45:
    grade = "P (Pass)"
else:
    grade = "F (Fail)"
print("Percentage:", p)
print("Grade:", grade)

"""
output:
Enter percentage: 79
Percentage: 79.0
Grade: B+ (Good)
"""