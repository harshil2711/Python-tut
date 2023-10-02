punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

listpunc = list(punctuations)

# print(listpunc)

text = "hello mys name is . ? / ///////////////////////  "

# for i in listpunc:
#     if i in text:
#         text.replace(i,'')
#
#         print(text)

analyzed = ''
for i in text:
    if i not in punctuations:
        analyzed = analyzed + i
print(analyzed)



try: print(1)
except: print(2)
finally: print(3)