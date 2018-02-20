# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

def remove_duplicate(list,n):

    for item in list:
        if len(item) <= n:
            list.remove(item)
    return list

print(remove_duplicate(['ines','junior','Bucky','aa'],2))