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

# Step 1: Get all salaries
salaries = list(map(lambda emp: emp["salary"], employees))

# Step 2: Find minimum and maximum salary
min_salary = min(salaries)
max_salary = max(salaries)

# Step 3: Remove employees with min and max salary
filtered_employees = list(filter(
    lambda emp: emp["salary"] != min_salary and emp["salary"] != max_salary,
    employees
))

# Step 4: Get remaining salaries
remaining_salaries = list(map(lambda emp: emp["salary"], filtered_employees))

# Step 5: Calculate average
average_salary = sum(remaining_salaries) / len(remaining_salaries)

# Print all results
print("Minimum Salary:", min_salary)
print("Maximum Salary:", max_salary)
print("Remaining Employees:", filtered_employees)
print("Remaining Salaries:", remaining_salaries)
print("Average Salary (excluding min and max):", average_salary)
