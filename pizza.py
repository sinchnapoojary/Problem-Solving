'''
Angela has decided to throw a pizza party. she has ordered N number of pizzas to be 
served to her N number of friends. In this way, she will be serving only one pizza to 
each friend.
She now wants to invite fewer people to her party in order to provide more pizzas per 
person. But at the same time, she wants to ensure that there are at least Y friends at 
her party.
Your task is to help Angela find and return an integer value, representing the sum of 
digits of the minimum number of friends that she can invite to the party, ensuring 
that each person gets an equal number of pizzas.

Sample Input:
100 17
Sample Output:
2
'''

def solve(n,y):
    for i in range(y,n+1):
        if n%i==0:
            return sum(int(x) for x in str(i))
    return -1

print(solve(100,17))

'''
pizza,people=list(map(int,input().split()))
a=pizza//people
print(a)
b=pizza/a
sum=0
while(b!=0):
    t=b%10
    sum=sum+t
    b=b//10
print(sum)


pizza,people=list(map(int,input().split()))
while(pizza%people!=0):
    people+=1
    sum=0
while(people!=0):
    temp=people%10
    sum=sum+temp
    people=people//10
print(sum)


pizza,people=list(map(int,input().split()))
while pizza%people!=0:
    people+=1
sum=0
s=str(people)
for i in s:
    sum+=int(i)
print(sum)
'''