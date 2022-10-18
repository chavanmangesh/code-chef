# cook your dish here
N = int(input())
for item in range(N):
    a,b,c = map(int,input().split())
#a=1 b=2 c=3
    if(a<b and a>c) or (a<c and a>b):
        print(a)
    elif(b>c and b<a) or (b<c and b>a):
        print(b)
    else:
        print(c)
    