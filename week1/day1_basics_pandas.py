import pandas as pd
import numpy as np

# Create a dataset
df = pd.DataFrame({
    'age': [23, 25, None, 31, 22, 25, None, 29],
    'salary': [30000, 45000, 52000, None, 29000, 45000, 61000, 48000],
    'department': ['HR', 'Eng', 'Eng', 'HR', 'Eng', 'Eng', 'HR', None]
})

# print(df.head()) # Prints the first 5 rows
# print(df.info()) # Tells me the rows, columns and each columns data-type
# print(df.describe()) # Quick summary of numeric columns - mean,min,max,SD,quartiles
# print(df.isnull().sum()) # How many nulls are there
# print(df.value_counts()) # How many times do things appear in columns

'''
print(df.groupby('department').agg({
    'salary': 'mean',
    'age': 'max'
}))
'''

# TASK 1 - How many nulls are in each column
print(df.isnull().sum())
# There are 2 in age, 1 in salary, 1 in department

# TASK 2 - What's the mean salary per department?
print(df.groupby('department').agg({
    'salary': 'mean'
}))
# English - 42750, HR - 45500

# TASK 3 - Fill missing ages with the median age
median_age = df['age'].median()
df['age'] = df['age'].fillna(median_age)
print(df['age'])

# TASK 4 - Drop any rows where department is null
df = df.dropna(subset=['department'])

# TASK 5 - Add a new column 'senior' - True if salary > 50,000
df['senior'] = df['salary'] > 50000

print(df)

