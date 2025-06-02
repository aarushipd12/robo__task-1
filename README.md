# robo__task-1
------(  Q1  )---------

We have used python list for (a)queue-(that stores coordinates of the same breadth/ level to be traversed) and, (b)DIRECTIONS-(that stores the direction vectors for up-down-left-right movement). Here, the grid was 5x5. 
Use of specific data structures can directly affect memory usage.
Basically, we want to increase efficiency (mainly- time efficiency, performance, memory usage)

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

