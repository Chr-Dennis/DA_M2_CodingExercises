# Run the cell below to load the Titanic dataset again. 
# Then, use the summary tools you’ve learned to explore the data and answer the prompts in the comments.

# -- IF WORKING IN VS CODE, PASTE THE CODE BELOW AND RUN -- #

import pandas as pd

# Load Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Preview the data
print(df.head())


# --- EXERCISE STARTS HERE --#
#answer the following using .describe(), .value_counts(), and column-level summary functions. 
# Put your code INSIDE the print statements!

# 1. Summarize the numeric columns
print(df.describe())

# 2. Use .value_counts() to see counts for embarkation ports
print(df['Embarked'].value_counts())

# 3. Use .value_counts() to count passenger classes
print(df['Pclass'].value_counts())

# 4. Show the average (mean) age of passengers
print(df['Age'].mean())

# 5. Show the maximum fare paid
print(df['Fare'].max())

# 6. Show how many unique names are in the dataset
print(df['Name'].nunique())

# 7. Show counts for values in the 'Sex' column
print(df['Sex'].value_counts())

# 8. Show how many unique values are in each column
print(df.nunique())
