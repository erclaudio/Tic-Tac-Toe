def draw_board(spots):
    board = (f"\033[4m{spots[1]}\033[0m|\033[4m{spots[2]}\033[0m|\033[4m{spots[3]}\033[0m\n"
    f"\033[4m{spots[4]}\033[0m|\033[4m{spots[5]}\033[0m|\033[4m{spots[6]}\033[0m\n"
    f"{spots[7]}|{spots[8]}|{spots[9]}")
    
    print(board)


def check_turn(turn):
    if turn %2 == 0: return 'O'
    else: return 'X'

def check_win(spots):
    if(spots[1]==spots[2]==spots[3]) \
    or(spots[4]==spots[5]==spots[6]) \
    or(spots[7]==spots[8]==spots[9]):
        return True
    
    elif(spots[1]==spots[4]==spots[7]) \
    or(spots[2]==spots[5]==spots[8]) \
    or(spots[3]==spots[6]==spots[9]):
        return True
    
    elif(spots[1]==spots[5]==spots[9]) \
    or(spots[3]==spots[5]==spots[7]):   
        return True
    
    else:
        return False