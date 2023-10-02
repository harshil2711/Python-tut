# To store same values in cache memory.
# It store every time you run the program


import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*2

print(fx(5))
print("executing for 5")
print(fx(10))
print("executing for 10")
print(fx(20))
print("executing for 20")
print(fx(5))
print("executing for 5")
print(fx(10))
print("executing for 10")
print(fx(20))
print("executing for 20")
print(fx(30))
print("executing for 30")

