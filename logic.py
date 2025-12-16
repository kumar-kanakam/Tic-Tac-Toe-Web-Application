import random

def check_winner(board, player):
    win = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for x,y,z in win:
        if board[x] == board[y] == board[z] == player:
            return True
    return False

def available_moves(board):
    return [i for i in range(9) if board[i] == ""]

def best_move(board):
    for move in available_moves(board):
        board[move] = "O"
        if check_winner(board, "O"):
            board[move] = ""
            return move
        board[move] = ""

    for move in available_moves(board):
        board[move] = "X"
        if check_winner(board, "X"):
            board[move] = ""
            return move
        board[move] = ""

    if 4 in available_moves(board):
        return 4
        x_move=[]
    if (len(available_moves(board))==8):
        if board[4]=="X":
            return 0
    if (len(available_moves(board))==6):
        x_move = [i for i in range(9) if board[i] == "X"]
        if (1 in x_move)and(8 in x_move):
            return 3
        if (1 in x_move)and((3 in x_move)or(5 in x_move)):
            return sum(x_move)-4
        if (7 in x_move)and((3 in x_move)or(5 in x_move)):
            return sum(x_move)-4   
        elif(1 in x_move)and(6 in x_move):
            return 5
        elif(4 in x_move)and(8 in x_move):
            return 6
        elif(3 in x_move)and(2 in x_move):
            return 7
        elif(3 in x_move)and(8 in x_move):
            return 1 
        elif(5 in x_move)and(0 in x_move):
            return 7
        elif(5 in x_move)and(6 in x_move):
            return 1
        elif(7 in x_move)and(0 in x_move):
            return 5
        elif(7 in x_move)and(2 in x_move):
            return 3
        elif(0 in x_move)and(8 in x_move):
            return 1
        else:
            pass
    return random.choice(available_moves(board))
