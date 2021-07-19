# in general, functions do something
# sometimes, functions "return" data / some expression to help whatever "called" it

def first_function():
    print("hello world")
    print("hello world again")

first_function() # calling first_function, calling = activating some function

def second_function(num):
    print(num+1)

second_function(6) # prints 7

second_function(3) # prints 4

# both first_function and second_function do not return anything

print( second_function(8) )

def third_function(num):
    print(num+1,"from inside third_function")
    return num-1

print(third_function(10),"from outside third_function")

def fourth_function(num1, num2): # num1, num2 are "arguments", "parameters" - they're like variables
    return num1+num2

print(fourth_function(7,12))

def fifth_function(num1, num2 = 8, mult = 1): # mult is now an optional argument
    return (num1+num2) * mult

print(fifth_function(3,4,2))

print(fifth_function(6,2))

print(fifth_function(10))