# cook your dish here
T=int(input())
for n in range(T):
    a,b = map(int,input().split())
    if((a+b)%2==0):
       print("Yes")
    else:
       print("No")