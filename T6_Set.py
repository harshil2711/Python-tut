"""
Set is mutable means changable.
set does not accept repeated value.
Unordered, unindexed, duplicate value not accept, changeable.
        
"""
s = {1,2,3,4,5}
s.add(6)
print(s)

# Output
# {1, 2, 3, 4, 5, 6}
# _________________________________________________________________________________________________
set1 = {1,2,3}
set2 = {4,5,6}
print(set1 + set2)

# Output
# {1, 2, 3, 4, 5, 6}
# _________________________________________________________________________________________________
set1 = {1,2,3}
print(set1.union({10,11}))

# Output
# {1, 2, 3, 10, 11}

# _________________________________________________________________________________________________

set3 = {10 ,11}
set4 = set3.union({15,16})
print(set3 , set4)

# Output
# {10, 11} {16, 10, 11, 15}
# _________________________________________________________________________________________________
set3 = {10 ,11}
set4 = set3.intersection({10,15,16})
print(set4)

# Output
# {10}

# _________________________________________________________________________________________________
set1 = {1,2,3}
set1.remove(2)
print(set1)

# Output
# {1, 3}
# _________________________________________________________________________________________________
s1 = {'Maruti' , 'toyota', 'honda'}
s1.add('kia')         #ek j item add kari sakay
print(s1)

# Output:
# {'honda', 'kia', 'Maruti', 'toyota'}
# _________________________________________________________________________________________________

s1 = {'sandwich' , 'kulfi' , 'panipuri' , 'pizza'}
s1.update({'pasta' , 'burger' ,'sizzler'})         #ek karta vadhare item add kari sakay
print(s1)

# Output
# {'sizzler', 'pasta', 'kulfi', 'sandwich', 'pizza', 'panipuri', 'burger'}
# _________________________________________________________________________________________________
s2 = {'cpu', 'monitor','wifi'}
s2.remove('cpu')
print(s2)

# Output
# {'wifi', 'monitor'}

# _________________________________________________________________________________________________

s1 = {1,2,3}
s2 = {5,6,3}

s3 = s1.symmetric_difference(s2)

print(s3)

# Output
# {1, 2, 5, 6}
# _________________________________________________________________________________________________

s1 = {1,2,3}
s2 = {5,6,3}
s3 = s1.difference(s2)
print(s3)

# Output
# {1, 2}
# _________________________________________________________________________________________________
# Update functon will change the main set also.
s1 = {1,2,3}
s2 = {5,6,3}
s3 = s1.difference_update(s2)
print(s1)

# Output
# {1, 2}
