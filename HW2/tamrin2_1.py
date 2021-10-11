import math

while(True) :
    print(" gozine morede nzr ra entekhab konid:  \n")
    print (" 1. jam     \n")
    print (" 2. tafrigh \n")
    print (" 3. zarb    \n")
    print (" 4. taghsim \n")
    print (" 5. sin     \n")
    print (" 6. cos     \n")
    print (" 7. tan     \n")
    print (" 8. cot     \n")    
    print (" 9. log     \n")
    print ("10. exit    \n")
    
    x=int(input())
    if x==1 :
        print (" adad aval va dovom ra vared konid :  \n")
        a1=int(input())
        b1=int(input())
        s1=a1+b1
        print (a1 ,"+", b1 , "= ", s1)

    elif x==2 : 
        print (" adad aval va dovom ra vared konid :  \n")
        a1=int(input())
        b1=int(input())
        s1=a1-b1
        print (a1 ,"-", b1 , "= ", s1)

    elif x==3 : 
        print (" adad aval va dovom ra vared konid :  \n")
        a1=int(input())
        b1=int(input())
        s1=a1*b1
        print (a1 ,"*", b1 , "= ", s1)

    elif x==4 :
        print (" adad aval va dovom ra vared konid :  \n")
        a1=int(input())
        b1=int(input())
        s1=a1/b1
        print (a1 ,"/", b1 , "= ", s1)

    elif x==5 :
        print (" zaviye morede nazar khod ra vared konid :   \n")
        a=int(input())
        a=a*math.pi/180
        s=math.sin(a)
        print (" sin ", a , "=" , s)

    elif x==6 :
        print (" zaviye morede nazar khod ra vared konid :   \n")
        a=int(input())
        a=a*math.pi/180
        s=math.cos(a)
        print (" cos ", a , "=" , s)

    elif x==7 :
        print (" zaviye morede nazar khod ra vared konid :   \n")
        a=int(input())
        a=a*math.pi/180
        s=math.tan(a)
        print (" tan ", a , "=" , s)

    elif x==8 :
        print (" zaviye morede nazar khod ra vared konid :   \n")
        a=int(input())
        a=a*math.pi/180
        s=1/math.tan(a)
        print (" cot ", a , "=" , s)

    elif x==9 :
        print (" zaviye morede nazar khod ra vared konid :   \n")
        a=int(input())
        s=math.log10(a)
        print (" log  ", a , "=" , s)

    elif x==10 : 
        break

    else : 
        print(" gozine eshtebah ra vared kardid :  \n")
