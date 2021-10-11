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
        s1=(saat1*3600)+(daghighe1*60)+saniye1
        print(s1)

    elif g==2 :

        print ("lotfan saat ra vared konid  \U000023F0 \n")
        t=input()
        ti=t.split(":")
        saat2=int(ti[0])
        daghighe2=int(ti[1])
        saniye2=int(ti[2])
        s2=(saat2*3600)+(daghighe2*60)+saniye2
        print(s2)

            
    elif g==3 :
        break  

    else :
        print(" gozine ra eshtebah entekhab kardid. ")
        break
