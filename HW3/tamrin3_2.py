import random

print("n: \n")
n=int(input())
arry=[]
for i in range(n):
    x = random.randint(1,100)
    if x not in arry :
        arry.append(x)
    else :
        i-=1

print (arry)



   


