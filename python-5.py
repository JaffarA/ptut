# introduction to python
# 5 - data, import and manipulation


# pandas is a popular data library we can use for data import, manipulation and export
# to import pandas we use the following line
import pandas as pd
# we import as pd instead of pandas to make it quicker to type, this is common practice
# most examples you find will do this too
# we should import numpy also, pandas and numpy work together extremely well
# functions compliment eachother
import numpy as np
# similar to pandas, we import numpy as np


# we're going to use pandas 'read_csv' function to parse a CSV file included with this lesson 'python-5.csv'
# the 'read_csv' function takes a CSV file and puts into a pandas dataframe object
# we put our data into a dataframe because thats what pandas uses for all its functions
# first, make sure that this file and the CSV are in the same directory, otherwise you'll have to specify a path
df = pd.read_csv('python-5.csv')
# df is a common name for a dataframe in pandas, you'll come across this often
# in this statement we're creating a pandas dataframe based on the values in 'python-5.csv'


# to see what data we have we can use the head method to sneak a peek at the top 5 records
print(df.head())
# similar to print, df.head will output these values to terminal or a python notebook window
# it will also present them in a nice easily readable table

#      name  uno victories  instrument favourite colour
# 0  jaffar              2      guitar              red
# 1     tim            100       drums             pink
# 2   chloe            200    triangle             gold
# 3  serena            250  rain stick             blue
# 4   steve             99        bass            green


# lets explore our data, let's look at the first 5 records but this time only the instrument column
# pandas dataframes use list syntax for accessing rows/columns
print(df['instrument'].head())

# 0        guitar
# 1         drums
# 2      triangle
# 3    rain stick
# 4          bass
# Name: instrument, dtype: object

# the information at the bottom shows the column name, and datatype (dtype) of the data


# lets do something with the dataframe, let's figure out which colour is the most popular
# to do this we can use the built-in pandas 'value_counts' function
print(df['favourite colour'].value_counts())

# red       4
# green     2
# blue      2
# gold      1
# pink      1
# orange    1
# Name: favourite colour, dtype: int64

# we get a nice table of each colour represented in our data in descending order and with frequency on the right
print(df['favourite colour'].value_counts())


# exercise 1:
# using the code above (line 61), write a loop that
# prints the value_counts of each column in our df


# lets add a new column to our dataframe, is_champion depending
# on who has the highest wins we give this column a value of True or False
# we can do this using the built-in numpy 'where' function
# similar to SQL we specify conditions we want to meet and what values to assign based on that
df['is_champion'] = np.where(df['uno victories'] == df['uno victories'].max(), True, False)


# now lets print the rows where is_champion is false
print(df[df.is_champion == False])


# exercise 2:
# reverse the code above (line 81) to only show cases where favourite_colour is the most popular colour
