str1 = "PyNaTive"
lower=""
upper=""
for char in str1:
    if char.islower():
        lower+=char
    else:
        upper+=char
new_str=lower+upper
print(new_str)