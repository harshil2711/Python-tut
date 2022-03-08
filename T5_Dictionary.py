"""
Dictionary is mutable means it can be changed.
Ordered, indexed(key), duplicate accept , changable
    
"""
a = {'name': 'Mukesh' , "Age": 22, "city": "ABD"}
a['food'] = "Manchurian"        #It can be updated. To add a new item in dectionary.
print(a)

# Output: 
# {'name': 'Mukesh', 'Age': 22, 'city': 'ABD', 'food': 'Manchurian'}

#___________________________________________________________________________________
a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
a["fname"]='mukesh'  #It can be updated. use list sign to update dicitonary

# Output:
# {'fname': 'mukesh', 'lname': 'Rajput', 'fname1': 'karan'}

#___________________________________________________________________________________

a = {'name': 'Mukesh' , "Age": 22, "city": "ABD"}
a.update({'color':'Blue'})
print(a)

# Output
# {'name': 'Mukesh', 'Age': 22, 'city': 'ABD', 'color': 'Blue'}

#___________________________________________________________________________________
a = {"fname": "pradip", "lname": "Rajput", "fname1": "karan"}
a.update({'fname':'My'})
print(a)

# Output
# {'fname': 'My', 'lname': 'Rajput', 'fname1': 'karan'}
#___________________________________________________________________________________

a = {'name': 'Mukesh', 'Age': 22, 'city': 'ABD', 'food': 'Manchurian'}
del a['food']
print(a)

# Output: 
# {'name': 'Mukesh', 'Age': 22, 'city': 'ABD'}

#___________________________________________________________________________________
a = {'name': 'Mukesh', 'Age': 22, 'city': 'ABD', 'food': 'Manchurian'}
b = a.copy()
print(a)
del b['name']
print(b)

# Output
# {'name': 'Mukesh', 'Age': 22, 'city': 'ABD', 'food': 'Manchurian'}
# {'Age': 22, 'city': 'ABD', 'food': 'Manchurian'}

#___________________________________________________________________________________
a = {'name': 'Mukesh', 'Age': 22, 'city': 'ABD', 'color': 'Blue'}
print(a.keys())

# Output
# dict_keys(['name', 'Age', 'city', 'color'])

#___________________________________________________________________________________
a = {'name': 'Mukesh', 'Age': 22, 'city': 'ABD', 'color': 'Blue'}
print(a.values())

# Output
# dict_values(['Mukesh', 22, 'ABD', 'Blue'])

#___________________________________________________________________________________
a = {'name': 'Mukesh', 'Age': 22, 'city': 'ABD', 'color': 'Blue'}
print(a.items())

# Output
# dict_items([('name', 'Mukesh'), ('Age', 22), ('city', 'ABD'), ('color', 'Blue')])
#___________________________________________________________________________________
a = {"fname": "mukesh", "lname": "patel", "fname1": "karan"}
if "pradip" in a.values():
    print("My value is available")
else:
    print("My value is not available")

# Output
# My value is available

#___________________________________________________________________________________
a = {'fname': 'Mukesh' , 'lname':'patel','age':'50'}
a.pop('fname')   #To remove particular item
print(a)

# Output
# {'lname': 'patel', 'age': '50'}
#___________________________________________________________________________________
a = {'fname': 'Mukesh' , 'lname':'patel','age':'50'}
a.popitem()  #To remove last item.
print(a)

# Output:
# a = {'fname': 'Mukesh' , 'lname':'patel'}

#___________________________________________________________________________________


a = {'name': 'Mukesh' , "Age": 22, "city": "ABD"}

for i,j in a.items():
    print(i,j)

# Output:
# name Mukesh
# Age 22
# city ABD
