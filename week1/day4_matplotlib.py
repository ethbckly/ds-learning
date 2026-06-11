import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Basic matplotlib setup:
'''
plt.figure(figsize=(6, 10))
plt.plot(x, y)
plt.title('My Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()
'''

df = sns.load_dataset('titanic')

# TASK 1 - Plot a histogram of passenger ages
plt.figure(figsize=(10, 6))
plt.hist(df['age'])
plt.title('Passenger ages Histogram')
plt.show()

# TASK 2 - Plot a bar chart of how many passengers were in each class
class_count = df['pclass'].value_counts()
plt.figure(figsize=(6, 10))
plt.bar(class_count.index, class_count.values)
plt.title('Passengers per class')
plt.show()

# TASK 3 - Plot a scatter plot of age vs fare
plt.figure(figsize=(10, 6))
plt.scatter(df['age'], df['fare'])
plt.title('Age vs Fare Scatter Plot')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()

# TASK 4 - Recreate scatter plot using seaborn
sns.scatterplot(x='age', y='fare', data=df, hue='survived')
plt.show()

# TASK 5 - Plot a boxplot of fare by passenger class
sns.boxplot(x='pclass', y='fare', data=df)
plt.ylim(0, 300)
plt.show()