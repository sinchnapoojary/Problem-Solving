'''
Andrew has a string N consisting of lowercase English letters representing respective grades of N 
students in his class. His grade is at Pth index. He can swap any two adjacent grades.
Your task is to help Andrew find and return a string value, representing maximized grade by 
bringing lexicographically smallest character on the Pth index after doing at most K swaps
Sample Input:
abcdefg
3
2
Sample Output:
a
'''

N=int(input('Total no. of Students'))
input2=input('Grades:')
P= int(input("Andrew's Grade"))
grade= input2[N-1]
if(N-P)>1:
    start=N-P-1
else:
    start=0
if(N+P<=len(input2)):
    end=N+P
else:
    end=len(input2)
print(min(input2[start:end],key=lambda x: ord(x)),P)
