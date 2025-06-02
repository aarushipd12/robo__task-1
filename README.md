# robo__task-1
------(  Q1  )---------
\n
We have used python list for (a)DIRECTIONS and, (b)variable queue (that stores coordinates of the same breadth/ level to be traversed). Here, the grid was 5x5. 
Use of specific datatypes can directly affect memory usage.
\n
(a)If the grid is larger (10x10), we can change the DIRECTIONS datatype from list to set. This increases time efficiency. Moreover, it need not be ordered, hence a set can be used. When tested and run for a 10x10 grid, as a list- elapsed time was 0.0372 sec, BUT as a set- elapsed time was 0.0227 sec. When the grid is much larger, these time gaps can increase, causing a significant difference.
Sets provide faster traversing, generally use less memory than lists when storing unique items. Though it uses higher initial memory overhead, because they use hash tables for fast lookups.
\n
(b)
