import random


game = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]
def reset():
    game[0] = ["-","-","-"]
    game[1] = ["-","-","-"]
    game[2] = ["-","-","-"]

def show ():    
    for i in range(3):
        for j in range(3):
            print(game[i][j] , end ='')
        print()

def check():

    for i in range(3):
            if game[i][0]==game[i][1]==game[i][2]:
                return True,game[i][0]
            elif game[0][i]==game[1][i]==game[2][i]:
                return True,game[0][i]
            if game[0][0]==game[1][1]==game[2][2]:
                return True, game[0][0]
            elif game[0][2]==game[1][1]==game[2][0]:
                return True , game[0][2]
    return False,game[0][0]

   # if game[0][0]==game[0][1]==game[0][2] or
     #   game[1][0]==game[1][1]==game[1][2] or
       # game[2][0]==game[2][1]==game[2][2] or 
        #game[0][0]== game[1][0]==game[2][0] or
        #game[1][0]==game[1][1]==game[1][2] or
        #game[2][0]== game[2][1] == game[2][2] or
       # game[0][0]==game[1][1]==game[2][2] or
       # game[0][2]==game[1][1]==game[2][0]:
        #print ("win")


def multiplayer():
    
    show ()
    while (True):
        #player1
        while True :
            print("player 1: ")
            row = int(input("row : "))
            col = int(input("col : "))
            if 0<=row<=2 and 0<=col<=2:
                if game[row][col]=="-":
                    game[row][col] ="X"
                    show()
                    break
                else:
                    print("this isnt empty, try aggain :")
            else:
                print (" invalid input ; row and col must be between 0 ,2 :")

        _check , winner = check()
        if _check==True and winner!="-":
            print (winner,"win")
            return

        if "-" not in game[0] and \
            "-" not in game[1] and \
            "-" not in game[2]  :
                print ("draw")
                return 

        #player2

        while True :
            print("player 2: ")
            row = int(input("row : "))
            col = int(input("col : "))
            if 0<=row<=2 and 0<=col<=2:
                if game[row][col]=="-":
                    game[row][col] = "O"
                    show()
                    break
                else:
                    print("this isnt empty, try aggain :")
            else:
                print (" invalid input ; row and col must be between 0 ,2 :")

        _check , winner = check()
        if _check==True and winner!="-":
            print (winner,"win")
            return


        if "-" not in game[0] and \
            "-" not in game[1] and \
            "-" not in game[2]  :
                print ("draw")
                return 

def co_play():

    show ()
    while(True):
        #player1
        while True :
            print("player 1: ")
            row = int(input("row : "))
            col = int(input("col : "))
            if 0<=row<=2 and 0<=col<=2:
                if game[row][col]=="-":
                    game[row][col] ="X"
                    show()
                    break
                else:
                    print("this isnt empty, try aggain :")
            else:
                print (" invalid input ; row and col must be between 0 ,2 :")

        _check , winner = check()
        if _check==True and winner!="-":
            print (winner,"win")
            return

        if "-" not in game[0] and \
            "-" not in game[1] and \
            "-" not in game[2]  :
                print ("draw")
                return 
        

        while True :
            print("computer : ")
            row = random.randint(0,2)
            col = random.randint(0,2)
            if game[row][col]=="-":
                game[row][col] ="O"
                show()
                break
            else:
                print("this isnt empty, try aggain :")
        

        _check , winner = check()
        if _check==True and winner!="-":
            print (winner,"win")
            return
            
        if "-" not in game[0] and \
        "-" not in game[1] and \
        "-" not in game[2]  :
            print ("draw")
            return 
        

x=0
while(x!=3):

    print("[1]:co-player:pve")
    print("[2]:player-player:pvp")
    print("[3]:exit")

    x=int(input("select options by entering its number:"))
    if x==1:
        co_play()
        reset();
    elif x==2:
        multiplayer()
        reset();
    elif x!=3:
        print("enter valid number")
    


