# It is use to raise custom errors. It stops execution where error occurs.

number = int(input("Enter the number between 5 to 9: "))

if number<5 or number>9:
    raise ValueError("Value should be between 5 to 9")

# Output
# Enter the number between 5 to 9: 555
# Traceback (most recent call last):
#   File "D:\Me\Python-tut-main\raisekeyword.py", line 6, in <module>
#     raise ValueError("Value should be between 5 to 9")
# ValueError: Value should be between 5 to 9
