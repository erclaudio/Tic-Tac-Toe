def draw_board(spots):
    board = (f"\033[4m{spots[1]}\033[0m|\033[4m{spots[2]}\033[0m|\033[4m{spots[3]}\033[0m\n"
    f"\033[4m{spots[4]}\033[0m|\033[4m{spots[5]}\033[0m|\033[4m{spots[6]}\033[0m\n"
    f"{spots[7]}|{spots[8]}|{spots[9]}")
    
    print(board)


def check_turn(turn):
    if turn %2 == 0: return 'O'
    else: return 'X'
