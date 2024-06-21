X=int(input())
A,B= map(int,input().split())
print({True:"Yes",False:"No"}[X>=(A+B)])