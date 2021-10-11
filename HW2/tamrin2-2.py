import random


list1=[ "sang" , "kaghaz" , "gheychi"]

c=0
u=0

for i in range(1,6) :
    Computer= random.choice(list1)

    print("marhale" ,i ,"\n ")
    print("sang \U0000270A  1 ra vare1d konid  \n")
    print("kaghaz \U0001F590  2 ra vared konid  \n")
    print("gheychi \U0000270C  3 ra vared konid  \n")
    
    user =int(input())

    if user == 1:
        if Computer == "sang" :
            print ("computer  sang \U0000270A  you   sang \U0000270A   barabar  \n")
        
        elif Computer == "kaghaz" :
            print ("Computer kaghaz \U0001F590  you sang \U0000270A    computer  win  \n")
            c+=1
        
        elif Computer == "gheychi" :
            print ("Computer  gheychi \U0000270C  you  sang  \U0000270A     you win  \n")
            u+=1

    elif user == 2:
        if Computer == "sang":
            print ("computer sang \U0000270A  you kaghaz \U0001F590     you win \n")
            u+=1

        elif Computer == "kaghaz":
            print ("Computer kaghaz \U0001F590  you kaghaz  \U0001F590    barabar \n")

        elif Computer == "gheychi" :
            print ("Computer  gheychi \U0000270C  you  kaghaz \U0001F590    computer win  \n")
            c+=1

    elif user == 3 :
        if Computer == "sang":
            print ("computer sang  \U0000270A  you gheychi \U0000270C   computer win \n")
            c+=1
        
        elif Computer == "kaghaz" :
            print ("Computer  kaghaz \U0001F590  you  gheychi  \U0000270C   you win  \n")
            u+=1
        
        elif Computer == "gheychi" :
            print ("Computer gheychi  \U0000270C  you  gheychi  \U0000270C   barbar \n")
    else :
        print(" gozine dorost ra entekhab nakardid . mojadad emthn konid .\n")
        break


if u or c >0 :
    print (" dar nahayat \n ")
    if u>c :
        print ("user win ")
    elif c>u :
     print (" computer win ")
    elif c==u :
      print ("mosavi shdid ")

print ("\n")
