import random
words_banks = ['tree', 'book' , 'python','sadjad', 'linux' , 'oslab' , 'mac','windows','java']

word=words_banks[random.randint(0,len(words_banks)-1)]

joon =2*len(word)

user_true_char=[]

while "true":
    win=1 

    for char in word:
        if char in user_true_char:
            print(char,end='')
        else:
            print("_ ",end='') 
            win=0

    if win==1:
        print("\n" , "You won :D \n")
        break
    print("\n" ,"joon = ",joon)
    

    char=input("Enter a letter : \n")
    if char in word:
        user_true_char.append(char)

        print("✅")
    else:
        print("❌")
        joon-=1
    
    if joon==0:
        print ("The answer is :    " , word ,"\n")
        print("game over  :(")

        break