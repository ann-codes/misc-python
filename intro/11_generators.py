# Iterators And Generators (WTF?)

"""
Iterables are objects that can return one of their elements at a time, such as a list. Many of the built-in functions we’ve used so far, like 'enumerate,' return an iterator.

An iterator is an object that represents a stream of data. This is different from a list, which is also an iterable, but is not an iterator because it is not a stream of data.

Generators are a simple way to create iterators using functions. You can also define iterators using classes

WHY? (from SO): Generators are a lazy way to build iterables. They are useful when the fully realized list would not fit in memory, or when the cost to calculate each list element is high and you want to do it as late as possible. But they can only be iterated over once.
"""

def my_range(x):
    i = 0
    while i < x:
        yield i # note the yield
        i += 1


print(my_range(3)) # <generator object my_range at 0x7fa06e354cf0>

#  since this returns an iterator, we can convert it to a list or iterate through it in a loop to view its contents
for x in my_range(5):
    print(x)


######## Exercise 1
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    count = start
    for x in iterable: 
        yield count, x
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

"""
Lesson 1: Why Python Programming
Lesson 2: Data Types and Operators
Lesson 3: Control Flow
Lesson 4: Functions
Lesson 5: Scripting
"""

######## Exercise 2

def chunker(iterable, size):
    # Yield successive chunks from iterable of length size.
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

# don't edit below
for chunk in chunker(range(25), 4):
    print(list(chunk))


"""
[0, 1, 2, 3]
[4, 5, 6, 7]
[8, 9, 10, 11]
[12, 13, 14, 15]
[16, 17, 18, 19]
[20, 21, 22, 23]
[24]
"""

######## Combining Generators and List Comprensions

sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares

print("list of squares =" , sq_list)
print(sq_iterator)