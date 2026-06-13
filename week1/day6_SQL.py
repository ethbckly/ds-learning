import pandas as pd
import sqlite3

employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'dept_id': [101, 102, 101, 103, 102],
    'salary': [55000, 48000, 72000, 61000, 45000]
})

departments = pd.DataFrame({
    'dept_id': [101, 102, 104],
    'dept_name': ['Engineering', 'HR', 'Marketing'],
    'budget': [500000, 200000, 350000]
})

conn = sqlite3.connect(':memory:')
employees.to_sql('employees', conn, index=False, if_exists='replace')
departments.to_sql('departments', conn, index=False, if_exists='replace')

'''
# TASK 1 — Get all employees with their department name (inner join)
print(pd.read_sql("SELECT * FROM employees e INNER JOIN departments d on e.dept_id = d.dept_id", conn))

# TASK 2 — Get ALL employees even if they have no department (left join)
print(pd.read_sql("SELECT * FROM employees e LEFT JOIN departments d on e.dept_id = d.dept_id", conn))

# TASK 3 — Get employees with their department name and budget
print(pd.read_sql("SELECT * FROM employees e INNER JOIN departments d on e.dept_id = d.dept_id", conn))

# TASK 4 — What is the average salary per department name?
print(pd.read_sql("SELECT dept_name, AVG(salary) FROM employees e INNER JOIN departments d ON e.dept_id = d.dept_id GROUP BY dept_name", conn))

# TASK 5 — Find all employees who earn more than the average salary
print(pd.read_sql("SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)", conn))

# TASK 6 — Find all employees who work in the same department as Alice
print(pd.read_sql("SELECT * FROM employees WHERE dept_id = (SELECT dept_id FROM employees WHERE name = 'Alice')", conn))
'''

# TASK 7 — Find all departments that have at least one employee earning over 60000
print(pd.read_sql("SELECT * FROM departments WHERE dept_id IN (SELECT dept_id FROM employees WHERE salary > 60000)", conn))