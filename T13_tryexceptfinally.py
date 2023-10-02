def divideee(a,b):
    return a/b

try:
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    print(divideee(a,b))

except ZeroDivisionError:
    print("Upps...You can not divide number by zero")

except ValueError as e:
    print("Please enter valid input")

except Exception as e:
    print("Something went wrong")

finally:
    print('okay')

# Output for zero division:
# Enter the first number: 2
# Enter the second number: 0
# Upps...You can not divide number by zero
# okay

# Output for value error:
# Enter the first number: df
# Please enter valid input
# okay


# _________________________________________________________________________

n = input("Enter the number : ")

try:
    for i in range(1,11):
        print(f"{int(n)} X {int(i)} = {int(n*i)}")


except:
    print("invalid input")

# Output
# Enter the number : w
# invalid input

# _________________________________________________________________________

n = int(input("Enter the index number: "))

try:
    a = [4, 6]
    print(a[n])

except IndexError:
    print("Invalid index")

# Output
# Enter the index number: 55
# Invalid index

# _________________________________________________________________________

# Finally keyword
# Finally keyword will use in function mostly. It is use to execute finally block if try and except block returns any value


def func1():
    try:
        n = int(input("Enter the number"))
        l = [23, 45]
        return l[n]

    except:
        return "Error occured"

    finally:
        print("this is finally block")

print(func1())

























