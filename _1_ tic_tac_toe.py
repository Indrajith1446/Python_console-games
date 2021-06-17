from IPython.display import clear_output

def display_board(board):
    print("   BOARD                   MODEL ")
    print("**************************************")
    print(f" {board[6]} | {board[7]} | {board[8]}               7 | 8 | 9 ")
    print("___________             ___________")
    print(f" {board[3]} | {board[4]} | {board[5]}               4 | 5 | 6 ")
    print("___________             ___________")
    print(f" {board[0]} | {board[1]} | {board[2]}               1 | 2 | 3 ")

def player_input(Player):
    condition=False
    while not condition :
        p1val=input("Enter the marker for player 1 ( X or O ) : ")
        if p1val=='x' or p1val=='X':
            Player[0]='X'
            Player[1]='O'
            condition=True
        else:
            if p1val=='o' or p1val=='O':
                Player[0]='O'
                Player[1]='X'
                condition=True
            else:
                print(" Sorry you have entered a wrong input please choose from 'X' or 'O' !")
    print(f"Now : \nplayer 1 is '{Player[0]}' \nPlayer 2 is '{Player[1]}'")
    return Player

def place_marker(board, marker, position):
    board[position-1]=marker

def win_check(board, mark):
    
    if board[0]==mark and board[1]==mark and board[2]==mark:
        return True
    elif board[3]==mark and board[4]==mark and board[5]==mark:
        return True
    elif board[6]==mark and board[7]==mark and board[8]==mark:
        return True
    elif board[0]==mark and board[3]==mark and board[6]==mark:
        return True
    elif board[1]==mark and board[4]==mark and board[7]==mark:
        return True
    elif board[2]==mark and board[5]==mark and board[8]==mark:
        return True
    elif board[0]==mark and board[4]==mark and board[8]==mark:
        return True
    elif board[2]==mark and board[4]==mark and board[6]==mark:
        return True
    else:
        return False

import random

def choose_first():
    return random.randint(1,2)

def space_check(board, position):
    
    if board[position-1]=='X' or board[position-1]=='O':
        return False
    else:
        return True

def full_board_check(board):
    flag=True
    for x in range(0,9):
        if space_check(board,x):
            flag=False
    return flag

def player_choice(board):
    
   condition=False 
   while not condition:
       choice=int(input("Enter Your choice (1-9) as per the model : "))
       if choice <=0 or choice >=10 :
           print(f" Entered position {choice} out of bounds\nPlease enter an number between 1 and 9 !")
       else:
            if space_check(board,choice):
                return choice
                condition=True
            else:
                print(f"Position {choice} is already occupied please provide a free postion form 1 to 9 !")

def replay():
    
    condition=False
    while not condition:
        choice=input(("Do you want to continue playing ? Y or N "))
        if choice=='y' or choice=='Y':
            return True
        elif choice=='n' or choice=='N':
            return False
        else :
            print("Not a valid input! please respond again.")

if __name__ =="__main__":

    print('Welcome to Tic Tac Toe!\n')
    while True:
        game_on=True
        board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        Player=['','']
        Player=player_input(Player)
        counter=0
        while game_on:
            clear_output()
            display_board(board)
            if counter %2 == 0:
                print(f"\nPLAYER 1's TURN {Player[0]}")
                choice=player_choice(board)
                place_marker(board,Player[0],choice)
            else:
                print(f"\nPLAYER 2's TURN {Player[1]}")
                choice=player_choice(board)
                place_marker(board,Player[1],choice)
            if full_board_check(board):
                if win_check(board,'X' ) or win_check(board,'O'):
                    if win_check(board,'X'):
                        if(Player[0]=='X'):
                            print("\nCONGRADULATIONS PLAYER 1 WON ")
                        else :
                            print("\nCONGRADULATIONS PLAYER 2 WON ")
                    else:
                        if(Player[0]=='O'):
                            print("\nCONGRADULATIONS PLAYER 1 WON ")
                        else :
                            print("\nCONGRADULATIONS PLAYER 2 WON ")
                print("\n   GAME OVER ")
                game_on=False
            else:
                if win_check(board,'X' ) or win_check(board,'O'):
                    if win_check(board,'X'):
                        if(Player[0]=='X'):
                            print("\nCONGRADULATIONS PLAYER 1 WON ")
                        else :
                            print("\nCONGRADULATIONS PLAYER 2 WON ")
                    else:
                        if(Player[0]=='O'):
                            print("\nCONGRADULATIONS PLAYER 1 WON ")
                        else :
                            print("\nCONGRADULATIONS PLAYER 2 WON ")
                    print("\n   GAME OVER ")
                    game_on=False
            counter+=1
        if not replay():
            print( "\n\n THANK YOU FOR PLAYING HAVE A NICE DAY")
            break