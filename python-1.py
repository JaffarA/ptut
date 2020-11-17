# introduction to python
# 1 - hello world
# every programmer goes through the hello world rite of passage.
# in python this can be done on one line.

# function ( parameters )
print('hello world')
# the code on the line above uses the function 'print' to write to terminal
# the () signifies the invocation of the function and is used to pass arguments
# the 'hello world' part of the code is a string, denoted by the quotation marks
# the code within the parenthesis is the argument used by the function
# so, what we're doing is calling the 'print' function, and passing it a string


# an example use-case of print.
# in a domino notebook, we may want to check the value of a variable created elsewhere

result = 214 * 940
house_census = [
  'Jaf',
  'Tim',
  'Chloe'
]

# to print the value of result we can do
print(result)
# or we can even print specific entries from a list variable
print(house_census[0])
# we can even manipulate and combine strings
print('The people who live in this house are:', house_census)
print('214 * 940 is', result)


# exercise 1
# fill in the blank (X) below to make the code work and output 'I work at Cardif Pinnacle'
company = 'Cardif Pinnacle'
print('I work at', X)
