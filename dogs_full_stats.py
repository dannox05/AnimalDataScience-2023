# Get the path to the working directory.
import os
# cwd = os.getcwd()
# print("Current working directory:", cwd)

# Set the working directory.
path = r'C:\Users\1dns2\Documents\data_science\AnimalDataScience'
os.chdir(path)
print("Current working directory:", path)

# List files in working directory.
files = os.listdir()
for file in files:
    print(file)


# Install the rpy2 library.
# py -m pip install pandas

# Import the pandas library.
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

# make the polt bigger
plt.figure(figsize=(30, 30))
plt.scatter(df['datadog'], df['popularity'])
plt.show()

# Add breed names to each plot point
plt.figure(figsize=(30, 30))
plt.scatter(df['datadog'], df['popularity'])
for i, txt in enumerate(df['breed']):
    plt.annotate(txt, (df['datadog'][i], df['popularity'][i]))
plt.show()

# Make the breed names smaller
plt.figure(figsize=(30, 30))
plt.scatter(df['datadog'], df['popularity'])
for i, txt in enumerate(df['breed']):
    plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8)
plt.show()


# Label each breed a color that corresponds to its group
plt.figure(figsize=(30, 30))
plt.scatter(df['datadog'], df['popularity'])
for i, txt in enumerate(df['breed']):
    if df['group'][i] == 'herding':
        plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8, color='red')
    elif df['group'][i] == 'sporting':
        plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8, color='blue')
    elif df['group'][i] == 'hound':
        plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8, color='green')
    elif df['group'][i] == 'terrier':
        plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8, color='orange')
    elif df['group'][i] == 'non-sporting':
        plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8, color='purple')
    elif df['group'][i] == 'toy':
        plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8, color='black')
    elif df['group'][i] == 'working':
        plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8, color='brown')
plt.show()

# Add a title and axis labels
plt.figure(figsize=(30, 30))
plt.scatter(df['datadog'], df['popularity'])
for i, txt in enumerate(df['breed']):
    if df['group'][i] == 'herding':
        plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8, color='red')
    elif df['group'][i] == 'sporting':
        plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8, color='blue')
    elif df['group'][i] == 'hound':
        plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8, color='green')
    elif df['group'][i] == 'terrier':
        plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8, color='orange')
    elif df['group'][i] == 'non-sporting':
        plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8, color='purple')
    elif df['group'][i] == 'toy':
        plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8, color='black')
    elif df['group'][i] == 'working':
        plt.annotate(txt, (df['datadog'][i], df['popularity'][i]), fontsize=8, color='brown')
plt.title('Best in Show')
plt.xlabel('Computed Datadog Score')
plt.ylabel('AKC Popularity Ranking')
plt.show()


# Save the plot to working directory
plt.savefig('best_in_show.png')


