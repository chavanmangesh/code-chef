# Problem

# Chef is buying sweet things to prepare for Halloween!
# The shop sells both chocolate and candy.
# * Each bar of chocolate has a tastiness of X.
# * Each piece of candy has a tastiness of Y.
# One packet of chocolate contains 2 bars, while one packet of candy contains 5 pieces.
# Chef can only buy one packet of something sweet, and so has to make a decision: 
# which one should he buy in order to maximize the total tastiness of his purchase?
# Print Chocolate if the packet of chocolate is tastier, 
# Candy if the packet of candy is tastier, and Either if they have the same tastiness.

T= int(input())
for i in range(T):
    x,y= map(int,input().split())
    a=x*2
    b=y*5
    if(a>b):
        print("Chocolate")
    elif(a<b):
        print("Candy")
    else:
        print("Either")