# 1. Average Salary Excluding Min and Max (Using Map & Filter)

# Problem Statement
# You are given a list of dictionaries where each dictionary represents an employee with name and salary.

# Remove the employees with the minimum and maximum salary, then return the average salary of the remaining employees.

# Input

# employees = [
#     {"name": "A", "salary": 30000},
#     {"name": "B", "salary": 50000},
#     {"name": "C", "salary": 40000},
#     {"name": "D", "salary": 60000}
# ]


employees = [
    {"name": "A", "salary": 30000},
    {"name": "B", "salary": 50000},
    {"name": "C", "salary": 40000},
    {"name": "D", "salary": 60000}
]

# Step 1: Get all salaries using map()
salaries = list(map(lambda emp: emp["salary"], employees))

# Step 2: Find minimum and maximum salary
min_salary = min(salaries)
max_salary = max(salaries)

# Step 3: Remove employees with min and max salary using filter()
filtered_salaries = list(filter(
    lambda salary: salary != min_salary and salary != max_salary,
    salaries
))

# Step 4: Calculate average of remaining salaries
average_salary = sum(filtered_salaries) / len(filtered_salaries)

print("Average salary (excluding min and max):", average_salary)
