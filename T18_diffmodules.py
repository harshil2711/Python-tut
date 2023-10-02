# It will print random numbers between 0 to 5.
import random
import time

random_numbers = random.randint(0,5)

print(random_numbers)

# __________________________________________________________________
# It will print random items in the list.

lst = ['star plus' , 'zee tv'  , 'sony' , 'ESPN']
a = random.choice(lst)
print(a)

# __________________________________________________________________
# To give current timestamp
a = time.strftime('%H:%M:%S')

print(a)