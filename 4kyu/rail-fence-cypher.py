"""
Rail Fence Cipher: Encoding and Decoding

URL: https://www.codewars.com/kata/58c5577d61aefcf3ff000081/train/python

Create two functions to encode and then decode a string using the Rail 
Fence Cipher. This cipher is used to encode a string by placing each 
character successively in a diagonal along a set of "rails". First 
start off moving diagonally and down. 

When you reach the bottom, reverse direction and move diagonally and 
up until you reach the top rail. Continue until you reach the end of 
the string. Each "rail" is then read left to right to derive the encoded 
string.

For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented 
in a three rail system as follows:

W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C  
    A       I       V       D       E       N    

The encoded string would be:

WECRLTEERDSOEEFEAOCAIVDEN

Write a function/method that takes 2 arguments, a string and the number 
of rails, and returns the ENCODED string.

Write a second function/method that takes 2 arguments, an encoded string 
and the number of rails, and returns the DECODED string.

For both encoding and decoding, assume number of rails >= 2 and that 
passing an empty string will return an empty string.

Note that the example above excludes the punctuation and spaces just for 
simplicity. There are, however, tests that include punctuation. Don't 
filter out punctuation as they are a part of the string.

(1)

My first attempt can be seen in encode_clumsy() below. The
method is simply to step through <string>, adding each character to
a list, with one list per rail, but this doesn't feel very efficient. 
Also, it left me with no idea how to decode!?

(2)

Eventually I did a bit of reading and came across a comment on decoding
that basically said you've got to create the rails, and then populate
them with the ciphertext in order to decode it.

This got me thinking that it would be a lot better if the representation
of the rails was done in a 'one dimensional' structure, rather than an
'n-dimensional' structure where 'n' is the number of rails. This is what 
I had implemented in encode_clumsy(), with one list per rail. 

Eventually I realised I could use an object with two elements to represent 
each letter in the text, with on element being a representation of the
'rail' and the other to hold the text that is being encoded / decoded.

For example, to encode the eleven character text "HELLO WORLD" with three
rails, I would just create an 'empty' grid of eleven 'cells', with the
first element in each being the rail number:

+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 2 | 3 | 2 | 1 | 2 | 3 | 2 | 1 | 2 | 3 |
+---+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+---+

This could simply be a list of lists:

encode_grid = [
    [1, ""],
    [2, ""],
    [3, ""],
    [2, ""],
    [1, ""],
    [2, ""],
    ... etc.
]

I would then fill the second element in each 'cell' with the plaintext:

+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 2 | 3 | 2 | 1 | 2 | 3 | 2 | 1 | 2 | 3 |
+---+---+---+---+---+---+---+---+---+---+---+
| H | E | L | L | O | _ | W | O | R | L | D |
+---+---+---+---+---+---+---+---+---+---+---+

encode_grid = [
    [1, "H"],
    [2, "E"],
    [3, "L"],
    [2, "L"],
    [1, "O"],
    [2, " "],
    ... etc.
]

I would then pull out all the '1's (i.e. the first rail), then the 
'2's etc.:

H, O, R ... E, L, _, O, L ... L, W, D

Which gives us the correct ciphertext "HOREL OLLWD"

Decoding would work in a similar way:

  (i) create a one-dimensional grid the length of the ciphertext
 (ii) use the first characters in the ciphertext to populate
      the first 'rail'
(iii) populate each next 'rail' until you get to the end

So to decode "HOREL OLLWD" as a three rail ciper, start with an
eleven character grid, marked up for three rails:

+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 2 | 3 | 2 | 1 | 2 | 3 | 2 | 1 | 2 | 3 |
+---+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+---+

Use the first characters in the ciphertext to fill out the
first rail:

+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 2 | 3 | 2 | 1 | 2 | 3 | 2 | 1 | 2 | 3 |
+---+---+---+---+---+---+---+---+---+---+---+
| H |   |   |   | O |   |   |   | R |   |   |
+---+---+---+---+---+---+---+---+---+---+---+

Then add the next characters to the second 'rail':

+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 2 | 3 | 2 | 1 | 2 | 3 | 2 | 1 | 2 | 3 |
+---+---+---+---+---+---+---+---+---+---+---+
| H | E |   | L | O | _ |   | O | R | L |   |
+---+---+---+---+---+---+---+---+---+---+---+

Then continue through the rails until you run out of 'cells'!

"""

def encode_rail_fence_cipher(string, n_rails):

    #Make a grid the length of the string, marked up with
    #the rail values.
    grid = make_grid(len(string), n_rails)

    
    #Fill the grid with the string
    for i in range(len(string)):
        grid[i][1] = string[i]

    #Pull out the encoded text, rail by rail
    rtn = []
    for i in range(n_rails):
        rtn.extend([cell[1] for cell in grid if cell[0] == i])
    return "".join(rtn)
    
def decode_rail_fence_cipher(string, n_rails):

    #Make a grid the length of the string, marked up with
    #the rail values.
    grid = make_grid(len(string), n_rails)

    #Use the ciphertext to populate the grid, rail by rail
    string_index = 0
    for i in range(n_rails):
        for cell in grid:
            if cell[0] == i:
                cell[1] = string[string_index]
                string_index += 1

    #Pull out the cells in order -- should be the decoded text!
    return "".join(cell[1] for cell in grid)
    
def make_grid(length, rails):

    grid = []
    current_rail = 0

    #remember if we are going up the rails or down
    #  1 means up
    # -1 means down
    direction = 1

    for i in range(length):
        
        #populate a new cell
        grid.append([current_rail, ""])
        current_rail += direction
        
        #change direction if necessary
        if (current_rail == 0) and (direction == -1): direction = 1
        if (current_rail == rails-1) and (direction == 1): direction = -1

    return  grid

def encode_clumsy(string, n_rails):

    '''
    My first thought is to simply step through <string>, adding
    each character to  a list, with one list per rail, but
    this doesn't feel very efficient. Maybe it's performant 
    anyway?
    '''
    rails = []
    for i in range(n_rails):
        rails.append([])

    current_rail = 0

    #remember if we are going up the rails or down
    #  1 means up
    # -1 means down
    direction = 1

    for c in string:
        rails[current_rail].append(c)
        current_rail += direction
        
        #change direction if necessary
        if (current_rail == 0) and (direction == -1): direction = 1
        if (current_rail == n_rails-1) and (direction == 1): direction = -1

    rtn = ""
    for rail in rails:
        rtn += "".join(rail)

    return rtn

    #having got here, I realise I have no straightforward way to decode!


print(encode_clumsy("hello there sexy boy", 3))
print(encode_clumsy("abcdefghijklmnopqrstuvwxyz", 4))
print(make_grid(11, 3))
print(make_grid(20, 5))
print(encode_rail_fence_cipher("hello there sexy boy", 3))
print(decode_rail_fence_cipher("hoes el hr eybyltexo", 3))
print(encode_rail_fence_cipher("abcdefghijklmnopqrstuvwxyz", 4))
print(decode_rail_fence_cipher("agmsybfhlnrtxzceikoquwdjpv", 4))
