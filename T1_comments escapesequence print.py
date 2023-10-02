# ----------------------------------------------------------------COMMENTS---------------------------------------------------------------------------

# Hello ,Good afternoon!!!        <== This is single line comment.

"""

Hello , Welcome
Welcome to my Python tuturial
Here I am making python tuturial for begginers and notes as well.               <== This is multiline comment.
Thanks......

"""
# --------------------------------------------------------ESCAPE SEQUENCES---------------------------------------------------------------------------

# 1. Use of end="".
#  => This is used for write info in existing sentence.Used for write in one sentense also
#  => You can give anything inside the " ".Like , : etc.
#  => Specify what to print at the end.

print('hello world.', end=" ")
print('Now making python tutorial.')

# Output:
# hello world. Now making python tutorial.
# _____________________________________________________________________________________________

# 2. Use of \"
    # => To print world in quotes.

print('\'hello\'')
# Output:
# 'hello'
# _____________________________________________________________________________________________

# 3. Use of \\
    # => To print \.

print('hello\\')

# Output:
# hello\
# _____________________________________________________________________________________________

# 4. Use of \n
    # => To print word in new line.

print('hello \nworld')

# Output:
# hello
# world
# _____________________________________________________________________________________________

# 5. Use of \t
    # => To print tab in line.

print('hello \tworld')

# Output:
# hello   world
# _____________________________________________________________________________________________

# Use of sep=

print('hello' , 5 ,6 , sep='!')

# Output
# hello!5!6

# _____________________________________________________________________________________________

# To print multiline string

line = """orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
It was popularised in the 1960s with 
the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing 
software like Aldus PageMaker includin

"""
print(line)