'''
You are given a string containing words separated by spaces. Your task is to write a 
function or program that reverses the order of words in the string.
Sample Input:
Hello World
Sample Output:
World Hello
'''

s=input("Enter String").split()
list.reverse(s)
str1=" "
print(str1.join(s))


