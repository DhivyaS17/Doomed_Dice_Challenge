#Securin - The Doomed Dice Challenge

#Part-A

Dice_A=[1,2,3,4,5,6]
Dice_B=[1,2,3,4,5,6]

#Question1: Total number of Combinations when 2 Dices are rolled together
"""print("The total number of combiations are ",len(Dice_A)*len(Dice_B))
   We can multiply the number of faces to get the total combination.
"""
count=0
for A in Dice_A:
    for B in Dice_B:
        count+=1
print("The number of combinations are",count)

#Question2:All possible combinations
"""pick one face from Dice_A and form pairs with every face in Dice_B
   to get all the possible combinations when the dices are rolled
"""
print("The possible combinations are:\n")
for A in Dice_A:
    for B in Dice_B:
        print(f"(%d,%d)"%(A,B),end=" ")
    print("\n")

#Question3:Probability of all possible Sum
"""we use dictionary which is a key-value pair data structure
   to store the distinct sum of the faces and all the occurances of the sum
   so it will be easier to calculate the sum probability
   probability(sum) = number of occurances/total number of occurances
"""
sumProbability=dict()

for A in Dice_A:
    for B in Dice_B:
        sum=A+B
        pair=[A,B]
        if(sum not in sumProbability):
            sumProbability[sum]=[] 
        sumProbability[sum].append(pair)

print("\nThe Sum and occurances :")
for sum in sumProbability:
    print(f"Sum %d: %s"%(sum,sumProbability[sum]))
print("\nThe Probability Sum :")
for sum in sumProbability:
    print(f"probability(%d):%f"%(sum,(len(sumProbability[sum]))/36))

        

