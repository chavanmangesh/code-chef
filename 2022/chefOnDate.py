# cook your dish here
T = int(input())
for item in range(T):
    X,Y = map(int,input().split())
    if(Y<=X):
        print('YES')
    else:
        print('NO')
    # TODO: write code...