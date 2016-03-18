# Lasers
In this puzzle, you are given a grid of numbers, and a set of three-way lasers to place. Each laser is placed on one square of the grid and covers three of the four horizontally or vertically adjacent squares. Your goal is to cover the highest sum of numbers possible. Note that if two lasers shoot at the same square, you can count that value twice, but you cannot have two lasers centered on the same square. You also may not place a laser such that it would shoot outside the grid (this would be very dangerous to spectators!). 

The grid for the puzzle will be given to you in a file, simply as integers separated by
spaces. For example, the small puzzle from problem solving would be in a file with the
following contents:

3 4 7 9 <br>
2 5 1 4 <br>
3 3 2 3 <br>
5 6 8 7 <br>

Your code should prompt for a file name, read in the grid data, and then prompt for the
number of lasers to place. Your output should give the positions and orientations for the
solution — you may designate the four orientations any way that you wish as long as it
is clear. For the large example shown here, if we say that the laser “faces” the center of
the three squares being targeted, the output would look something like:

(6,1) facing west <br>
(5,6) facing north <br>
(5,2) facing north <br>
(1,3) facing east <br>

where the coordinates are (x,y) counting down form the top left with (0,0) the upper-leftmost
square.

