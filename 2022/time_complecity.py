# cook your dish here
T= int(input())
for item in range(T):
    A,B = map(int,input().split())
    print({True:"Yes",False:"No"}[A>B])
    # TODO: write code...