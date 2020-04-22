'''
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

'''

def encode_rail_fence_cipher(string, n_rails):

    return encode_1_clumsy(string, n_rails)
    
def decode_rail_fence_cipher(string, n_rails):

    pass

def encode_1_clumsy(string, n_rails):

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


print(encode_1_clumsy("hello there sexy boy", 3))

print(encode_1_clumsy("abcdefghijklmnopqrstuvwxyz", 4))
