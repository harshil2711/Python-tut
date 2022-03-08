"""
'r' = To read the file
'w' = To write into file
'x' = create file if not exist
'a' = add more content into file
'b' = binary mode
'+' = read and write in the file
't' = text mode


"""
# To read the file 
f = open('textfile.txt','r')
content = f.read()
print(content)

# Output
# Hello world 
# Today is saturday
# Tommorrow is sunday

# ____________________________________________________________________________________________________
f = open('textfile.txt','r')
content = f.read(3)   #if you give value in read , it will read three characters of the first line
print(content)

# Output 
# Hel
# ____________________________________________________________________________________________________
f = open('textfile.txt','r')
content = f.read(3000)   #if you give value greater than total characters then it will return whole text
print(content)

# Output 
# Hello world
# Today is saturday
# Tommorrow is sunday
# ____________________________________________________________________________________________________
f = open('textfile.txt','r')

for line in f:
    print(line)

#Output
# Hello world

# Today is saturday

# Tommorrow is sunday
# ____________________________________________________________________________________________________
f = open('textfile.txt','r')
print(f.readline())  #To read one line of file 

# Output
# Hello world 
# ____________________________________________________________________________________________________
f = open('textfile.txt','r')
print(f.readline(4))  #To read 4 charachters of line 

# Output
# Hell
# ____________________________________________________________________________________________________
f = open('textfile.txt','r')
print(f.readlines())  #To store lines in a list

# Output
# ['Hello world \n', 'Today is saturday\n', 'Tommorrow is sunday']
# ____________________________________________________________________________________________________
f = open('textfile3.txt','w') #Write function will remove everything from the file and write the new content 
f.write('Today is sunday')    #If the given file is not exist , then it will create new one.

# Output:
# Today is sunday
# ____________________________________________________________________________________________________
f = open('textfile2.txt','a')   #append is used to add content in file.
for i in range(5):
    f.write(f'hello world {i} \n')  

# output : 
# hello world 0 
# hello world 1 
# hello world 2 
# hello world 3 
# hello world 4 
# ____________________________________________________________________________________________________
f =  open('textfile4.txt','w')
print(f.write('Hello world')) #If you print write function,it will show character count that is written in file.

# Output:
# 11
# ____________________________________________________________________________________________________
f = open('textfile4.txt', 'r+')
print(f.read())   #It will read the file first 
f.write('hello INDIA \n')  #and then write the content in it.

# Output:
# Hello world