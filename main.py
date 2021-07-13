import copy
import random
#creates a 3x3 2D array of None values
def new_board():
    board = []
    for x in range(3):
        column = []
        for y in range(3):
            column.append(None)
        board.append(column)
    return board

#prints the board to the terminal with coordinates at the top and left
def render(board):
    print("  0 1 2")
    print("  ------")
    for x in range(3):
        print(x, end='')    #prints left-side (y) coordinates
        print('|', end='')
        for y in range(3):
            if board[x][y] == None:
                print(' ', end=' ')
            else:
                print(board[x][y], end=' ')
        print('|')
    print("  ------")

#gets move from user and returns the coordinates as a tuple
def get_move():
    #these are swapped b/c the board is inverted for some reason
    y = input("What is your x-coordinate: ")
    x = input("What is your y-coordinate: ")
    return (int(x),int(y))
    
#checks if move is valid on board
def is_valid_move(board, move):
    for x in range(2):
        if move[x] > 2 or move[x] < 0:
            return False
    if board[move[0]][move[1]] != None:
        return False
    return True

#checks if move is valid and makes the move if so or says the move is invalid and gets a new move
def make_move(board, move, player):
    if player == 0:
        if is_valid_move(board, move):
            new_board = board
            new_board[move[0]][move[1]] = 'X'
    if player == 1:
        if is_valid_move(board, move):
            new_board = board
            new_board[move[0]][move[1]] = 'O'

#checks if there is a winner on the board and returns the char if so
#if not then returns None
def check_winner(board):
    lines = [ board[0], board[1], board[2] ]
    lines.append([ row[0] for row in board ])
    lines.append([ row[1] for row in board ])
    lines.append([ row[2] for row in board ])
    lines.append([ board[0][0], board[1][1], board[2][2] ])
    lines.append([ board[2][0], board[1][1], board[0][2] ])
    for x in range(8):
        if lines[x].count(lines[x][0]) == 3:
            if lines[x][0] != None:
                return lines[x][0]
    return None

def ai(board):
    ai_future = copy.deepcopy(board)
    user_future = copy.deepcopy(board)
    winning_user_moves = []
    #check if any valid move wins (ai or user)
    for x in range(3):
        for y in range(3):
            if is_valid_move(board, (x,y)):
                ai_future[x][y] = 'X'
                user_future[x][y] = 'O'
                if check_winner(ai_future) == 'X':
                    make_move(board, (x,y), 0)
                    return
                if check_winner(user_future) == 'O':
                    #store move
                    winning_user_moves.append((x,y))
                ai_future = copy.deepcopy(board)
                user_future = copy.deepcopy(board)
    if winning_user_moves:
        make_move(board, winning_user_moves[0], 0)
        return

    #check if center is valid
    if is_valid_move(board, (1,1)):
        make_move(board, (1,1), 0)
        return
    
    #if after move 3 user has opposite diagonals, go non corner
    if board[0][0] == 'O' and board[2][2] == 'O' or board[2][0] == 'O' and board[0][2] == 'O':
        if is_valid_move(board, (1,0)):
            make_move(board, (1,0), 0)
            return
        elif is_valid_move(board, (0,1)):
            make_move(board, (0,1), 0)
            return
        elif is_valid_move(board, (2,1)):
            make_move(board, (2,1), 0)
            return
        elif is_valid_move(board, (1,2)):
            make_move(board, (1,2), 0)
            return
    
    #check if corner is valid
    if is_valid_move(board, (0,0)):
        make_move(board, (0,0), 0)
        return
    elif is_valid_move(board, (2,0)):
        make_move(board, (2,0), 0)
        return
    elif is_valid_move(board, (0,2)):
        make_move(board, (0,2), 0)
        return
    elif is_valid_move(board, (2,2)):
        make_move(board, (2,2), 0)
        return
    
    #else
    if is_valid_move(board, (1,0)):
        make_move(board, (1,0), 0)
        return
    elif is_valid_move(board, (0,1)):
        make_move(board, (0,1), 0)
        return
    elif is_valid_move(board, (2,1)):
        make_move(board, (2,1), 0)
        return
    elif is_valid_move(board, (1,2)):
        make_move(board, (1,2), 0)
        return

#main

#coin flip to choose who goes first
num = random.randint(0,9)
choice = input("Heads or tails?")
choice.lower()
choice2 = "no"

if num % 2 == 0:
    print("It was heads")
else:
    print("It was tails")
if choice == "heads" and num % 2 == 0:
    choice2 = input("Would you like to go first?")
    choice2.lower()
elif choice == "heads" and num % 2 != 0:
    print("Sorry")
elif choice == "tails" and num % 2 == 0:
    print("Sorry")
else:
    choice2 = input("Would you like to go first?")
    choice2.lower()

if choice2 == "yes":
    player = 1
else:
    player = 0


board = new_board()
render(board)

#game loop
for x in range(9):
    if not player:
        print("\nMy turn\n")
        ai(board)
        winner = 0
        player = 1
    else:
        print("\nYour turn\n")
        move = get_move()
        if is_valid_move(board, move):
            make_move(board, move, 1)
        else:
            print("Move is invalid")
            while(not is_valid_move(board, move)):
                move = get_move()
            make_move(board, move, 1)
        winner = 1
        player = 0
    if check_winner(board):
        print("Winner is: ")
        if winner:
            print('O')
            render(board)
        else:
            print('X')
            render(board)
        break
    render(board)
    print("")

if not check_winner(board):
    print("Draw")