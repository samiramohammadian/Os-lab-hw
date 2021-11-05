from os import linesep


def show_menu():

    print("----------------------------------------------------")


    print(" Welcome to my store: ")
    print(" 1.add ")
    print(" 2.edit ")
    print(" 3.delete ")
    print(" 4.show List ")
    print(" 5.search ")
    print(" 6.buy ")
    print(" 7.exit ")

    print("----------------------------------------------------")


Products=[]





def load_data_from_datastore():
    f = open('datastore.csv', 'r')
    for line in f:
        info = line[:-1].split(',')
        new_dict = {'id': info[0], 'Name': info[1], 'Price': info[2], 'Stock': info[3]}

        Products.append(new_dict)
    
def show_List():
    print('id','\t\t'  ,  'Name','\t\t'  ,  'Price' ,'\t\t'  ,  'Stock')
    for product in Products:
        print(product['id'], '\t\t', product['Name'], '\t\t', product['Price'], '\t\t', product['Stock'])



def add(): 
    while(True):

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
            


        



def edit():
    show_List()
    x=int(input())

    for pr in Products:
       if pr['id']==x:

            pr['Name']=input('enter your Name :')
            pr['Price']=input('enter your Price :')
            pr['Stock']=input('enter your Stock :')

    


def delete():
    show_List()

    x=int(input("Enter the product id :"))
    for pro in Products:
        if pro['id']==x:
            Products.remove(pro)

            




def search():
    name = input('Enter the product name : ')
    k = 0
    found = False
    for i in Products:






        if i['Name'] == name:
            found = True
            break
        else:
            k += 1
    if found==True:

        print('Your search result :', 
              '\n id : ', Products[k]['id'],
              '\nPrice: ', Products[k]['Price'],
              '\nStock: ', Products[k]['Stock'])
    else:
        print('You did not select the correct option!')

       


def buy():
    arr=[]
    p=True
    while True:
        
        if p==True:

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

        if answer== "y" :
            p=True
        elif answer == "n":
            p=False  
            break
        else:

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