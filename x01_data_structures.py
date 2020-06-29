# Data Structures

# Lists
list = ["a", "b", "c", "d", "e", "f", "g"]
print(list[4]) #e
print(list[-1]) #g
list.append("h") #adding "h" to end of list
print(list) #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
list.pop() #removing last item at end of list "h"

slice = list[4:-1]  
# starting index: index up to but not including
print(slice) #['e', 'f']

bool1 = "e" in list
bool2 = "x" in list
print(bool1) #True
print(bool2) #False

# List Methods
print(len(list))
join1 = "###".join(list)
print(join1)
print(max(list))
print(min(list))
print(sorted(list, reverse=True))

# Tuples: immutable, ordered data structure that can be indexed and sliced like a list, defined by listing a sequence of elements separated by commas, optionally contained within parentheses: ().
tuple1 = ("t1", "t2") #call by index similar to list
# compact way to assign
dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))
print (dimensions)

# Sets (Unique array list, mutable, unordered, can't slice)
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)
print(3 in unique_nums)
unique_nums.add(8) # uses .add() instead of .append
print(unique_nums)

# Dictionary (list of key value pairs, a la object/hash)
# mutable, unordered data structure that contains mappings of keys to values. Keys must be unique and immutable. 
dict1 = {"a":1, "b":2, "c":3}
print(dict1["a"]) # 1
dict1["d"] = 4 #adding new value
print(dict1)
# if calling a key that does not exist, it will error
# better to use "in/not in" vs calling the key directly
print("c" in dict1)

# Complex data structures like nested dictionary as value inside of dictionary can be accessed similarly to JS i.e. 
# hydrogen_weight = elements["hydrogen"]["weight"]

############ Exercise1
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
# print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
# print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
# print(verse_set, '\n')

# # print the number of unique words
num_unique = len(verse_set)
print(num_unique, '\n')

############ Exercise2
verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
# print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
# print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
# print(contains_breathe)

# create and sort a list of the dictionary's keys
# keys_only = verse_dict.keys()
# key_list = []
# for key in keys_only:
#   key_list.append(key)
# sorted_keys = sorted(key_list)
sorted_keys = sorted(verse_dict.keys())
# print(sorted_keys)

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1]) 

##################

# Data Structure	Ordered	Mutable	Constructor	Example
# List	Yes	Yes	[ ] or list()	[5.7, 4, 'yes', 5.7]
# Tuple	Yes	No	( ) or tuple()	(5.7, 4, 'yes', 5.7)
# Set	No	Yes	{}* or set()	{5.7, 4, 'yes'}
# Dictionary	No	No**	{ } or dict()	{'Jun': 75, 'Jul': 89}