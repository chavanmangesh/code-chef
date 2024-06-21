T= int(input())
for i in range(T):
    X,Y,A,B = map(int,input().split())
    if(X<Y and (X+A)>Y):
        print("Yes")
    elif(X==Y):
        print("Yes")