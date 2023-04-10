# Get the path to the working directory.
import os
# cwd = os.getcwd()
# print("Current working directory:", cwd)

# Set the working directory.
path = r'C:\Users\1dns2\Documents\data_science'
os.chdir(path)
print("Current working directory:", path)

# List files in working directory.
files = os.listdir()
for file in files:
    print(file)


# Install the rpy2 library.
# py -m pip install pandas

# Import the rpy2 library.
import pandas as pd

# Import the csv data.
df = pd.read_csv('dogs_full.csv')

# Get number of columns and rows.
print(df.shape)

# Get column names.
print(df.columns)

# Get row names.
print(df.index)

# What is the overall struucture of the data?
print(df.info())

# Get top 10 rows.
print(df.head(10))

# Get statistical summaries.
print(df.describe())

# Get the mean of 3 numbers
def mean(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print(mean(1, 2, 3))

# Extract a single column of the data
height = df['height']
print(height)

# Standard Deviation of height
print(height.std())

# Check for NaN values
print(height.isnull())

# Get frequency for a categorical variable
print(height.isnull().value_counts())

# Get value by specific row and column
print(df.iloc[0, 0]) # 1st row, 1st column because python index starts at 0

print(df.iloc[0, ])

print(df.iloc[:, 0].isnull().value_counts())

# Get positions of specific values in a column
print(df[df['height'].isnull()])


# Make a scatter plot with x = datadog and y = popularity
import matplotlib.pyplot as plt
plt.scatter(df['datadog'], df['popularity'])
plt.show()
