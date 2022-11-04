T= int(input())
for i in range(T):
    x= int(input())
    if(x<=100):
        print(x)
    elif(x>100 and x<=1000):
        print(x-25)
    elif(x>1000 and x<=5000):
        print(x-100)
    elif(x>5000):
        print(x-500)