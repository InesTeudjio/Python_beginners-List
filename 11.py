#11. Write a Python function that takes two lists and returns True if they have at least one common member.

list1 = ['a','b','c']
list2 = ['a','d','y']

for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            print('True')