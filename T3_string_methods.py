a = "                         Hello World, Today is beautiful day                          "
print(a.strip())    #It won't print extra space   

#Output: Hello World, Today is beautiful day

# ______________________________________________________________________________________________________________________
a = "Hello World, Today is beautiful day"
print(len(a))   #Gives length of variable a.

# Output: 35

# ______________________________________________________________________________________________________________________

a = "Hello World, Today is beautiful day"
print(a.upper())  #Convert text into uppercase.

# Output: HELLO WORLD, TODAY IS BEAUTIFUL DAY

# ______________________________________________________________________________________________________________________

a = "Hello World, Today is beautiful day"
print(a.lower())   #Convert text into lowercase.

# Output: hello world, today is beautiful day

# ______________________________________________________________________________________________________________________

a = "Hello World, Today is beautiful day"
print(a.replace("is", "are"))  #Replace word with another.

# Output: Hello World, Today are beautiful day

# ______________________________________________________________________________________________________________________

a = "Hello World, Today is beautiful day"
print(a.split(' '))   #Split sentence with given value.Here value is space. And return value in list.

# Output: ['Hello', 'World,', 'Today', 'is', 'beautiful', 'day']

# ______________________________________________________________________________________________________________________

a = "Hello World, Today is beautiful day"
print(a.split('i'))  #Here value is i.

# Output: ['Hello World, Today ', 's beaut', 'ful day']
#  ______________________________________________________________________________________________________________________

a = "Python"
print(a[::-1])  #Print value reverse.

# Output: nohtyP
#  ______________________________________________________________________________________________________________________

a = 'Python is easy language'
print(a[0:6:2])

# Output: Pto

a = 'Python is easy language'
print(a[0:6:2])

# Output: Pto

#  ______________________________________________________________________________________________________________________

a = 'Python is easy language'
print(a.isalnum())   #Returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) OR numbers (0-9).Return boolean values.
                     #space is not alnum.

# Output: False

#  ______________________________________________________________________________________________________________________

a = 'Python is easy language'
print(a.isalpha())   #Returns True if all the characters are alphabet letters (a-z).
                     #space is not alpha.

# Output: False

#  ______________________________________________________________________________________________________________________

a = 'Python is easy language'
print(a.endswith('easy'))

# Output: False

#  ______________________________________________________________________________________________________________________
 
a = 'Python is easy language'
print(a.count('e'))  #Counts alphabate in given string.
 
# output: 2

#  ______________________________________________________________________________________________________________________

a = 'vscode editor'
print(a.capitalize())  #Make first letter of sentence capital and make all other letter small.

#Output: Vscode editor

#  ______________________________________________________________________________________________________________________

a = 'Python is easy language'
print(a.find('is')) #Gives index number of word.

# Output: 7

#___________________________________________________________________________________

a = ['p', 'y', 't', 'h', 'o', 'n']
b = ''.join(a) #It is only apply on string.It joins the strings.
print(b)

# Output
# python
#___________________________________________________________________________________

myTuple = ("John", "Peter", "Vicky")
x = ",".join(myTuple)
print(x)

# Output
# John,Peter,Vicky
#___________________________________________________________________________________

a = "typing|||||||||||||||||||"

print(a.strip("|"))

#___________________________________________________________________________________
a = "typing !! vs code $$"
print(a.split("!"))

#___________________________________________________________________________________

str1 = "Welcome to the console !!"
print(str1.endswith("to", 4 , 10))

# Output
# True

#___________________________________________________________________________________

# To change string from capital to small and small to capital
str1 = "Python is interpreted language"
print(str1.swapcase())

# Output
# pYTHON IS INTERPRETED LANGUAGE

#___________________________________________________________________________________

str1 = "Python is interpreted language"
print(str1.title())