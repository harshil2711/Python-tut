a = 23
b = 55

print(b) if b>a else print("=") if a==b else print(a)

# Output
# 55
# __________________________________________________________________

print(b) if b>a else ""

# Output
# 55
# __________________________________________________________________

c = 9 if a<b else 0
print(c)

# Output
# 9