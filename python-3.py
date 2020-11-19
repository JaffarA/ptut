# introduction to python
# 3 - io, loops & functions

# functions are pieces of code that take inputs and return an output
def get_name(prompt):
  return input(prompt)
# this code is indented because python uses indentation to define a blocks dimensions
# the code on the line above uses def command to define a function, 'get_name' which will prompt the user for their name
# there are many ways of getting inputs from python, the input function is one of the simplest 
# but will help you understand how functions work, and to give you an idea of how you could use data

def get_type(obj):
  return type(obj)
print('not part of the function')
# this example function returns the 'type' of an object passed to it.
# the 14th line, is not part of the function because it is outside of the indented block
# to call a function you use it's command and pass any values if needed
# you can also chain functions as shown below
name_type = get_type(get_name('What is your name: '))
print(name_type) # will print -> string


# another feature of python is iteration, iteration allows you to run code as many times as you want
# an example usecase of this would be a password entry program
attempts = 0
password = 'cheese'
while attempts: # this line is responsible for iteration
  attempts += 1 # increases the value of attempts by 1, which will repeat everytime the loop continues
  if get_name('Please enter the password: ') == password: # retrieves user-input inline and checks against stored pass
    print('Access Granted')
  else: # if the user-inputted password does not match the password it will go to this else branch of the if-statement
    print('Access Denied')


# exercise 1
# fill in the blanks (#) below to make the final line print 'i understand variables 3'
def password_program(password):
  attempts = 0
  while # insert a conditional that will stop the code after 3 attempts
    attempts # iterate attempts
    if get_name('Please enter the password: ') == password:
      print('Access Granted')
      attempts = # what value should be assigned to stop the loop
    else:
      print() # fill this in to say 'Access Denied'


# exercise 2
# write a function which asks for someone's name and greets them
