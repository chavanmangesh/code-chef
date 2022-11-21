# cook your dish here
T= int(input())
for item in range(T):
    N=int(input())
    print({True:"Yes",False:"No"} [N%2==0])