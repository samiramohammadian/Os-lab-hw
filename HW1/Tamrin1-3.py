print ("please enter your weight",  "Kg")
weight=float (input())

print ("please enter your height"  ,"m")
height =float (input())

BMI= weight/ (height*height)

if  BMI < 18.5 :
   print("You are Losing weight.\n")  

elif 18.5< BMI <24.9 :
    print("You are Normal. \n")
elif 25 < BMI <29.9 :
    print ("You are Overweight. \n")
elif 30< BMI <34.9 :
    print ("You are Obese. \n")
elif BMI>35 :
    print ("You are Extremely obese.")
