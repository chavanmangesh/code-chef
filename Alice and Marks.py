# cook your dish here
# X,Y=map(int,input().split())

# if(X>=2*Y):
#     print('YES')
# else:
#     print('NO')


# cook your dish here
# T=int(input())
# array=[]
# for i in range(T):
#     N =int(input())
#     for j in range(N):
#         array.append(int(input()))

# print(array)

# cook your dish here
T=int(input())
for item in range(T):
    A,B,X =map(int,input().split())
    a=int(A+X)
    b=int(B-X)
    print(A+X)
    if((A==A+X and B== B-X) or (A==A-X and B==B+X)):
        print('YES')
    else:
        print('NO')