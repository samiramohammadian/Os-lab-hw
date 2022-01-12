array = []
n = int(input('Enter number of elements: '))
for i in range(n) :
    print(f"Enter number {i+1} ")
    element = int(input())
    array.append(element) 
y= 0
n=0
for i in range(0 , int(len(array)/2)):
        if array[i] == array[len(array)-(i+1)]:
            y+=1
        elif array[i] != array[len(array)-(i+1)]: 
            n+=1
if n>0 :
    print("NO !!")
elif y>0 :
    print("Yes ")


