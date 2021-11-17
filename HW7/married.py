import random
import array 
boys=["ali","reza","vahid","saeed","amir","farhad","farshad","akbar"]
girls=["mina","shiva","roya","tina","donya","mahsa","sheyda","felora"]
b=[0,0,0,0,0,0,0,0]
g=[0,0,0,0,0,0,0,0]
a = array.array('i')
for i in range(8):
    while True:
        y = random.randint(0,7)
        if(b[y]==0):
            b[y]=1
            break
    while True:
        x = random.randint(0,7)
        if(g[x]==0):
            g[x]=1
            break
    print(boys[y]," + ",girls[x])    