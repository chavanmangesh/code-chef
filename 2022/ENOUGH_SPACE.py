# cook your dish here
T = int(input())
for i in range(T):
    n,x,y = map(int,input().split())
    if(x+(y*2) <=n):
        print("Yes")
    else:
        print("No")