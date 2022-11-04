from math import floor


T= int(input())
for i in range(T):
    x,y = map(int,input().split())
    print(floor((x*y)/100))
   # print(round((x*y)/100))