'''
Given two numbers a and b. Find the GCD and LCM of and d.
Input:
* Two positive integers a and b (1 <=a, b <=1000)
Output:
For GCD function, an integer representing the GCD of a 'and b
For LCM function, an integer representing the LCM of a and b
Sample Input:
12 18
Output:
6
36
'''

a=int(input("Enter a"))
b=int(input("Enter b"))
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

GCD= gcd(a,b)
LCM= lcm(a,b)
print(GCD,LCM)

''' Using built-in function
import math
a=int(input("Enter a"))
b=int(input("Enter b"))
gcd=math.gcd(a,b)
print(gcd)
lcm=math.lcm(a,b)
print(lcm)
'''


