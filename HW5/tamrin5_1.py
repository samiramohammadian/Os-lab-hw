from os import linesep


def show_menu():
<<<<<<< HEAD
    print("----------------------------------------------------")
=======
>>>>>>> dba6d24abd3a2e315769d6699112f3b5b98e792e
    print(" Welcome to my store: ")
    print(" 1.add ")
    print(" 2.edit ")
    print(" 3.delete ")
    print(" 4.show List ")
    print(" 5.search ")
    print(" 6.buy ")
    print(" 7.exit ")
<<<<<<< HEAD
    print("----------------------------------------------------")


Products=[]
=======


kala=[]
>>>>>>> dba6d24abd3a2e315769d6699112f3b5b98e792e

def load_data_from_datastore():
    f = open('datastore.csv', 'r')
    for line in f:
        info = line[:-1].split(',')
        new_dict = {'id': info[0], 'Name': info[1], 'Price': info[2], 'Stock': info[3]}
<<<<<<< HEAD
        Products.append(new_dict)
    
def show_List():
    print('id','\t\t'  ,  'Name','\t\t'  ,  'Price' ,'\t\t'  ,  'Stock')
    for product in Products:
        print(product['id'], '\t\t', product['Name'], '\t\t', product['Price'], '\t\t', product['Stock'])
=======
        kala.append(new_dict)
    
>>>>>>> dba6d24abd3a2e315769d6699112f3b5b98e792e


def add(): 
    while(True):
<<<<<<< HEAD
        chiocess=True
        if chiocess==True:
            show_List()
        
            productId = int(input('enter Id of product : '))
            for product in Products:
                if productId == int(product['id']):
                    print("product is existed ... ")
                    break
            else:
                productName = input('enter name of product : ')
                productPrice = int(input('enter price of product : '))
                productCount = int(input('enter stock of product : '))
                Products.append({'id':productId,'Name':productName,'Price':productPrice,'Stock':productCount})

        chiocess=False
        tekrar=(input("Do you want to buy another product? (y/n) :"))
        if tekrar=="n":
            break
        elif tekrar=="y":
            chiocess=True
        else :
            print("Wrong option..... try aggain")
            break
            

=======
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
>>>>>>> dba6d24abd3a2e315769d6699112f3b5b98e792e




def edit():
    show_List()
    x=int(input())
<<<<<<< HEAD
    for pr in Products:
       if pr['id']==x:

            pr['Name']=input('enter your Name :')
            pr['Price']=input('enter your Price :')
            pr['Stock']=input('enter your Stock :')
=======
    for kal in kala:
        if kal['id']==x:

            kal['Name']=input('enter your Name :')
            kal['Price']=input('enter your Price :')
            kal['Stock']=input('enter your Stock :')
>>>>>>> dba6d24abd3a2e315769d6699112f3b5b98e792e


def delete():
    show_List()
<<<<<<< HEAD
    x=int(input("Enter the product id :"))
    for pro in Products:
        if pro['id']==x:
            Products.remove(pro)
=======
    x=int(input("id kala ra vared konid :"))
    for kal in kala:
        if kal['id']==x:
            kala.remove(kal)
>>>>>>> dba6d24abd3a2e315769d6699112f3b5b98e792e
            



<<<<<<< HEAD
def search():
    name = input('Enter the product name : ')
    k = 0
    found = False
    for i in Products:
=======




def search():
    name = input('name kala ra vared konid : ')
    k = 0
    found = False
    for i in kala:
>>>>>>> dba6d24abd3a2e315769d6699112f3b5b98e792e
        if i['Name'] == name:
            found = True
            break
        else:
            k += 1
    if found==True:
<<<<<<< HEAD
        print('Your search result :', 
              '\n id : ', Products[k]['id'],
              '\nPrice: ', Products[k]['Price'],
              '\nStock: ', Products[k]['Stock'])
    else:
        print('You did not select the correct option!')
=======
        print(' natije josto joye shoma :', 
              '\n id : ', kala[k]['id'],
              '\nPrice: ', kala[k]['Price'],
              '\nStock: ', kala[k]['Stock'])
    else:
        print('Dorost vared nakardid!')
>>>>>>> dba6d24abd3a2e315769d6699112f3b5b98e792e


def buy():
    arr=[]
    p=True
    while True:
        
        if p==True:
<<<<<<< HEAD
            show_List()
            x=input("Enter the product name : \n")
            
            for i in Products:
                if x == i["Name"]:
                    arr.append(i)
                    i['Stock'] = int (i['Stock']) - 1
                    break
            else :
                print ("Product not available. \n")
                break
                    


        answer=input("Do you have another purchase?? (y/n) :")  
=======
            x=input("esm mahsol ra vred kkonid: \n")
            
            for i in kala:
                if x in i["Name"]:
                    arr.append(i)

        answer=input("kharid digari darid? (y/n) :")  
>>>>>>> dba6d24abd3a2e315769d6699112f3b5b98e792e
        if answer== "y" :
            p=True
        elif answer == "n":
            p=False  
            break
        else:
<<<<<<< HEAD
            print("You did not select the correct option !")

    for i in arr:
        print( i["Name"],"\t",i["Price"],"\t",i["Stock"], "\n")
            


def exit():
    f = open('datastore.csv', 'w')
    
    for i in Products:

        f.write(str(i["id"])+","+str(i["Name"])+","+str(i["Price"])+","+str(i["Stock"])+"\n")

    f.close()

load_data_from_datastore()
while True:
    show_menu()
    choice = int (input("please choose from menu : \n"))
=======
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
>>>>>>> dba6d24abd3a2e315769d6699112f3b5b98e792e
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