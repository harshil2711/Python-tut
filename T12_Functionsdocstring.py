def addition():
    print(5+6)

addition()

# Output
# 11
# ________________________________________________________________________________________________________

a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))

def avg():
    print((a+b)/2)

avg()

# Output
# 4.0
# ________________________________________________________________________________________________________

def sub(a,b):
    return a-b
    
v=sub(20,5)
print(v)

# Output
# 15
# ________________________________________________________________________________________________________

def division(a,b):
    print(a/b)

division(12,2)

# Output
# 6
# ________________________________________________________________________________________________________
def typo(x):
    return type(x)

print(typo(4))

# Output
# <class 'int'>
# ________________________________________________________________________________________________________
x = int(input('enter the number : '))
def ran(x):
    if x in  range(2,9) :
        print("yes")
    else:
        print("no")
ran(x)

# enter the number : 25
# no
# ________________________________________________________________________________________________________

def rever(x):
    return x[::-1]

n = input('Enter the string')

a = rever(n)
print(a)

# Output
# Enter the stringhalo
# olah

# ________________________________________________________________________________________________________

def rever(x):
    """Hello this is docstring testing"""
    return x[::-1]

print(rever.__doc__)
n = input('Enter the string \n')
print(rever(n))

# Output
# Hello this is docstring example
# Enter the string 
# hello
# olleh
# ________________________________________________________________________________________________________
def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)

# Output:
# 11715
# ________________________________________________________________________________________________________

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1 , number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller,bigger = order_numbers(100, 99)
print(smaller,bigger)

# Output
# 99 , 100

# __________________________________________________________________________________

def averagee(*numbers):
    sum = 0
    for i in numbers:
        sum=sum + i
    print(sum/len(numbers))

averagee(5,6,9,7,2)
