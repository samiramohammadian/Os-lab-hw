from os import linesep


def show_menu():
    print(" Welcome to my store: ")
    print(" 1.add ")
    print(" 2.edit ")
    print(" 3.delete ")
    print(" 4.show List ")
    print(" 5.search ")
    print(" 6.buy ")
    print(" 7.exit ")


kala=[]

def load_data_from_datastore():
    f = open('datastore.csv', 'r')
    for line in f:
        info = line[:-1].split(',')
        new_dict = {'id': info[0], 'Name': info[1], 'Price': info[2], 'Stock': info[3]}
        kala.append(new_dict)
    


def add(): 
    while(True):
        c=True
        if c==True:
            new_kala={'id': int(input("id kala ra vared konid.")) , 'Name': input("esm kala ra vared konid.") , 'Price': int(input("gheymate kala ra vared konid.")) , 'Stock' :int(input("tedad kala ra vared konid."))}

            if new_kala not in kala :
                kala.append(new_kala)
            else:
                print("kala mojod ast.")

        c=False
        tekrar=(input("kalaye digari mikhahid vared kkonid (y/n) :"))
        if tekrar=="n":
            break
        elif tekrar=="y":
            c=True
        else :
            print("gozine dorosti entekhab nakrdid.")
            break
            

def show_List():
    print('id  ,  Name  ,  Price  ,  Stock')
    for product in kala:
        print(product['id'], '  ', product['Name'], '  ', product['Price'], '  ', product['Stock'])




def edit():
    show_List()
    x=int(input())
    for kal in kala:
        if kal['id']==x:

            kal['Name']=input('enter your Name :')
            kal['Price']=input('enter your Price :')
            kal['Stock']=input('enter your Stock :')


def delete():
    show_List()
    x=int(input("id kala ra vared konid :"))
    for kal in kala:
        if kal['id']==x:
            kala.remove(kal)
            







def search():
    name = input('name kala ra vared konid : ')
    k = 0
    found = False
    for i in kala:
        if i['Name'] == name:
            found = True
            break
        else:
            k += 1
    if found==True:
        print(' natije josto joye shoma :', 
              '\n id : ', kala[k]['id'],
              '\nPrice: ', kala[k]['Price'],
              '\nStock: ', kala[k]['Stock'])
    else:
        print('Dorost vared nakardid!')


def buy():
    arr=[]
    p=True
    while True:
        
        if p==True:
            x=input("esm mahsol ra vred kkonid: \n")
            
            for i in kala:
                if x in i["Name"]:
                    arr.append(i)

        answer=input("kharid digari darid? (y/n) :")  
        if answer== "y" :
            p=True
        elif answer == "n":
            p=False  
            break
        else:
            print("gozine dorost ra vared nakardid ")


    
    for i in arr:
        print( i["Name"],"\t",i["Price"],"\t",i["Stock"], "\n")
            
def exit():
    f = open('datastore.csv', 'w')
    
    for i in kala:

         f.write(i["id"]+","+i["Name"]+","+i["Price"]+","+i["Stock"]+"\n")
    f.close()


while True:
    show_menu()
    choice = int (input("please choose from menu : \n"))
    load_data_from_datastore()
    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        delete()
    elif choice == 4:
        show_List()
    elif choice == 5:
        search()
    elif choice == 6:
        buy()
    elif choice == 7:
        exit()
        break