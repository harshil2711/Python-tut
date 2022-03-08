# -----------------------------------------------------------TYPE CASTING----------------------------------------------------------------

a = 150
b = "250"
print(a+int(b))   #Output: 400

a = 150.90
b = 250
print(int(a+b))   #Output: 400
 
a = "150.90"
b = 250
print(float(a)+b)  #Output: 400.9

a = "150.90"
b = 250
print(int(float(a)+b))  #Output: 400

a = "Hello World, Today is beautiful day"
print(a[1])     #Output: e


a = "Hello World, Today is beautiful day"
print(a[5:11])  #Output: World

# ----------------------------------------------------------VARIABLES---------------------------------------------------------------
# => Variables are the container that stores the value.