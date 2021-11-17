import random
import array
boys = ["ali", "reza", "yasin", "benyamin", "mehrdad", "sajjad", "aidin", "shahin"]
girls = ["sara", "zari", "neda", "homa" ,"eli", "goli","mary", "mina"]

a=[]

k=True
while True:
    if k==True:
        married_b=random.choice(boys)
        married_g=random.choice(girls)
        b=[married_g , married_b]
        
        for i in range(8): 
            if b != a:
                print(married_g , "with" , married_b)
                a.append(b)
                break
            
    print("edaME MIDI? ")
    c=input("edame midi (yes/no")
    if c == "yes":
        k=True
    else :
        k=False
        break