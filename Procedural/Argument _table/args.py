#args**
#utilise for list of arguments
"""if you don't know how many arguments that will be passed into your function, add a * before the parameter name in the function definition."""

def my_function(*args):
    for i in args:
        i += i
    print(i)


my_function(1, 2, 3)
my_function(2)
my_function(6, 7, 8, 9)