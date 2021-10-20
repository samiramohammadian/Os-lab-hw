x=input("bzn addao: ")
tol=len(x)
adad=int(x)
sum=0
for char in x :
    sum+=int(char)**tol
if sum==adad:
    print("yes")
else:
    print("no")
    
