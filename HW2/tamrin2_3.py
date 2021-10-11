import random

list1=[ "front" , "back" ]

c1=0
c2=0
u =0

for i in range(1 , 6) :
    computer1 = random.choice(list1)
    computer2 = random.choice(list1)

    print ("marhale : " , i, "\n ")
    print ("posht dast  \U0001F91A   adad 1 ra vared konid.\n ")
    print ("kaf dast  \U0001F590   adad 2 ra vared konid . \n ")

    user =int (input())

    if user ==1 :
        if computer1 == "back" and computer2 =="front" :
            print("computer1 posht dast  \U0001F91A  you  posht dast  \U0001F91A  computer2  kafe dast \U0001F590  \n ")
            print ("computer 2 win \n ")
            c2+=1

        elif computer1 == "front" and computer2 =="back" :
            print ("computer1 kafe dast  \U0001F590  you  posht dast  \U0001F91A  computer2   posht dast  \U0001F91A  \n ")
            print ("computer 1 win \n ")
            c1+=1

        elif computer1 == "front" and computer2 =="front" :
            print ("computer1 kafe dast  \U0001F590  you  posht dast  \U0001F91A  computer2   kafe dast  \U0001F590  \n ")
            print ("you win \n ")
            u+=1

        elif computer1 == "back" and computer2 =="back" :
            print ("computer1   posht dast  \U0001F91A   you  posht dast  \U0001F91A  computer2   posht dast  \U0001F91A  \n ")
            print ("mosavi \n ")

    
    elif user ==2:
        if computer1 == "back" and computer2 =="front" :
            print("computer1 posht dast  \U0001F91A  you  kafe dast \U0001F590  computer2  kafe dast \U0001F590  \n ")
            print ("computer 1 win \n ")
            c1+=1

        elif computer1 == "front" and computer2 =="back" :
            print ("computer1 kafe dast  \U0001F590  you  kafe dast \U0001F590  computer2   posht dast  \U0001F91A  \n ")
            print ("computer 2 win \n ")
            c2+=1

        elif computer1 == "front" and computer2 =="front" :
            print ("computer1 kafe dast  \U0001F590  you  kafe dast \U0001F590  computer2   kafe dast  \U0001F590  \n ")
            print ("mosavi \n ")

        elif computer1 == "back" and computer2 =="back" :
            print ("computer1   posht dast  \U0001F91A   you  kafe dast \U0001F590  computer2   posht dast  \U0001F91A  \n ")
            print ("you  win \n ")
            u+=1
    else :
        print(" gozine dorost ra entekhab nakardid . mojadad emthn konid .\n")
        break


if u or c1 or c2 >0 :
    print ("dar nahayat \n ")
    if u>c1:
        if u>c2 :
         print ("user win  ")
        elif u<c2 :
         print (" computer 2 win ") 
        elif u==c2 :
         print ("user and computer 2  win")
    elif u<c1 :
        if c1>c2 :
          print (" computer 1 win ")
        elif c1<c2 :
         print ("computer 2 win")
        elif c1==c2 :
          print(" computer 1 and computer 2 win ")
    elif u==c1:
      if c1>c2:
         print ("computer 1 and user win ")
      elif c2>c1 :
             print (" computer 2 win ")
      elif c1==c2 :
           print (" mosavi ")


print ("\n")