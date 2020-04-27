"""

Sudoku Solver

URL: https://www.codewars.com/kata/sudoku-solver/python

Write a function that will solve a 9x9 Sudoku puzzle. The function 
will take one argument consisting of the 2D puzzle array, with the 
value 0 representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. 
determinable; there will be no need to assume and test possibilities 
on unknowns) and can be solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)
# Should return
         [[5,3,4,6,7,8,9,1,2],
          [6,7,2,1,9,5,3,4,8],
          [1,9,8,3,4,2,5,6,7],
          [8,5,9,7,6,1,4,2,3],
          [4,2,6,8,5,3,7,9,1],
          [7,1,3,9,2,4,8,5,6],
          [9,6,1,5,3,7,2,8,4],
          [2,8,7,4,1,9,6,3,5],
          [3,4,5,2,8,6,1,7,9]]

General thoughts

- I think this is going to be brute force for now, and 
  replicate how I solve easy and  moderate puzzles:

  > look at any given empty cell, and check what
    my options are in the current row, column, 
    and 'square'
  > if there is only one option, write this in
  > repeat

It would be helpful not to have to look up the column,
row, and 'square' indices every time I look at a
cell, so I will probably build these at the beginning.

I also don't think there's any need to persist with
a 2D array; we can use a single dimension array of 81
cells.

Each cell has:
 - a value: '0' or the solution
 - a set of other cells to look at

Let's do it!

"""

def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""

    flat_puzzle = flatten_puzzle(puzzle)

    lookups = create_lookups()
    #print(lookups)

    return None

def flatten_puzzle(puzzle):
    r = []
    for line in puzzle:
        r.extend(line)
    return r

def create_lookups():

    sq1 = [0, 1, 2, 9, 10, 11, 18, 19, 20]
    sq2 = [3, 4, 5, 12, 13, 14, 21, 22, 23]
    sq3 = [6, 7, 8, 15, 16, 17, 24, 25, 26]
    sq4 = [27, 28, 29, 36, 37, 38, 45, 46, 47]
    sq5 = [30, 31, 32, 39, 40, 41, 48, 49, 50]
    sq6 = [33, 34, 35, 42, 43, 44, 51, 52, 53]
    sq7 = [54, 55, 56, 63, 64, 65, 72, 73, 74]
    sq8 = [57, 58, 59, 66, 67, 68, 75, 76, 77]
    sq9 = [60, 61, 62, 69, 70, 71, 78, 79, 80]

    lookups = {}
    for i in range(81):
        lookups[i] = []
        row = i//9
        col = i%9
        #add rows and columns
        for j in range(81):
            #rows
            if (j//9 == row): lookups[i].append(j)
            #cols
            if (j%9 == col): lookups[i].append(j)
        #now add the squares
        sq = []
        if i in sq1: sq = sq1
        elif i in sq2: sq = sq2
        elif i in sq3: sq = sq3
        elif i in sq4: sq = sq4
        elif i in sq5: sq = sq5
        elif i in sq6: sq = sq6
        elif i in sq7: sq = sq7
        elif i in sq8: sq = sq8
        else: sq = sq9
        lookups[i].extend(sq)

        #tidy up: make sure we have no duplicates and
        #the cell isn't in its own lookup
        lookups[i] = list(set(lookups[i]))
        lookups[i].remove(i)
        print(len(lookups[i]))

    return lookups
            

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print(sudoku(puzzle))        