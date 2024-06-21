#Fill In The blanks 
#Input : array1 = [1,None,2,3,None,None,5,None,6,7,None,8,9,None,None]
array1 = [1,None,2,3,None,None,5,None,6,7,None,8,9,None,None]

res=[]
valid=0
for i in array1:
    if i is not None:
        res.append(i)
        valid=i
    else:
        res.append(valid)

print(res)