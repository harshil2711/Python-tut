"""
List is mutable(can be change or update) type of datatype.
List can contain items with different data types.
List accepts duplicate values.
Remove : index , value
Pop : index
Insert : Index value together , old list as it is
"""


a = 'python'
print(list(a))

#Output
# ['p', 'y', 't', 'h', 'o', 'n']

#___________________________________________________________________________________

list1 = [1 , 2 ,3 , 4 ,5]
list1[1] = 10  # list can be changable.
print(list1)
 
# Output
# [1, 10, 3, 4, 5]

#___________________________________________________________________________________

list1 = [1 , 2 ,3 , 4 ,5 , 1 ,2 ,1 , 1]
print(list1.count(1))

# Output
# 4

#___________________________________________________________________________________

list2 = [1 ,2 ,3 ,4 ,5 ,6]
list2.append(7)   # append add the value at the end of the list and only takes value as input.
print(list2)

# Output
# [1, 2, 3, 4, 5, 6, 7]

#___________________________________________________________________________________

list3 = [11 ,22 , 33 ,44]
list3.insert(1 ,55)    #Insert take index and value as argument.
print(list3)

# Output
# [11, 55, 22, 33, 44]

#___________________________________________________________________________________

list1 = [1 , 2 ,3 , 4 ,5]
list2 = ['apple' , 'orange' , 'pine']

list1.extend(list2)  #To concatenate to list.

print(list1)

# Output
# [1, 2, 3, 4, 5, 'apple', 'orange', 'pine']
#___________________________________________________________________________________

A=[1,59,36,966,96,66,45]
B = ["maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti"]

c=A+B

print(c)

# Output
# [1, 59, 36, 966, 96, 66, 45, 'maruti', 'Mahindra', 'Audi', 'Mercy', 'BMW', 'maruti']



#___________________________________________________________________________________

list4 = ['apple' , 'orange' ,'grapes' , 'banana']
list4.remove(list4[0])  #Remove function takes index number as input.
print(list4)

# Output
# ['orange', 'grapes', 'banana']

#_________________________________________________________________________________

list4 = ['apple' , 'orange' ,'grapes' , 'banana']
list4.remove('apple')  # Remove function also take value as input.
print(list4)

# Output
# ['orange', 'grapes', 'banana']

#___________________________________________________________________________________

list5 = ['audi' , 'maruti' , 'kia' , 'suzuki']
list5.pop(1)  #pop only take index number as input to remove that particular value. 
              #If you dont give value in pop function it will rmove last element of list.
print(list5) 

# Output
# ['audi', 'kia', 'suzuki']

#___________________________________________________________________________________

list6 = ['men' , 'women' , 'kids']
del list6   # For delete the list 6.

#___________________________________________________________________________________

list7 = ['men' , 'women' , 'kids']
list7.clear()   # For clear the itmes in list.
print(list7)

# Output
# []

#___________________________________________________________________________________

list8 = ['shirt' , 't-shirt' , 'jeans' , 'shorts']
list9 = list8.copy()  # To copy one list in to another.
print(list9)

# Output
# ['shirt', 't-shirt', 'jeans', 'shorts']

#___________________________________________________________________________________

list11= ["maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti"]
print(list11)  #List accepts duplicate values.

# Output
# ['maruti', 'Mahindra', 'Audi', 'Mercy', 'BMW', 'maruti']

#___________________________________________________________________________________

a = ["maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti"]
for x in a:
    print(x)

# Output
# maruti
# Mahindra
# Audi
# Mercy
# BMW
# maruti

#___________________________________________________________________________________

a = ["maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti"]
if "maruti" in a:
    print("Value is available")
else:
    print("value not available")

# Output
# Value is available

#___________________________________________________________________________________

a = ["maruti", "Mahindra", "Audi", "Mercy", "BMW", "maruti"]
print(len(a))

# Output
# 6

#___________________________________________________________________________________

a=[["har",6],["hari",2],["devs",8],["kinjal",7]]
for i,j in a:
    print(i,j)

# Output
# har 6
# hari 2
# devs 8
# kinjal 7

#___________________________________________________________________________________

a=[1,59,36,966,96,66,45]
a.sort()   # Make all numbers and strings in ascendig order.
print("second largest number is :",a[-2])  

#Output
#second largest number is : 96

#___________________________________________________________________________________

a=[1,59,36,966,96,66,45]
a.sort(reverse=True)  # You can use reverse attribute in sort function.
print(a)

#Output
# [966, 96, 66, 59, 45, 36, 1]

#___________________________________________________________________________________

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subject_marks.sort()  # This will sort list according to first letter of item in sublist.
print(subject_marks)

#Output
# [('English', 88), ('Maths', 97), ('Science', 90), ('Social sciences', 82)]

#___________________________________________________________________________________

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subject_marks.sort(key=lambda x:x[1])   # Use key = function to sort second element in sublist.
print(subject_marks)  

# Output
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

#___________________________________________________________________________________

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
b=sorted(subject_marks,key=lambda x:x[1])  #Sorted function make another list for sort list.
print(b)

# Outputs
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

#___________________________________________________________________________________
 
models = [{'make':'Nokia', 'model':216, 'color':'Red'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
b=sorted(models,key=lambda x:x["color"])  # sort list based on color key.
print(b)

# Output
# [{'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Nokia', 'model': 216, 'color': 'Red'}]

#___________________________________________________________________________________

models = [{'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Nokia', 'model': 216, 'color': 'Red'}]
models.sort(key= lambda x:x['color'])
print(models)

# Output
# [{'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Nokia', 'model': 216, 'color': 'Red'}]

#___________________________________________________________________________________

# SLICING IN LIST

a=[1,2,3,4,5,6,7,8,6,9]    
print(a[:])     # [1, 2, 3, 4, 5, 6, 7, 8, 6, 9]    
print(a[1:])        # [2, 3, 4, 5, 6, 7, 8, 6, 9]       
print(a[:5])        #  [1, 2, 3, 4, 5]      
print(a[2:5])       #   [3, 4, 5]    
print(a[0::4])      #   [1, 5, 6]   
print(a[1::3])      #  [2, 5, 8]    
print(a[2::2])      #   [3, 5, 7, 6]   

#___________________________________________________________________________________

a=[1,2,3,4,5,6,7,8,6,9]    
print(max(a)) #9
print(min(a)) #1

#___________________________________________________________________________________
a = ["maruti", "Mahindra", "Audi", "Mercy", "BMW"]

for i,j in enumerate(a):
    print(i,j)

# Output
# 0 maruti
# 1 Mahindra
# 2 Audi
# 3 Mercy
# 4 BMW
#___________________________________________________________________________________
a = [3 ,4 ,5 ,6 ,7]

for i,j in enumerate(a , start=1):
    print(i , j)

# Output
# 1 3
# 2 4
# 3 5
# 4 6
# 5 7