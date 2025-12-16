from django.shortcuts import render, redirect
from .logic import check_winner, best_move

def select_mode(request):
    return render(request, 'game/select_mode.html')

def start_game(request, mode):
    request.session['board'] = [""] * 9
    request.session['mode'] = mode
    request.session['turn'] = "X"
    request.session['game_over'] = False

    if mode == "pvp":
        request.session['message'] = "X's Turn"
    else:
        request.session['message'] = "Your Turn (X)"

    return redirect('game')



def game(request):
    if 'mode' not in request.session:
        return redirect('select_mode')
    return render(request, 'game/index.html', {
        'board': request.session.get('board', [""] * 9),
        'mode': request.session.get('mode'),
        'turn': request.session.get('turn', "X"),
        'message': request.session.get('message', "Select a mode"),
        'game_over': request.session.get('game_over', False),
    })


def move(request, cell):
    if not request.session.get('board'):
        return redirect('select_mode')

    if request.session.get('game_over'):
        return redirect('game')

    board = request.session['board']
    mode = request.session['mode']

    if mode == "pvp":
        turn = request.session['turn']

        if board[cell] == "":
            board[cell] = turn

            if check_winner(board, turn):
                request.session['message'] = f"{turn} Wins!"
                request.session['game_over'] = True
                return redirect('game')

            if "" not in board:
                request.session['message'] = "It's a Tie!"
                request.session['game_over'] = True
                return redirect('game')

            # switch turn
            request.session['turn'] = "O" if turn == "X" else "X"
            request.session['message'] = f"{request.session['turn']}'s Turn"

    # ================= PLAYER vs COMPUTER =================
    elif mode == "pvc":
        if board[cell] == "":
            # Human always X
            board[cell] = "X"

            if check_winner(board, "X"):
                request.session['message'] = "X Wins!"
                request.session['game_over'] = True
                return redirect('game')

            if "" not in board:
                request.session['message'] = "It's a Tie!"
                request.session['game_over'] = True
                return redirect('game')

            # Computer move
            ai = best_move(board)
            board[ai] = "O"

            if check_winner(board, "O"):
                request.session['message'] = "Computer Wins!"
                request.session['game_over'] = True
                return redirect('game')

            request.session['message'] = "Your Turn (X)"

    request.session['board'] = board
    return redirect('game')


def reset_game(request):
    mode = request.session.get('mode')
    return redirect('start', mode=mode)

def back_to_menu(request):
    request.session.flush()
    return redirect('select_mode')
