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