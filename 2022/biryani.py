# According to a recent survey, Biryani is the most ordered food. 
# Chef wants to learn how to make world-class Biryani from a MasterChef. 
# Chef will be required to attend the MasterChef's classes for X weeks, 
# and the cost of classes per week is Y coins.
# What is the total amount of money that Chef will have to pay?

# 4
# 1 10
# 1 15
# 2 10
# 2 15
#Lets take one integer variable


T=int(input())
for i in range(T):
    X,Y = map(int,input().split())
    print(X*Y)