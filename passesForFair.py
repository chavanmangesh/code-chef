T=int(input())
for i in range(T):
    X,Y = map(int,input().split())
    print({True:"Yes",False:"No"} [X<Y])