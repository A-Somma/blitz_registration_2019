Stub project for coveo blitz registration

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

T(cursor, p_i):= A function of the cursor and p_i command

Initial conditions

T(start, f) = 0
T(cursor, f) = -1 #if cursor != start
T(out, p_i) = -1

Recurrence

T(cursor, p_i) = T(cursor.move(p_i), p_(i-1)) #for p_i in {u, d, l, r}
T(cursor, p_i) = Max(T(cursor.move(u), p_(i-1)), T(cursor.move(d), p_(i-1)), T(cursor.move(l), p_(i-1)), T(cursor.move(r), p_(i-1))) #for p_i = ?

Using the above recurrence it is possible to resolve the problem using dyanimc programming
If T(end, p_n) = 0 then a solution has been found
If T(end, p_n) = -1 Then no solution is possible