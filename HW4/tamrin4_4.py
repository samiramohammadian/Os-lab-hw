n=int(input("n:"))

k=0
j=1
sum=0
for i in range(n-1):
    sum=k+j
    k=j
    j=sum
    if sum==1 :
        print(sum)

    print(sum)



