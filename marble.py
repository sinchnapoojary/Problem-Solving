'''
You have a jar which initially contains N marbles. You can perform the below 
operations in any order:
1. Taking out A number of marbles from the jar.
2. Taking out B number of marbles from the jar.
Your task is to find and return an integer value, representing the total number of 
unique positive number of marbles that can be left behind by performing these 
operations, including the initial number of marbles.
Note:
You can perform the above operations any number of times and in any order keeping 
in mind that the jor should never become empty.
Input Specification:
A single line containing space seperated integers N,A,B.

Sample Input:
10 3 5
Sample Output:
6
'''

input1,input2,input3=list(map(int,input().split()))
count=set()
for i in range((input1//input2)+1):
    for j in range((input1//input3)+1):
        mcount=input1-input2*i-input3*j
        if mcount>0 :
            count.add(mcount)
print(len(count))
print(count)

        

