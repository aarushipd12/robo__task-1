#Maze-Task
'''Direction list: for traversing Up, Down, Left, Right, each tuple corresponds to the direction of motion'''
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(grid, start, goal):
    #List definition for bfs
    queue = [start]
    #Dictionary to stor visited nodes and their previous nodes
    visited = {start: None}

    while queue:
        #Remove the first node(coordinate, tuple) from the list queue
        current = _____.pop(0)
        #Once we have reached the goal, break out of the loop
        if current == goal:
            break

    #Check motion across all possible directions (Up, Down, Left, Right)
    for direction in DIRECTIONS:
        #Calculate the new position
        new_row = current[0] + direction[0]
        new_col = current[1] + direction[1]

        new_position = (new_row, new_col)
    
    #Check if new position is within bounds(grid dimensions) and not an obstacle
    if (0 <= new_row < len(grid)) and (0 <= new_col < len(grid[0])) and grid[new_row][new_col] == 0:
        #Check if the position has not been visited yet
        if new_position not in visited:
            #Mark it as visited and append the position to the list
            visited[new_position] = _____
            _____.append(new_position)
            #Reconstruct the path from the goal to the start
            path = []
            step = goal
    while step is not None:
        path.append(step)
        step = ______.get(step)
        #Return the path
        return path

#Occupancy grid (0 is a free space, 1 is an obstacle)
grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
    ]
#Starting and goal positions
start = (0, 0)
goal = (4, 4)
#Call the BFS function and print the actual path(from start to end)
path = bfs(grid, start, goal)
print("Path from start to goal: ", _______)


