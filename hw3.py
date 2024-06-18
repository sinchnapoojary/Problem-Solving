'''
HW3: Print the given pattern
You are given a number N and you have to print the given pattern:
For N=3
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1
'''

n=3
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(f"{j} " * i,end='')
    print()

'''  2nd appraoch
def print_pattern(N):
    for i in range(N, 0, -1):
        for j in range(N, 0, -1):
            print(f"{j} " * i, end='')
        print()

# Example usage
N = 3
print_pattern(N)
'''

'''  3rd approach
n=3
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(i,end=" ")
print()
for i in range(n,0,-1):
    for j in range(1,n):
        print(i,end=" ")
print()
for i in range(n,0,-1):
    for j in range(1,n-1):
        print(i,end=" ")
        
'''