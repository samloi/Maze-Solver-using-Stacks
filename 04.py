from Stack import Stack


def maze_path_exists(maze, start_x, start_y):
    stack = Stack()
    stack.push([start_x, start_y])
    progression = 1
    maze[start_x][start_y] = progression

    while not stack.isEmpty():
        present_x, present_y = stack.peek()

        #nrth
        if present_x - 1 >= 0 and (maze[present_x - 1][present_y] == ' ' or maze[present_x - 1][present_y] == 'G'):
            next_cell_x = present_x - 1
            next_cell_y = present_y
            next_cell_coordinates = [next_cell_x, next_cell_y]
            stack.push(next_cell_coordinates)
            if maze[next_cell_x][next_cell_y] == 'G':
                return True
            else:
                progression += 1
                maze[next_cell_x][next_cell_y] = progression
                continue

        #west
        if present_y - 1 >= 0 and (maze[present_x][present_y - 1] == ' ' or maze[present_x][present_y - 1] == 'G'):
            next_cell_x = present_x
            next_cell_y = present_y - 1
            next_cell_coordinates = [next_cell_x, next_cell_y]
            stack.push(next_cell_coordinates)
            if maze[next_cell_x][next_cell_y] == 'G':
                return True
            else:
                progression += 1
                maze[next_cell_x][next_cell_y] = progression
                continue

        #suth
        if present_x + 1 < len(maze) and (maze[present_x + 1][present_y] == ' ' or maze[present_x + 1][present_y] == 'G'):
            next_cell_x = present_x + 1
            next_cell_y = present_y
            next_cell_coordinates = [next_cell_x, next_cell_y]
            stack.push(next_cell_coordinates)
            if maze[next_cell_x][next_cell_y] == 'G':
                return True
            else:
                progression += 1
                maze[next_cell_x][next_cell_y] = progression
                continue

        #east
        if present_y + 1 < len(maze[0]) and (maze[present_x][present_y + 1] == ' ' or maze[present_x][present_y + 1] == 'G'):
            next_cell_x = present_x
            next_cell_y = present_y + 1
            next_cell_coordinates = [next_cell_x, next_cell_y]
            stack.push(next_cell_coordinates)
            if maze[next_cell_x][next_cell_y] == 'G':
                return True
            else:
                progression += 1
                maze[next_cell_x][next_cell_y] = progression
                continue

        #backtrack
        stack.pop()

    return False
