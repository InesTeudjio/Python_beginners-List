#5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

def count_string(list):
    ctr = 0

    for string in list:
        if len(string) > 1 and string[0] == string [-1]:
            ctr += 1
    return ctr

print(count_string(['abc', 'xyz', 'aba', '1221']))

