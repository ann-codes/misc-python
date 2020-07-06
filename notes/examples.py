###################### Exercises

import random

word_file = "ex_words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    return word_list[int(random.random() * len(word_list))] + \
    word_list[int(random.random() * len(word_list))] + \
    word_list[int(random.random() * len(word_list))]

## theirs
def generate_password2():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

def generate_password3():
    return ''.join(random.sample(word_list,3))

# test your function
print("YOUR NEW PASSWORD", generate_password())

###################### Exercises

filename = "ex_flowers.txt"

# function that creates a flower_dictionary from filename
def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower() 
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict

# Main function that prompts for user input, parses out the first letter
# includes function call for create_flowerdict to create dictionary
def main(): 
    flower_d = create_flowerdict(filename)
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
# print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

main()