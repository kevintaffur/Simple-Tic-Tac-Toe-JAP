def how_many_values(arr):
    x = 0
    o = 0
    no_value = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == "X":
                x += 1
            elif arr[i][j] == "O":
                o += 1
            elif arr[i][j] == " ":
                no_value += 1
    return x, o, no_value


def analyze(arr):
    x_won = False
    o_won = False
    for i in range(3):
        if ((arr[i][0] == arr[i][1] == arr[i][2] == "X") or
                (arr[0][i] == arr[1][i] == arr[2][i] == "X") or
                (arr[0][0] == arr[1][1] == arr[2][2] == "X") or
                (arr[0][2] == arr[1][1] == arr[2][0] == "X")):
            x_won = True

        if ((arr[i][0] == arr[i][1] == arr[i][2] == "O") or
                (arr[0][i] == arr[1][i] == arr[2][i] == "O") or
                (arr[0][0] == arr[1][1] == arr[2][2] == "O") or
                (arr[0][2] == arr[1][1] == arr[2][0] == "O")):
            o_won = True

    how_many_x, how_many_o, no_value = how_many_values(arr)

    if (x_won and o_won) or abs(how_many_x - how_many_o) > 1:
        print("Impossible")
        return False
    elif x_won:
        print("X wins")
        return False
    elif o_won:
        print("O wins")
        return False
    elif no_value > 0:
        return True
    else:
        print("Draw")
        return False


def init_grid(arr, values):
    index = 0
    for i in range(3):
        for j in range(3):
            arr[i][j] = values[index]
            index += 1

    return arr


def print_grid(arr):
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(arr[i][j], end=" ")

        print("|")
    print("---------")


def turn(player):
    row, column = input().split()

    try:
        row = int(row)
        column = int(column)
    except ValueError:
        print("You should enter numbers!")
        return player
    else:
        if (1 <= row <= 3) and (1 <= column <= 3):
            row -= 1
            column -= 1
            if grid[row][column] != "X" and grid[row][column] != "O":
                grid[row][column] = player
                print_grid(grid)
                if player == "X":
                    player = "O"
                elif player == "O":
                    player = "X"
                return player
            else:
                print("This cell is occupied! Choose another one!")
                return player
        else:
            print("Coordinates should be from 1 to 3!")
            return player


grid = [[" " for i in range(3)] for j in range(3)]

print_grid(grid)

player = "X"
running = True
while running:
    player = turn(player)
    running = analyze(grid)
