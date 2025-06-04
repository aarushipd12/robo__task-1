#Maze-Task: HOW CAN A LESSER DISTANCE PATH BE OBTAINED??
from collections import deque

#Direction list: for traversing Up, Down, Left, Right, each tuple corresponds to the direction of motion
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#For traversing diagonally
DIRECTIONS_DIAG = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
def bfs(grid, start, goal):
    #DEQUE definition for bfs
    queue = deque([start])
    #Dictionary to store visited nodes and their previous nodes
    visited = {start: None}

    while queue:
        #Remove the first node(coordinate, tuple) from the DEQUE queue
        current = queue.popleft()
        #Once we have reached the goal, break out of the loop
        if current == goal:
            break

        #Check motion across cardinal directions (Up, Down, Left, Right)
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
                    visited[new_position] = current
                    queue.append(new_position)


        #Diagonal directions (allowed only if both adjacent sides are free)    
        for direction in DIRECTIONS_DIAG:
            new_row = current[0] + direction[0]
            new_col = current[1] + direction[1]
            new_position = (new_row, new_col)                     
            #Check if new position is within bounds(grid dimensions) and not an obstacle
            if (0 <= new_row < len(grid)) and (0 <= new_col < len(grid[0])) and grid[new_row][new_col] == 0:
                # Check both adjacent cells for obstacles
                adj1 = (current[0], new_col)
                adj2 = (new_row, current[1])
                 #Check if adjacent position is within bounds(grid dimensions) and not an obstacle
                if (0 <= adj1[0] < len(grid)) and (0 <= adj1[1] < len(grid[0])) and \
           (0 <= adj2[0] < len(grid)) and (0 <= adj2[1] < len(grid[0])) and \
           (grid[adj1[0]][adj1[1]] == 0 or grid[adj2[0]][adj2[1]] == 0):

                    #Check if the position has not been visited yet
                    if new_position not in visited:
                        #Mark it as visited and append the position to the list
                        visited[new_position] = current
                        queue.append(new_position)
    #Reconstruct the path from the goal to the start
    path = []
    step = goal
    while step is not None:
        path.append(step)
        step = visited.get(step)
    path.reverse()
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
print("Path from start to goal: ", path)

'''
OUTPUT:
Path from start to goal:  [(0, 0), (0, 1), (1, 2), (2, 1), (3, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
'''
