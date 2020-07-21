# Python

You have n number of locked boxes in front of you. Each box is numbered sequentially
from 0 to n - 1 and each box may contain keys to the other boxes.

Determines if all the boxes can be opened.

The boxes are a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
The first box is unlocked

Examples.
  X    X    X    X    X
[[1], [2], [3], [4], []]
  0    1    2    3   4

     X       X       X          X       X     X      X
[[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
     0       1       2          3       4      5     6

  X       X       X            X
[[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
   0      1       2       3    4     5       6
