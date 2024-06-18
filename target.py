'''
You are given a list of integers, and your task is to write a function that finds the two 
numbers in the list that add up to a specific target sum. You need to retum the indices 
of these two numbers.
Write a function that takes a list of Integers and a target sum as input and returns a 
list of two indices (0-based) of the numbers that add up to the target sum. Assume 
that there is exactly one solution, and you cannot use the same element twice
Sample Input:
2 7 11 15
9
Sample Output:
[0, 1]
'''

l=list(map(int,input("Enter number").split()))
target=int(input("Enter number"))
new=[]
sum=0
for i in range(0,len(l)):
    for j in range(1,len(l)):
        if l[i]+l[j]==target:
            new=[l.index(l[i]), l.index(l[j])]
# l=(set(new))
print(new)
 