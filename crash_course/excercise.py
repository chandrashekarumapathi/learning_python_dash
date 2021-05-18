# TODO: 1) Import numpy and pandas
import numpy as np
import pandas as pd

# TODO: 2) Set numpy random number generator to seed = 101
np.random.seed(101)

# TODO: 3) Create a numpy matrix for 100 rows and 5 columns consisting of 100 random integers from 1 - 100
matrix = np.random.randint(1, 101, (100, 5))

# TODO: 4) Now use this numpy array as a pandas dataframe
df = pd.DataFrame(matrix)

# TODO: 5) Rename the dataframe columns to something else
df.columns = ['f1', 'f2', 'f3', 'f4', 'label']
# print(df)

# TODO: 6) Create a pandas dataframe with 5 columns with each column having 50 rows of random numbers as data. The
#  random numbers must be between 0 - 100

random_numbers = np.random.randint(0, 100, (50, 4))
columns = 'A B C D'.split()
df = pd.DataFrame(data=random_numbers, columns=columns)
print(df)
