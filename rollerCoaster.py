# cook your dish here
T= int(input())

for x in range(T):
    X,H = map(int,input().split())
    if(H<=X):
        print('YES')
    else:
        print('No')
    # TODO: write code...