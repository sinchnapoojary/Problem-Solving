'''
You have been given the task of making the content on a social media platform more 
user-friendly. Your task is to find and return an integer value representing the count 
of the number of spaces in a given string S.

Input:
A string S
Output :
Return an integer value representing the count of the number of spaces in a given 
string S.
Example:
Input:
Hello World Hey
Output:
2
'''

a="Hello World Hey"
space=a.split(" ")
a=len(space)-1
print (a)