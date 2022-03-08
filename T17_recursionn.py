# Factorial using iterative method :

def factorial_iterative(n):
    fact=1

    for i in range(1 , n+1):
        fact = fact * i
    print(fact)

factorial_iterative(5)

# Output
# 120

# __________________________________________________________________________________________________
# Factorial using recursive method :

def factorial_recursive(n):

    if n==1:
        return 1

    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(5))

# Output
# 120

# __________________________________________________________________________________________________
# Fibbonacci using iterative method :

def fibb_iterative(n):
    a = 0
    b = 1
    i = 1

    while i<n:
        if i == 1:
            print(0)

        if i == 2:
            print(1)

        else:
            c=a+b
            print(c)
            a,b=b,c
        i = i+1

fibb_iterative(5)

# Output:
# 0
# 1
# 1
# 2
# 3

# __________________________________________________________________________________________________
# Fibbonacci using recursive : 

def fib_recursive(n):

    if n==1:
        return 0

    elif n==2:
        return 1

    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

n = int(input("number: "))
for i in range(1 , n+1):
    print(fib_recursive(i))


# Output
number: 8
0
1
1
2
3
5
8
13