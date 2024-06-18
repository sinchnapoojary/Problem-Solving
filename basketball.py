'''
You are competing in a basketball contest. In this contest the score for each 
successful shot depends on both the distance from the basket and the player's position.
The ball is shot N times, successfully. You are given an array A containing the 
distance of a player from basket for N shots. The index of array represents the position 
of the player. Score is calculated by multiplying the position with the 
distance from the basket.
Your task is to find and return an integer value, representing the maximum possible 
score you can achieve by choosing a contiguous subarray of size K from the given 
array.
Given: 
K=3
A=[4,3,2,7,1,9]
'''

def basketball(distance,pos):
    ndistance=len(distance)
    if(ndistance<pos):
        print('not possible')

    score=[]
    for i in range(ndistance):
        score.append(distance[i]*i)

    current_dis= sum (score[:pos])
    max_dis=current_dis

    for i in range(1,ndistance-pos+1):
        current_dis= current_dis-score[i-1]+score[i+pos-1]
        max_dis=max(max_dis,current_dis)
    return max_dis

array=[4,3,2,7,1,9]
pos=3
print(basketball(array,pos))
