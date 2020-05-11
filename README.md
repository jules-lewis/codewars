# CodeWars

Repo for practicing CodeWar katas and storing solutions. This will also include incomplete kata for me to go back to. Code is in Python unless otherwise stated. The code contains a link back to the kata in CodeWars.

## [3 Kyu](https://github.com/jules-lewis/codewars/tree/master/3kyu)

### [Alphabetic Anagrams](https://github.com/jules-lewis/codewars/blob/master/3kyu/alphabetic-anagrams.py)  
Assign a number to every 'word', based on where it falls in an alphabetically sorted list of all words made up of the same group of letters. There is a performance test to prevent coders using brute force (this is essentially a mathematical problem).

### [Sudoku Solver](https://github.com/jules-lewis/codewars/blob/master/3kyu/sudoku-solver.py)  
Solver for 'easy' (i.e. determinable) Sudokus.


## [4 Kyu](https://github.com/jules-lewis/codewars/tree/master/4kyu)

### [Hamming Numbers](https://github.com/jules-lewis/codewars/blob/master/4kyu/hamming-numbers.py)
Algorithm to generate Hamming Numbers, otherwise known as Natural Numbers. There are three versions of the code in the module, but only the third version is fast enough to pass the *kata*. It uses set() to ensure that only unique Hamming Numbers are added to the list of calculated Hamming Numbers, otherwise 30 could be added three times, for example, as it is a multiple of 2, 3,, and 5. I've also cached calculated Hamming Numbers from previous calls so that if, for example `hamming(10)` is called, I now have the first 10 Hamming Numbers stored, in case the caller asks for `hamming(7)`. 

### [Ranking Poker Hands](https://github.com/jules-lewis/codewars/blob/master/4kyu/ranking-poker-hands.py)  
Fun challenge to rank poker hands in the format "AH 4C 7D 3C KS". Had already coded some of this years ago in Euler Problem 54, but the kata in CodeWars is to put the implementation in a class. Really enjoyed coding this.

### [Rail Fence Cipher](https://github.com/jules-lewis/codewars/blob/master/4kyu/rail-fence-cypher.py) 
The challenge is to encode and decode text using a fairly simple cipher that turns out to be a little harder to decode than I expected.



