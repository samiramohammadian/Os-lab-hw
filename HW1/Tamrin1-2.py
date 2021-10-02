print("adad aval ra vared konid: \n")
A=int(input())
print("adad dovom ra vared konid: \n")
B=int(input())
print("adad sevom ra vared konid: \n")

C=int(input())

if A>0 and B>0 and C>0 :
    if A+B>C and B+C>A and A+C>B:
        print("ba in 3 adad mosalas sakhte mishavd. ")
    else :
        print("ba in 3 adad mosalas sakhte nemishavd. ")
else :
    print("ba in 3 adad mosalas sakhte nemishavd. ")