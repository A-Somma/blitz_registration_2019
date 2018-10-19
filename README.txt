Project for coveo blitz registration

Strategy for resolving problem is descibed below:

Let us define the following

Node:= An object representing a node of a 5x5 graph defined by it's (x,y) coordinates
Path:= An object representing series of commands of size n
p_i:= The ith command of a path  (0 <= i <= n)
u:= Up command, move up
d:= Down command, move down
l:= Left command, move left
r:= Right command, move right
?:= Wild card command, may be any command except f
f:= First command, indicates we are at the start of the path
dest:= Node representing the target destintion
start:= Node representing the starting position
out:= Node representing any position that is not within the graph
cursor:= Node representing the current position

Let us define the following recurrence

T(cursor, i):= A function of the cursor and the command number

Initial conditions

T(start, 0) = 0
T(cursor, 0) = -1 #if cursor != start
T(out, i) = -1

Recurrence

T(cursor, i) = T(cursor.move(p_i), i-1) #for p_i in {u, d, l, r}
T(cursor, i) = Max(T(cursor.move(u), i-1), T(cursor.move(d), i-1), T(cursor.move(l), i-1), T(cursor.move(r), i-1)) #for p_i = ?

Using the above recurrence it is possible to resolve the problem using dyanimc programming
If T(end, n) = 0 then a solution has been found
If T(end, n) = -1 Then no solution is possible