#14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

def remove_even(list):
    for item in list:
        if item % 2 == 0:
            list.remove(item)
    return list

print(remove_even([1,2,3,4,5,6,7]))