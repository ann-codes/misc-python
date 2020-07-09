import time
import numpy as np

with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')
    
gift_costs = np.array(gift_costs).astype(int)  # convert string to int

# Task: sum all prices less than 25 and sum it up w/ tax included


############ Inefficient way
start = time.time()

total_price = 0
for cost in gift_costs:
    if cost < 25:
        total_price += cost
        #  * 1.08  # add cost after tax
total_price = total_price * 1.08

print(total_price)
print('Duration: {} seconds'.format(time.time() - start))
# 32765421.23999867
# Duration: 18.344516277313232 seconds


############ Efficient way
start = time.time()

# numpy makes it very easy to select all the elements in an array that meet a certain condition, and then perform operations on them together all at once. 
total_price = (gift_costs[gift_costs < 25]).sum() * 1.08

print(total_price)
print('Duration: {} seconds'.format(time.time() - start))
# 32765421.240000002
# Duration: 0.08283138275146484 seconds