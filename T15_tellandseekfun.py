# Tell() Function tells you the current position of the pointer. 

f = open('textfile.txt','r')
print(f.tell())
print(f.readline())
print(f.tell())

# Output
# 0
# Hello world guys python
# 25

# _____________________________________________________________________________________________
# Seek(argument) Function is used to set a pointer at a particular location
f = open('textfile.txt','r')
print(f.tell())
print(f.readline())
f.seek(7)
print(f.tell())

print(f.readline())


# Output
# 0
# Hello world guys python

# 7
# orld guys python

# _____________________________________________________________________________________________
# Truncate function is used to write a file with a particular character
f = open("file1.txt",'w')

f.write('Hello world.')
f.truncate(3)

# Output
# Hel