'''
You are given an array A of N integers. The array A can be divided into two parts: the 
first part consists of the first 'i' elements of A (where ranges from 1 to N), and the 
second part consists of the last (N-i) elements of A
Your task is to find and return a new array named result of the same size as A, where 
each element of result[i] represents the absolute difference between the sum of the 
elements in the first part of A and the sum of the elements in the second part of A
Note: For i= N,N-i=0.So, consider the sum of last N-i integers as 0 in this case
Input Specifications:
input1: An integer value representing the size of the array A.
input2: An integer array A.
Output Specification:

Return a new integer array named result of the same size as A, where each element of 
result[i) represents the absolute difference between the sum of the elements in the 
first part A and the sum of the elements in the second part of A
Sample Input:
5
1 2 3 4 5
Sample Output:
[13, 9, 3, 5, 15]
'''

n=int(input())
array=list(map(int,input().split()))
total=sum(array) #15
a=[]
first=0
for i in range(0,n):    
    first+=array[i]   
    print(first,end=" ")  
    second=total-first  #15-1, 15-3, 15-6, 15-10, 15-15
    print(second,end=" ")
    a.append(abs(first-second))  
print(a)
    

        


