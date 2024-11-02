def is_can_exit_from_maze(arr, row, col, move=""):
    if arr[row][col] == 'E':
        return True
    elif arr[row][col] == '#':
        return False
    else:
        if move == "up":
            return (is_can_exit_from_maze(arr, row + 1, col, "up") or
                    is_can_exit_from_maze(arr, row, col - 1, "left") or
                    is_can_exit_from_maze(arr, row, col + 1, "right"))
        elif move == "down":
            return (is_can_exit_from_maze(arr, row - 1, col, "down") or
                    is_can_exit_from_maze(arr, row, col - 1, "left") or
                    is_can_exit_from_maze(arr, row, col + 1, "right"))
        elif move == "left":
            return (is_can_exit_from_maze(arr, row + 1, col, "up") or
                    is_can_exit_from_maze(arr, row, col - 1, "left") or
                    is_can_exit_from_maze(arr, row - 1, col, "down"))
        elif move == "right":
            return (is_can_exit_from_maze(arr, row + 1, col, "up") or
                    is_can_exit_from_maze(arr, row, col + 1, "right") or
                    is_can_exit_from_maze(arr, row - 1, col, "down"))
        else:
            return (is_can_exit_from_maze(arr, row + 1, col, "up") or
                    is_can_exit_from_maze(arr, row - 1, col, "down") or
                    is_can_exit_from_maze(arr, row, col - 1, "left") or
                    is_can_exit_from_maze(arr, row, col + 1, "right"))

