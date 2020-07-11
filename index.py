myboard = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

                  
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)
    return None

def check(bo, position, num):
    #check the row first
    for i in range(len(bo[0])):
        if bo[position[0]][i] == num and position[1] != i:
            return False     
    #check the column
    for i in range(len(bo)):
        if bo[i][position[1]] == num and position[0] != i:
            return False    
    #check the square
    #find the square where the position is 
    n = position[1] // 3
    m = position[0] // 3
    for i in range(3* m, 3* m + 3):
        for j in range(3*n, 3*n + n):
            if bo[i][j] == num and (i,j) != position:
                return False
    return True

def solve(bo):
    f = find_empty(bo)
    if f == None:
        return True
    else:
        row, col = f

    for i in range(1,10):
        if check(bo,(row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0 #backtrack

    return False
    
print("Let's start solving!\n")               
print_board(myboard)
print("working on it...\n\n")
solve(myboard)
print("Here is the answer!")
print_board(myboard)

            
        