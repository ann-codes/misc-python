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

# can reassign by index or slice index
list[0] = "1"
list[3:4] = ["HELLO", "WORLD"]
print(list) ## ['1', 'b', 'c', 'HELLO', 'WORLD', 'e', 'f', 'g']
# delete by using del
del list[-1]
print(list) ## ['1', 'b', 'c', 'HELLO', 'WORLD', 'e', 'f']

# can do list concat with +, or replication with *
print([1,2,3]+[4,5,6])
print([1,2,3]*3)

# boolean to check value in list
bool1 = "e" in list
bool2 = "x" in list
bool3 = "z" not in list
print(bool1) #True
print(bool2) #False
print(bool3) #True

# List Methods
print("LIST METHODS ==========================", len(list))
join1 = "###".join(list)
print(join1)
print(max(list))
print(min(list))
print(sorted(list, reverse=True))
print("index of 'e' = ", list.index("e")) 
# .list() will return first of any dupe; if doesn't exist, will get exception
print(list) ## ['1', 'b', 'c', 'HELLO', 'WORLD', 'e', 'f']
list.append("Z") ## adds to the end; ['1', 'b', 'c', 'HELLO', 'WORLD', 'e', 'f', 'Z']
list.insert(1, "WHAT") ## adds to specific index, doesnt replace
list.remove("HELLO") 
# append and insert is only for list
print(list) ## ['1', 'WHAT', 'b', 'c', 'WORLD', 'e', 'f', 'Z']
# append and insert is only for list
list.sort() ## sorts based on ASCII (upper case will come before lowercase)
print(list) ##['1', 'WHAT', 'WORLD', 'Z', 'b', 'c', 'e', 'f']
list.sort(reverse=True) ## reverse sort
# note: can't sort a mixed list of types, will throw exception
print(list)
list.sort(key=str.lower) # this is true sort
print(list)


print("TUPLES ==========================")
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
keys_only = verse_dict.keys()
key_list = []
for key in keys_only:
  key_list.append(key)
sorted_keys = sorted(key_list)
sorted_keys = sorted(verse_dict.keys())
# print(sorted_keys)

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1]) 



### For Question 2: Please provide a list with the name(s) of the director(s) with 
### the most Oscar wins. The list can hold the names of multiple directors,
### since there can be more than 1 director tied with the most Oscar wins.
winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'], 1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'], 1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'], 1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'], 1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'], 1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'], 1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'], 1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'], 1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'], 1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'], 1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'], 1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'], 1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'], 1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'], 1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'], 1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'], 1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'], 1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}

most_win_director = []
win_count_dict = {}

# # Part 1 mine
# for winners in winners.values():
#     for name in winners: 
#         if name not in win_count_dict: 
#             win_count_dict[name] = 1
#         else:
#             win_count_dict[name] += 1

# Part 1 theirs NOTE use of get() method
for year, winnerlist in winners.items():
    for winner in winnerlist:
        win_count_dict[winner] = win_count_dict.get(winner, 0) + 1

## Part 2 mine 
highest_award = 0

for dir in win_count_dict.keys():
    if win_count_dict[dir] > highest_award:
        highest_award = win_count_dict[dir]
        most_win_director = []
        most_win_director.append(dir)
    elif win_count_dict[dir] == highest_award:
        most_win_director.append(dir)
        
## Part 2 Theirs NOTE methods used
highest_count = 0
most_win_director = []

for key, value in win_count_dict.items():
    if value > highest_count:
        highest_count = value
        most_win_director.clear()
        most_win_director.append(key)
    elif value == highest_count:
        most_win_director.append(key)
    else:
        continue

## Part 2 Their alternative using list comprehension
highest_count = max(win_count_dict.values())

most_win_director = [key for key, value in win_count_dict.items() if value == highest_count]

print("most_win_director = {}".format(most_win_director))


######################################################

# Data Structure	Ordered	Mutable	Constructor	Example
# List	Yes	Yes	[ ] or list()	[5.7, 4, 'yes', 5.7]
# Tuple	Yes	No	( ) or tuple()	(5.7, 4, 'yes', 5.7)
# Set	No	Yes	{}* or set()	{5.7, 4, 'yes'}
# Dictionary	No	No**	{ } or dict()	{'Jun': 75, 'Jul': 89}