T=int(input())
for i in range(T):
    A,B,C = map(int,input().split())
    if(A>B and A>C):
        print("Alice")
    elif(B>A and B>C):
        print("Bob")
    else:
        print("Charlie")