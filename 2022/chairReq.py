# cook your dish here
T=int(input())
for item in range(T):
    x,y = map(int,input().split())
    z=x-y
    if(z<0):
        print('0')
    else:
        print(z)
    # TODO: write code...