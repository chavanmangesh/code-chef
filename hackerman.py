def checkprime(num):
    if num > 1: 
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
       return False 

T=int(input())
for i in range(T):
    X,Y =map(int,input().split())
    P=checkprime(X+Y)
    print({True:"Alice",False:"Bob"}[P])