import pandas as pd

df = pd.DataFrame(columns=['Name', 'Salary', 'Age'])
name = ["Ram", "Raj", "Jay"]
salary = [1000, 2000, 5000]
age = [24, 25, 26]
df['Name'] = name
df['Salary'] = salary
df['Age'] = age

# Selecting whole dataframe
print(df)

# Selecting only one column from the dataframe
print(df['Name'])

# Selecting multiple columns from the dataframe
print(df[['Name', 'Salary']])