employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

employee_data = {employee: defaults.copy() for employee in employees}
print(employee_data)
