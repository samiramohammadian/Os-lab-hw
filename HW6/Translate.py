
WORDS_BANK = []

def menu():
    print("************************************************\n")
    print("Welcome to my DICTIONARY :\n")
    print("  1. English to Persian   \n")
    print("  2. Persian to English   \n")
    print("  3. Add NEW word         \n")
    print("  4. Exit                 \n")
    print("************************************************\n")


def load_data ():
    print ("Loadong...\n")
    try :
        f=open('words_bank.txt' , 'r')
        txt=f.read()
        words = txt.split('\n')

        for i in range(0 , len(words) , 2):
            WORDS_BANK.append({'english' : words[i] , 'persian' : words[i+1] } ) 
        print("cant open this file ")
        
    except :
        print("Loaded !! \n")
        


def en2fa():
    print("\n**************** English to Persian ***************\n")
    input_text=input("please write your text \n")
    user_sentesnces = input_text.split(".")
    output_text = ""
    for i in user_sentesnces :
        user_word=i.split(" ")
        output=""
        for u_word in user_word :
            for word in WORDS_BANK:
                if u_word == word['english'] :
                    output += word['persian'] + " "
                    break
            else :
                output += u_word + " "
        output_text += output + "."

    print ("*** Meaning :" + "\t" + output_text +"\n ****************")

def fa2en ():
    print("\n************** Persian to English ****************\n")
    input_text=input("please write your text to finglish  \n")
    user_sentesnces = input_text.split(".")
    output_text = ""
    for i in user_sentesnces :
        user_word=i.split(" ")
        output=""
        for u_word in user_word :
            for word in WORDS_BANK:
                if u_word == word['persian'] :
                    output += word['english'] + " "
                    break
            else :
                output += u_word + " "
        output_text += output + "."

    print ("*** In English :"+"\t" + output_text +"\n *******************")

def add():

    new_en = input("Please enter the word in English  \n")
    new_fa = input("Please enter the meaning of the word in Finglish \n")
    for word in WORDS_BANK:
        if word["english"] == new_en or word ["persian"] == new_fa:
            print("This word is now available ...!!!!!\n")
            break
    else:

        WORDS_BANK.append({'english' : new_en  , 'persian' : new_fa})
        print("********************  Successfully added :)  **************************")


def ext():
    f=open('words_bank.txt' , 'w')
    for i in WORDS_BANK :
        f.write(i["english"])
        f.write("\n")
        f.write(i["persian"])
        f.write("\n")
    print("******************* Saved successfully \n****************************")

load_data ()
print("Exit the menu if you want the words you added to be saved successfully  !!!")
while True:
    menu()
    
    choice = int (input("please choose from menu : \n"))
    
            
    if choice == 1:
        en2fa()
    elif choice == 2:
        fa2en()
    elif choice == 3:
        add()
    elif choice == 4:
        ext()
        break









 

