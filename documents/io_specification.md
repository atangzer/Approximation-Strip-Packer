# Input/Output Specification



## Input Specification

​	The program first receives, in one line, two positive integers **W** and **N**, in that order, where **W** is the width of the texture atlas that the images will be packed into and **N** is the number of images to be packed.

​	The program then receives *N* lines of input. Each line specifies an images and contains two positive integers **w** and **h**, in that order, specifying the pixel width and height of the image, respectively.

## Output Specification

​	The program first outputs the total area used by the packing.

​	The program then outputs **N** lines, specifying the positions of the images in the texture atlas. Each line contains an ordered pair of non-negative integers **x** and **y**, in that order, specifying the x and y position of the bottom left pixel of the image in the texture atlas, respectively. The positions are output in the same order as the input sizes are input; that is, the i-th position in output corresponds to the i-th image in input. 

​	If the input width **w** of one or more of the images is less than 1, or greater than the texture atlas width **W**, "Invalid Input" is output and the program terminates.

## Examples

**Input 0:**

10 10
4 5
1 1
3 2
1 6
2 9
1 3
2 2
2 4
5 3
8 1

**Output 0:**

area=130

(3, 0)
(8, 12)
(7, 9)
(2, 0)
(0, 0)
(9, 0)
(5, 9)
(7, 0)
(0, 9)
(0, 12)

**Input 1:**

25 17
1 9
2 12
3 15
8 6
9 14
9 6
2 2
1 3
2 7
5 1
10 9
8 25
1 12
4 6
5 9
12 5
7 18

Time taken by program was 1572.000000 milliseconds

**Output 1:**

area=1375

(5, 39)
(10, 25)
(15, 0)
(0, 48)
(0, 25)
(12, 39)
(21, 48)
(20, 48)
(6, 39)
(0, 54)
(12, 25)
(0, 0)
(9, 25)
(8, 39)
(0, 39)
(8, 48)
(8, 0)

Time taken by program was 27.000000 milliseconds

**Input 2:**

1 3
5 2
4 3
1 6

**Output 2:**

Invalid Input