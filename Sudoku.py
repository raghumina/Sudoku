# Sodoku in Python
# With help of backtracking



# Board to represent our problem
# Will work on board to solve problem
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def valid(bo,num,pos):
    # check row each row by sequence
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[i] != i:
            return False

    # to check coloumn

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3  # 3 becuse we are checking 3 by 3 box so that a numbe is not repeating itself.
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
            









def print_board(bo):
    for i in range(len(bo)):
        if i % 3 and i != 0:
            print("---------------")

    for j in range (len(bo[0])):
        print(" | ",end="")

        if j == 8:
            print(bo[i][j])
        else:
            print(str(bo[i][j] + "", end=""))

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j )  # row and column







