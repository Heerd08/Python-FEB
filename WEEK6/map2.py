"""
Average Salary Excluding Min and Max (Using Map & Filter)
Problem Statement:
You are given a list of dictionaries where each dictionary represents an employee with name and salary.
Remove the employees with the minimum and maximum salary, then return the average salary of the remaining employees.

Input
employees = [
    {"name": "A", "salary": 30000},
    {"name": "B", "salary": 50000},
    {"name": "C", "salary": 40000},
    {"name": "D", "salary": 60000}
]
"""
def get_salary(employee):
    return employee["salary"]

def is_middle_salary(salary, min, max):
    return salary != min and salary != max

def average_salary(values):
    return sum(values)/len(values)

def average_salary_excluding_min_max(employees):

    salaries = list(map(get_salary,employees))
    print(salaries)

    min_salary = min(salaries)
    max_salary = max(salaries)

    def salary_filter(salary):
        return is_middle_salary(salary,min_salary,max_salary)

    middle_salary = list(filter(salary_filter,salaries))

    return average_salary(middle_salary)


def main():
    employees = [
    {"name": "A", "salary": 30000},
    {"name": "B", "salary": 50000},
    {"name": "C", "salary": 40000},
    {"name": "D", "salary": 60000}
    ]

    result = average_salary_excluding_min_max(employees)
    print(f"Average salary excluding min and max is {result}")

    

if __name__ == "__main__":
    main() 