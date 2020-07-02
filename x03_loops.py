# For Loops - used when the number of iterations is known or finite

# using range(start, stop, step) in forloops
# print 5,10,15,20,25,30 w/ forloop: 
for n in range(5, 31, 5):
  print (n)

# for n in range(0, 31, 5):
#   if n > 0:
#     print(n)

# for num in range(0, 31):
#   if num % 5 == 0 and num > 0:
#     print(num)


letters = ["a", "b", "c", "d", "e"]
for idx in range(len(letters)):
  letters[idx] = letters[idx].title()
print(letters)

for letter in letters:
  print(letter.title())


# print the following ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(" ", "_"))

# for i in range(len(names)):
#     usernames.append(names[i].replace(" ", "_").lower())

print(usernames)

# mutate
for i in range(len(usernames)):
    usernames[i] = usernames[i].replace(" ", "_").upper()
print(usernames)

# print the following
# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>

items = ['first string', 'second string']
html_str = "<ul>\n"

for i in range(len(items)):
    html_str += "<li>" + items[i] + "</li>\n"
    if i == len(items) -1:
        html_str += "</ul>"

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)

# more range
print(list(range(0, 8, 2))) # [0, 2, 4, 6]


##### loops and dictionaries
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}

## using typical way
# for word in book_title:
#     if word not in word_counter:
#         word_counter[word] = 1
#     else:
#         word_counter[word] += 1
        
# using get method => .get(key, value to return if key not found)
for index in book_title:
    word_counter[index] = word_counter.get(index, 0) + 1
print(word_counter)


cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

ppl = []

for key in cast:
  ppl.append(key)    
print(ppl)

for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))


# total up all fruits in basket
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# for key in basket_items:
#   if key in fruits: 
#     result += basket_items[key]
# print(result)

for object, count in basket_items.items():
   if object in fruits:
       result += count
print("There are {} fruits in the basket.".format(result))


######################################################################
# While Loops - used when the iterations need to continue until a condition is met


deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []
# https://www.programiz.com/python-programming/methods/built-in/sum
while sum(hand) <= 17:
  hand.append(deck.pop())
print(hand)

# Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square.

limit = 40
n = 0
nearest_square = 0
while n**2 < 40:
    nearest_square = n**2
    n+=1
print(nearest_square)


# add up the odd numbers in the list, but only up to the first 5 odd numbers together.
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

# Mine
total = 0
odd_count = 0

for n in num_list: 
    if n % 2 != 0 and odd_count < 5:
        total += n
        odd_count += 1
print(total)

# Theirs
count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)
while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1
print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))

######################################################################
# Zip - creating tuples

new_zip = list(zip(['a', 'b', 'c'], [1, 2, 3])) # [('a', 1), ('b', 2), ('c', 3)].
print("ZIP", new_zip)
for x in new_zip: 
  print(x[0], x[1])

# Unzip using asterisk *
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
print(letters) #('a', 'b', 'c')
print(nums) #(1, 2, 3)

# transposing from a 4-by-3 matrix to a 3-by-4 matrix
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
data_transpose = tuple(zip(*data))
print(data_transpose)

# Enumerate - iterate through the index
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e

# Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points. Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4.
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points = []

for x in list(zip(labels, x_coord, y_coord, z_coord)):
    points.append("{}: {}, {}, {}".format(x[0], x[1],x[2],x[3]))

for point in points:
    print(point)