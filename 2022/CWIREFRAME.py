n=int(input())
for i in range(n):
    n,m,x=map(int,input().split())
    tlength=0
    cost=0
    if(n>=1 and n<=1000 and m>=1 and m<=1000 and x>=1 and x<=1000):
        tlength  = n * 2 + m * 2
        cost = x * tlength
        print(cost)