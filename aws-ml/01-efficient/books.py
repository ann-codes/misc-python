import time
import pandas as pd
import numpy as np


with open('books_published_last_two_years.txt') as f:
    recent_books = f.read().split('\n')
    
with open('all_coding_books.txt') as f:
    coding_books = f.read().split('\n')

######################## inefficient code, need to optimize
start = time.time()
recent_coding_books = []

for book in recent_books:
    if book in coding_books:
        recent_coding_books.append(book)

print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))

# Duration: 30.193002462387085 seconds



######################## Make more efficient
# ### Tip #1 Use numpy's `intersect1d` method to get the intersection of the `recent_books` and `coding_books` arrays.

start = time.time()
recent_coding_books = np.intersect1d(recent_books, coding_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))
# Duration: 0.04543328285217285 seconds




# ### Tip #2: Know your data structures and which methods are faster
# Use the set's `intersection` method to get the common elements in `recent_books` and `coding_books`. NOTE this method does not need numpy import, is built in

start = time.time()
recent_coding_books = set(recent_books).intersection(coding_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))
# Duration: 0.012140274047851562 seconds



