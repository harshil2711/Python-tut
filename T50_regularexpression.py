import re

text = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into Sorem electronic typesetting, remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently
with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum Forem.

"""
pattern = r'[A-Z]orem'

match = re.search(pattern , text)  # It stops on first occurances.
print(match)

match = re.finditer(pattern , text)
for mat in match:
    print(mat)