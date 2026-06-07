import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

# TASK 1 - Create a pivot table showing survival rate by sex and pclass
print(df.pivot_table(values='survived', index='sex', columns='pclass', aggfunc='mean'))

# TASK 2 — Create a pivot table showing mean fare by embark_town and pclass
print(df.pivot_table(values='fare', index='embark_town', columns='pclass', aggfunc='mean'))

# TASK 3 — Which embarkation town and class combination had the highest fare?
# Cherbourg class 1

df = pd.DataFrame({
    'name': ['  alice smith', 'BOB JONES', 'Charlie Brown  ', 'diana prince'],
    'email': ['alice@gmail.com', 'bob@yahoo.com', 'charlie@gmail.com', 'diana@outlook.com'],
    'department': ['engineering', 'HR', 'engineering', 'Marketing']
})

# TASK 1 — Strip whitespace and make all names lowercase
df['name'] = df['name'].str.strip().str.lower()


# TASK 2 — Extract just the domain from the email column (gmail, yahoo, outlook)
#hint: use .str.split() and think about what to split on
df['email'] = df['email'].str.split('@').str[1].str.split('.').str[0]

# TASK 3 — How many people use each email domain? (use value_counts)
print(df.value_counts('email'))

# TASK 4 — Standardise the department column so everything is lowercase
df['department'] = df['department'].str.lower()



df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Diana', 'Bob'],
    'email': ['alice@gmail.com', 'bob@yahoo.com', 'charlie@gmail.com', 
              'alice@gmail.com', 'diana@outlook.com', 'bob@work.com'],
    'department': ['Engineering', 'HR', 'Engineering', 'Engineering', 'Marketing', 'HR']
})

# TASK 1 — How many duplicate rows are there?
print(df.duplicated().sum())

# TASK 2 — Remove fully duplicate rows
df = df.drop_duplicates()

# TASK 3 — Bob appears twice but with different emails — find duplicates based on name only
print(df.duplicated(subset=['name']))

# TASK 4 — How many unique departments are there? (hint: not duplicates related, think about another method)
print(df['department'].nunique())
