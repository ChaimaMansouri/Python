#kwargs**
#utilise for dictionary of arguments
#kwargs** and args* thier names can be changed while preserving the symbols ** and *


"""if you don't know how many arguments that will be passed into your function, add a ** before the parameter name in the function definition."""
def my_function(**kwargs):
    print(kwargs)


my_function(first='Geeks', mid='for', last='Geeks')

def my_function_two(**k):
    print(k)
    

my_function_two(first='Geeks', mid='for', last='Geeks')