# cook your dish here
T=int(input())
for item in range(T):
    a,b,c= map(int,input().split())
    if(((a+b)%2!=0) or ((a+c)%2!=0) or ((b+c)%2!=0)):
        print("Yes")
    else:
        print("No")
    # TODO: write code...