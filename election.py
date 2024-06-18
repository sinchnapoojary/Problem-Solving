'''
You are the head of the election committee in your village. Each Political party is 
associated with a unique number and the votes are represented as an integer array A. 
where each element contains the party number voted for by the villagers. For a party 
to win, they must have a majority of votes. our task is to find and return an integer 
value denoting the winning party's number. Return -1 if there is no party with a 
majority.
Note: If only one vote is there he is the winner.
Input Format :
input1: An integer value representing the number of voters
input2: An integer array A representing the votes of the voters.
output Format:
Return an integer value denoting the winning party's number.Return -1 there is no 
party with a majority
Example 1:
Input:
6
1 1 2 2 2 3
Output: 2
'''

voters=int(input("Enter number of voter"))
vote=list(map(int,input("Enter vote").split()))
win={}
if voters==1:
    print(vote[0])
else:
    for i in vote:
        if i in win:
            win[i]=win[i]+1
        else:
            win[i]=1
    vals=list(win.items())
    ans=-1
    vals.sort(reverse=True,key=lambda s:s[1])
    if len(vals)==1:
        ans=vals[0][0]
    else:
        if vals[0][1]==vals[1][1]:
            ans=-1
        else:
            ans= vals[0][0]
print(ans)

''' 2nd approach
from collections import Counter
voters=int(input("Enter number of voter"))
vote=list(map(int,input("Enter vote").split()))
frequency=Counter(vote)
max_freq=max(frequency.values())
for i in frequency:
    if(frequency[i]==max_freq):
        print(i)
'''






