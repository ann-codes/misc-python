## Functions

# how to define a function, also can set default param value
def function_name_hello_world(param_your_name="World"):
  return "Hello {}!".format(param_your_name)
print(function_name_hello_world("Ann"))
print(function_name_hello_world())


def readable_timedelta(days):
  """
  alt_weeks = days//7
  print("using integer division for weeks", alt_weeks)
  """ # this is a docstring w/ the 3 quotes can be used inside of func 
  return "{} week(s) and {} day(s).".format(int(days/7), (days%7))
print(readable_timedelta(500))


######### Lambda expressions (aka anonymous functions)
double_lambda = lambda number: number * 2
print("lambda", double_lambda(20))
# vs function
def double_func(number):
  return number * 2
print("function", double_func(20))

multipy_lambda = lambda x, y: x*y
print("lambda", multipy_lambda(20, 10))
# vs function
def multiply_func(x, y):
  return x*y
print("function", multiply_func(20, 10))


# Using map()
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]
# function
def mean(num_list):
    return sum(num_list) / len(num_list)
averages = list(map(mean, numbers))
# lambda
averages = list(map(lambda list: sum(list) / len(list), numbers))
print(averages)


# using filter()
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]
# function
def is_short(name):
    return len(name) < 10
short_cities = list(filter(is_short, cities))
# lambda
short_cities = list(filter(lambda city: len(city) < 10, cities))
print(short_cities)


######### NOTES
# UnboundLocalError occurs if we try to change or reassign this global variable (variable scope)
# Lambdas should only be used for short functions, not too complex for readability