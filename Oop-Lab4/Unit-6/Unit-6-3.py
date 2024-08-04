# Page 12
# Example 1 : Working with dictionaries

grades = {'Alice': 85, 'Bob': 92, 'Charlie': 88, 'David': 95}
print("Bob's grade:", grades['Bob'])

grades['Alice'] = 90
for student, grade in grades.items():
        print(f"{student}: {grade}")
print("Frank's grade:", grades.get('Frank', 'grade not found'))


