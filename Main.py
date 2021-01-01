board = [[" ", "|", " ", "|", " "],
        ["-", "+", "-", "+", "-"],
        [" ", "|", " ", "|", " "],
        ["-", "+", "-", "+", "-"],
        [" ", "|", " ", "|", " "]]

def lookCoord(board):
    count = 1
    dicts = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                dicts[count] = [i, j]
                count += 1
    return dicts

def printBoard(board):
    for floor in board:
        acu = ""
        for i in floor:
            acu += i
        print(acu)

def Insert(board, coord, count):
    char = ["O", "X"]
    cont = True
    while cont:
        Move = int(input(">> "))
        if Move != 0:
            loc = coord[Move]
            if board[loc[0]][loc[1]] == " ":
                board[loc[0]][loc[1]] = char[count % 2]
                cont = False
            else:
                print("Already taken")
        else:
            print("enter number from 1 - 9")
    return board

def check_taken(board, coord, slot):
    coord = [Coordinate for Coordinate in coord.values()]
    slot = [Coordinate for Coordinate in slot.values()]
    for i in slot:
        if i in coord:
            coord.remove(i)
    n = len(coord)
    taken = {}
    for i in range(n):
        taken[i+1] = coord[i]
    return taken

#check_taken(board)

def find_shape(board, coord):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if [i,j] == coord:
                shape = board[i][j]
    return shape

def horizontal_check(board, current_coord, shape):
    score = 0
    new_coord = current_coord.copy()
    for j in range(3):
        new_coord[1] += 2
        if new_coord[1] > 4:
            new_coord[1] = 0
        it_shape = find_shape(board, new_coord)
        if it_shape != shape:
            break
        else:
            score += 1
    return score

def vertical_check(board, current_coord, shape):
    score = 0
    new_coord = current_coord.copy()
    for j in range(3):
        new_coord[0] += 2
        if new_coord[0] > 4:
            new_coord[0] = 0
        it_shape = find_shape(board, new_coord)
        if it_shape != shape:
            break
        else:
            score += 1
    return score

def diagonal_check(board, current_coord, shape):
    score = 0
    new_coord = current_coord.copy()
    possible_coord = [[0,0], [4,0], [0,4], [4,4]]
    if new_coord in possible_coord:
        if new_coord == [0,0] or new_coord == [4,4]: #right diagonal
            for i in range(3):
                new_coord[0] += 2
                new_coord[1] += 2
                if new_coord[0] > 4:
                    new_coord[0] = 0
                if new_coord[1] > 4:
                    new_coord[1] = 0
                it_shape = find_shape(board, new_coord)
                if it_shape != shape:
                    break
                else:
                    score += 1
                    
        elif new_coord == [4,0] or new_coord == [0,4]: #left diagonal
            for i in range(3):
                new_coord[0] += 2
                new_coord[1] -= 2
                if new_coord[0] > 4:
                    new_coord[0] = 0
                if new_coord[0] < 0:
                    new_coord[0] = 4

                if new_coord[1] > 4:
                    new_coord[1] = 0
                if new_coord[1] < 0:
                    new_coord[1] = 4
                it_shape = find_shape(board, new_coord)
                if it_shape != shape:
                    break
                else:
                    score += 1
        
        return score
    else:
        return 0

def check_win(board, coord, current):
    score = 0
    st = False
    taken = check_taken(board, coord, current)
    run = True
    taken_coord = list(taken.values())
    count = 1
    while run:
        current_coord = taken_coord[0]
        shape = find_shape(board, current_coord)
        #Horizontal
        score = horizontal_check(board, current_coord, shape)
        #Vertical
        if score != 3:
            score = vertical_check(board, current_coord, shape)
            #Diagonal
            if score != 3:
                score = diagonal_check(board, current_coord, shape)
        taken_coord.pop(0)
        count += 1
        if not taken_coord:
            run = False
        if score == 3:
            run = False
            st = True
    if st:
        printBoard(board)
    return st, shape

def main(board):
    coord = lookCoord(board)
    count = 0
    game = True
    printBoard(board)
    while game:
        if count >= 5:
            st, shape_w = check_win(board, coord, newCoord)
            if st:
                print('"%s" win'%shape_w)
                break
        board = Insert(board, coord, count)
        printBoard(board)
        count += 1
        newCoord = lookCoord(board)
        if not newCoord:
            game = False
    if not st:
        print("\nTIE")
    print("Game Finished")


main(board)