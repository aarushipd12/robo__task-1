# robo__task-1
------(  Q1  )---------

We have used python list for (a)queue-(that stores coordinates of the same breadth/ level to be traversed) and, (b)DIRECTIONS-(that stores the direction vectors for up-down-left-right movement). Here, the grid was 5x5. 
Use of specific data structures can directly affect memory usage.
Basically, we want to increase efficiency (mainly- time efficiency, performance, memory usage) as grid size increases.

(a)In 'queue', storing data as a list can rather be made from a specialized data structure- deque(DOUBLE- ENDED QUEUE). It is a specialized data structure, specific for Queue(that works on FIFO model) that has a pointer at both ends- front and rear. Thus, appending or removing items from a deque is much faster. So time efficiency increases. 
The main plus point that makes deque better than lists, **here**, is when we need to remove the first node(coordinate, tuple) from queue. When it is a list, we use the .pop(0) function, which involves returning the first node and shifting all rest of the elements to the immediate left index. But, when it is a deque, we use the .popleft() function which makes it much faster because a deque is implemented as a doubly linked list, so removing from either end is always fast and does not require the shifting of elements. Deque is best for faaster queue or stack operations and hence the choice. 

When the code was run for a 10x10 grid:

Using list:
  Elapsed time: 0.000148 seconds

Using deque:
  Elapsed time: 0.000068 seconds

And, both gave the same path. Hence, using list required more than twice the time reuired using deque.
This gap will keep increasing with increase in grid size.

(b)If the grid is larger (10x10), DIRECTIONS may also be stored in the built-in data structure, sets, which have faster traversing across its elements, and are unordered which is also not a problem for DIRECTIONS , as it only stores the direction vectors for up-down-left-right movement.



(------Q2-------)

Breadth first search (bfs) is an algorithm which is most suited for searching for the shortest path in unweighted graphs. Thus, it is most suited for such maze solving. In real world applications, in case of a maze solver mouse trying to exit from a maze using the bfs algorithm, it will have to store information about all possible directions at each node, hence first discovering all possiblities at each breadth/level. This requires more memory to store informations of all nodes at current depth before moving to the next node.

Moreover, in my opinion, in a very large and dense maze, it can become very complex and hence slower, as it stores memory of all nodes at a depth level.




(-------Q3------)

new_row = current[0] + direction[0]

new_col = current[1] + direction[1]

new_position = (new_row, new_column)

To ensure that the mouse traverses lesser distance we can make the following changes:-

DIRECTIONS= [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

Running the code after modification, we get the shortest distance path:

Output;
Path from start to goal:  [(0, 0), (0, 1), (1, 2), (2, 1), (3, 0), (4, 1), (4, 2), (4, 3), (4, 4)]




























