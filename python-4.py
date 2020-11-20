# introduction to python
# 4 - io, loops & functions cont..

# functions can take multiple arguments, default arguments and even optional arguments (part of *args)
def introduce(name='slim shady', age, hobby='fishing'):
  return print(f'Hi, my name is {name}. Hi, my age is {age}. Hi, i like this "{hobby}"')
# this code will by default work with only 1 variable passed.
introduce(8)
# we can even be explicit and say exactly what we want to pass
introduce(age=23, hobby='tacos')


# for-based iteration, previously we used while-based iteration but this option is more popular
# a for loop iterates a finite amount of times in what is called a count-controlled loop
# below are two examples of types of for-loops
items = ['eggs', 'cheese', 'milk']
for i in items: # we can iterate over a list object using each element as the i value
  print(f'Buying {i}\n') # \n adds a newline

# fixed-length for loop
for i in range(1, 100): # range technically creates a list object with every number between two points
  print(i, end='\n')


# exercise 1
# fill in the blanks (#) below to make the code run 3 times and stop if the password is correct with a for loop
def password_program(password):
  for # insert an i control statement
    if get_name('Please enter the password: ') == password:
      print('Access Granted') # fill this in to say 'Access Granted after {i} attempts'
      break # escape from the for loop
    else:
      print() # fill this in to say 'Access Denied. {i}/3 attempts left'


password_program('cheese')

# exercise 2
# write a function which asks for someone's name and uses a default greeting parameter
