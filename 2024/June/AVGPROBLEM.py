T=int(input())
for i in range(T):
    A, B , C =map(int,input().split())
    ab = (A+B)/2
    print({True:"Yes" ,False:"No"}[ab>C])