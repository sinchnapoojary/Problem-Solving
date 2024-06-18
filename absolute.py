'''
You are given an array A of size N. In one operation you can select any two elements 
from it, add their absolute difference in your score.
Your task is to find and return an integer value, representing the maximum score.
Note:
Assume 1 based indexing
The elements on which operation has been performed cannot be selected again.
Input Specification:
Input1: An integer value N, representing the size of array A
input2: An integer array A
Output Specification:
Return an integer value, representing the maximum score.
Sample Input:
4
1 2 3 4 
Sample Output: 4
'''

n=list(map(int,input().split()))
sum=0
i=0
j=0
for i in range(0,len(n)//2-1): 
        for j in range(len(n)-1,len(n)//2-1,-1):  
            a=n[j]-n[i]
            sum=sum+abs(a)
            i+=1            
print(sum)

