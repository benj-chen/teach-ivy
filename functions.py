# in general, functions do something
# sometimes, functions "return" data / some expression to help whatever "called" it

def first_function():
    print("hello world")
    print("hello world again")

first_function() # calling first_function, calling = activating some function

def second_function(num): # num is an "argument", "parameter" - they're like variables
    print(num+1)

second_function(6) # prints 7, you have to put one value inside the parentheses for Python to
# understand. Otherwise, you get an error complaing about missing arguments.

second_function(3) # prints 4

# both first_function and second_function do not return anything, which means that when Python
# comes back from the function, it doesn't bring any value with it. So, when printed as an
# expression, since there is no value, None is printed. Same goes for making variables:
# foo = second_function(5) sets the value of foo to None.

print( second_function(8) ) # prints None

def third_function(num):
    print(num+1,"from inside third_function") # when num = 10, prints 11
    return num-1

print(third_function(10),"from outside third_function") # prints 9 because 10-1 = 9

def fourth_function(num1, num2): # num1, num2 are arguments
    return num1+num2

print(fourth_function(7,12))

def fifth_function(num1, num2 = 8, mult = 1): # mult is now an optional argument
    return (num1+num2) * mult

print(fifth_function(3,4,2)) # prints (3+4)*2 = 14

print(fifth_function(6,2)) # prints (6+2)*1 = 8, because mult = 1 when we don't provide mult

print(fifth_function(10)) # prints (10+8)*1 = 18, because we did not provide num2 or mult, so they
# each became their default value, which is 8 for num2 and 1 for mult.