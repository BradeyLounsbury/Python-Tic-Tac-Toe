def new_board():
    board = []
    for x in range(0, 3):
        column = []
        for y in range(0, 3):
            column.append(None)
        board.append(column)
    return board

def render(board):
    print("  0 1 2")
    print("  ------")
    for x in range(3):
        print(x, end='')
        print('|', end='')
        for y in range(3):
            if board[x][y] == None:
                print(' ', end=' ')
            else:
                print(board[x][y], end=' ')
        print('|')
    print("  ------")

def get_move():
    #these are swapped b/c the board in inverted for some reason
    y = input("What is your x-coordinate: ")
    x = input("What is your y-coordinate: ")
    return (int(x),int(y))
    
def is_valid_move(board, move):
    for x in range(2):
        if move[x] > 2 or move[x] < 0:
            return False
    if board[move[0]][move[1]] != None:
        return False
    return True

def make_move(board, move, player):
    #check if move is valid
    if is_valid_move(board, move):
        new_board = board
        new_board[move[0]][move[1]] = player
    #if move is valid => make move
    else:
        print("Move is invalid")
        get_move()
        make_move(board,move,player)

def check_winner(board):
    lines = [ board[0], board[1], board[2] ]
    lines.append([ row[0] for row in board ])
    lines.append([ row[1] for row in board ])
    lines.append([ row[2] for row in board ])
    lines.append([ board[0][0], board[1][1], board[2][2] ])
    lines.append([ board[2][0], board[1][1], board[0][2] ])
    for x in range(8):
        if lines[x].count(lines[x][0]) == len(lines[x]):
            if lines[x][0] != None:
                return lines[x][0]
    return None



board = new_board()
render(board)
for x in range(9):
    move = get_move()
    if x % 2 == 0:
        make_move(board, move, 'X')
    else:
        make_move(board, move, 'O')
    winner = check_winner(board)
    if winner != None:
        break
    render(board)

print("Winner is: ")
print(winner)