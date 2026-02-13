# 3. Student Weighted Score Calculator
# Problem Statement
# You are given a list of students:

# Task:
# • Keep students whose average is ≥ 60
# • Increase each mark by 5 grace marks
# • Compute the total of all updated marks
# Input
# students = [
#     {"name": "A", "marks": [50, 60, 70]},
#     {"name": "B", "marks": [30, 40]},
#     {"name": "C", "marks": [80, 90]}
# ]

# Output: 
# 375



students = [
    {"name": "A", "marks": [50, 60, 70]}, 
    {"name": "B", "marks": [30, 40]},  
    {"name": "C", "marks": [80, 90]}    
]

total = 0

for student in students:
    marks = student["marks"]
    
    average = sum(marks) / len(marks)
    
    if average >= 60:
        for mark in marks:
            new_mark = mark + 5
            total = total + new_mark

print(total)

