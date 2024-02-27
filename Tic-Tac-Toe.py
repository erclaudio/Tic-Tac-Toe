from helpers import draw_board
from helpers import check_turn
from helpers import check_win
import os
#spots
spots = {1:'1',2:'2',3:'3',4:'4', 5:'5', 6:'6',7:'7',8:'8',9:'9'}
draw_board(spots)

playing = True
complete = False
winner = ""
turn = 0
prev_turn = -1
while playing:
    #reset screen 
    os.system('cls' if os.name =='nt' else 'clear')
    draw_board(spots)
    if prev_turn == turn :
        print("Invalid input, try again")
    prev_turn = turn
    print("Player: "+check_turn(turn-1),", pick your spots or press Q to quit")
    choice = input()
    if choice == "q":
        playing = False
        #print("The winner is: "+ winner)
    #check input is valid number
    elif str.isdigit(choice) and int(choice) in spots:
    #check spot is not taken
        if not spots[int(choice)] in {"X", "O"}:
            turn +=1
            spots[int(choice)] = check_turn(turn)
    if check_win(spots): 
        playing, complete = False, True
        print("Winner is player: "+ check_turn(turn))
        break
    if turn == 9 and not check_win(spots):
        playing, complete = False, True
        print("It's a draw")
        break
draw_board(spots)



    

"""
def main():
    chosenChar = input("Choose X or O")
    if chosenChar == "X":
        oppositeChar = "O"
    else:
        oppositeChar = "X"
    winner = ""
    currentState = list(" " * 10)  # Initialize with 10 elements (index 0 to 9)
    
    emptyBoard = "\033[4m1\033[0m|\033[4m2\033[0m|\033[4m3\033[0m\n\033[4m4\033[0m|\033[4m5\033[0m|\033[4m6\033[0m\n7|8|9 "
    print(emptyBoard)
    
    while winner == "":
        nextChar = int(input("Select a number to insert your character in: "))
        
        # Check if the selected index is valid
        if 1 <= nextChar <= 9 and currentState[nextChar] == " ":
            currentState[nextChar] = chosenChar
            print(currentState)
            print(emptyBoard)
        if (currentState[0]==currentState[1]==currentState[2] or
        currentState[4]==currentState[5]==currentState[6] or
        currentState[7]==currentState[8]==currentState[9] or
        currentState[1]==currentState[4]==currentState[7] or
        currentState[2]==currentState[5]==currentState[8] or
        currentState[3]==currentState[6]==currentState[9] or
        currentState[0]==currentState[1]==currentState[2] or
        currentState[0]==currentState[1]==currentState[2]):
        
            nextInput = int(input)


    
    
if __name__ == "__main__":
    main()
"""