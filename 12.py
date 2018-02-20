#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

def remove_element(list):

    if len(list) > 4:
        return list[1:4] + list[6:]
print(remove_element([1,2,3,4,5,6,7,7,8]))