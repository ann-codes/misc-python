##### Inputs

# name = input("What's your name? ")
# ans = "Hello " + name.title() + ". "
# print(ans)

# # need to wrap in int() or float() if you want a number
# num = int(float(input("Give a number: ")))
# print(ans * num)

print("===================================")

##### Their Sample

# names = input("Enter names separated by commas: ").title().split(",")
# assignments = input("Enter assignment counts separated by commas (integer): ").split(",")
# grades = input("Enter grades separated by commas (integer): ").split(",")

# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"

# for name, assignment, grade in zip(names, assignments, grades):
#     print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))

print("===================================")

##### Error handling with Try/Except

# try: 
#   x = int(input("Enter your lucky integer: "))
# except (ValueError, KeyboardInterrupt): # can have more than one exception in a line
#   print("Need a valid integer!")
# except KeyboardInterrupt: # or different line
#   print("Why are you leaving?!")
# else:
#   print("Your lucky number is: ", x)
# finally: 
#   # finally will run in any condition of the try statement (such as ctrl+C to exit program)
#   # useful if you are calling packages and need to close out some resource
#   print("Attempts have been made.")

print("===================================")

##### Sample Problem

def party_planner(cookies, people):
    leftovers = None
    num_each = None

    # try/except practice, make sure no ZeroDivisionError occurs.
    try: 
      num_each = cookies // people
      leftovers = cookies % people
    except Exception as e: ## can be generic "Exception" and print out error message as "e"
      print("Must be greater than 0 people! \nError occurred: {}".format(e))

    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")

print("===================================")

##### Sample Problem 2

# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers 
for i in range(10):
    userInput = int(input("Enter any 2-digit number: "))
    
# check to see if number is even and if yes, add to list_sum
# print incorrect value warning  when ValueError exception occurs
    try:
        number = userInput
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))