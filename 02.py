#2. Write a Python program to multiplies all the items in a list.

def mult_items(list):
    mult = 1
    for x in list:
        mult *= x
    return mult
print(mult_items([1,3,6]))