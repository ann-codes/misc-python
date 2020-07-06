# List Comprehensions - short hand way of creating lists

example = ["a", "b", "c", "d", "e"]
capitalized = []

for x in example: 
  capitalized.append(x.upper())

print(capitalized)

# shorthand for list comprehensions (not common in other languages)

capped = [x.upper() for x in example]
print(capped)

# original list
print(list(range(10)))

# using range
squares = [x**2 for x in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# multiples of 3 in a list of 20 
multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]

# can include condition
squaresEven = [x**2 for x in range(10) if x % 2 == 0]
print(squaresEven) # [0, 4, 16, 36, 64]

# if it is even square, else add 3
square3 = [x**2 if x % 2 == 0 else x + 3 for x in range(10)]
print(square3) # [0, 4, 4, 6, 16, 8, 36, 10, 64, 12]

# create a new list first_names containing just the first names in names in lowercase.
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
first_names = [name.lower().split(" ")[0] for name in names]
print(first_names)

# comprehension in dictionary: create a list of names passed that only include those that scored at least 65. uses items()
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
passed = [name for name, score in scores.items() if score >= 65]
print(passed)

print(scores.items())