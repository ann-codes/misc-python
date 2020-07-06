# Conditional Statements

balance = 12 # edit this

if balance < 5: 
  print("the balance is less than 5")
elif balance < 10:
  print("the balance is between 5 and 10")
else: 
  print("the balance is greater than 10")


if balance % 2 == 0:
  print("the balance is even")
else:
  print("the balance is odd")


answer = 100
guess = 9
if answer > guess:
    result = "Oops!  Your guess was too low."
elif answer < guess:
    result = "Oops!  Your guess was too high."
elif answer == guess:
    result = "Nice!  Your guess matched the answer!"
print(result)


# from udacity, note the .format
state = 'CA'
purchase_amount = 2000.00    # a sample state and purchase amount

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
print(result)


## Falsy
# constants defined to be false: None and False
# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# empty sequences and collections: '"", (), [], {}, set(), range(0)