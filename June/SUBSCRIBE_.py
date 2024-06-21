from math import ceil

T = int(input())
for i in range(T):
    X,N = map(int,input().split())
    x=ceil(X/6)
    print(x*N)