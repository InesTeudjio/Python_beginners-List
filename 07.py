#7. Write a Python program to remove duplicates from a list.

def remove_duplicate(list):

    for item in list:
        if list.count(item) > 1:
            list.remove(item)
    return list

print(remove_duplicate([1,3,3,4,4,6,9]))
