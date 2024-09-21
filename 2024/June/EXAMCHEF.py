# cook your dish here
T = int(input())
for item in range(T):
    X, Y, Z = map(int, input().split())
    m = X*Y
    p = (Z/m)*100
    print({True:"Yes",False:"No"}[p  > 50])