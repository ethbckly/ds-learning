import pandas as pd

# Two fictional tables

employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'dept_id': [101, 102, 101, 103, 102]
})

departments = pd.DataFrame({
    'dept_id': [101, 102, 104],
    'dept_name': ['Engineering', 'HR', 'Marketing']
})

# TASK 1 - Merge these two tables so you only see employees with a matching department
df = pd.merge(employees, departments, on='dept_id', how='inner')

# TASK 2 - Merge so I see ALL employees, regardless of matching department
# df = pd.merge(employees, departments, on='dept_id', how='left')

# TASK 3 - How many employees are in each apartment?
print(df['dept_name'].value_counts())