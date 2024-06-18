'''
*HW1:*Akshay has a number of toys and he decided to donate some of them to an NGO. After 
the donation, he still has some toys left. Write a program to help Akshay to determine 
the number of remaining toys.
Example:
Input: 50 45
Output: The remaining number of toys = 5
Input: 60 6
Output: The remaining number of toys = 54
'''

toys=list(map(int,input("Enter toys, remaining toys").split()))
for i in range(1,len(toys)):
    toys[i]= toys[i-1] -toys[i]
    print(toys[i])