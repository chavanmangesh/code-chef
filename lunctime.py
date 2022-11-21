T= int(input())
for i in range(T):
    N= int(input())
    print({True:"Yes",False:"No"}[N<=4 and N>=1])