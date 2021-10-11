import time

while(True) :

    print("gozine morede nazar khod ra vared konid : \n ")
    print(" 1.saat system  \U0001F4BB  \n")
    print(" 2.saat morede nazaretan  \U000023F0  \n")
    print(" 3. exit  \U0000274C  \n")
    g=int(input())

    if g==1 :
       
        saat1=time.localtime().tm_hour
        daghighe1=time.localtime().tm_min
        saniye1= time.localtime().tm_sec
        print(" saat :" , saat1 , " daghighe : ", daghighe1 , "saniye : ", saniye1)
    elif g==2 :

        print ("lotfan  saniye ra vared konid  \U000023F0 \n")
        saniye2 =int(input())
        saat2= int(saniye2/3600)
        s=saniye2 % 3600
        daghighe2 = int(s/60)
        saniye=s%60

        print (saat2 ,":", daghighe2 ,":", saniye)

    elif g==3 :
        break  

    else :
        print(" gozine ra eshtebah entekhab kardid. ")
        break
