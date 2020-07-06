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
    # TODO: Add a try-except block here to
    #       make sure no ZeroDivisionError occurs.
    num_each = cookies // people
    leftovers = cookies % people

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