'''
Pangram is a sentence containing every letter in the English alphabet. Given a string, 
find all characters that are missing from the string, Le., the characters that can make 
the string a Pangram We need to print output in alphabetic order.
For example,
Input: welcome to geeksforgeeks
Output: abdhijnpquvxyz
'''

i=input("Enter string")
s=i.lower()
a="abcdefghijklmnopqrstuvxyz"
for i in a:
    if s.count(i)==0:
        print(i,end="")