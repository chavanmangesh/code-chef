


# Problem

# There is a cricket match going on between two teams A and B.

# Team B is batting second and got a target of X runs. Currently,
# team B has scored Y runs. Determine how many more runs Team B should score to win the match.

# Note: The target score in cricket matches is one more than the number of runs
#  scored by the team that batted first.
#4 Test Cases
# Input       Output
# 4           -
# 200 50      150
# 100 99      1
# 130 97      33
#  53 51      2

#Lets take one integer for loop

T= int(input())

#take for loop for test cases
for x in range(T):
    #take 2 input from user
    A,B = map(int,input().split())
    print(A-B)