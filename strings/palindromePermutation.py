import sys
import math


def isPalindromePermutation(string):

    if string == None or string == '':
        raise Exception("Invalid arguments")

    string = string.upper()

    #return brute_force(string)
    return __optimized(string)


# This is a hyperoptimized version of the algorithm
# It takes no additional memory to perform O(1) memory
# The runtime complexity is around O(n) where n is the length of the string
def __optimized(string):

    bit_vector = 0 

    for c in string:
        c_ord = ord(c)
        if c_ord >= 65 and c_ord <= 90:
            bit_vector ^= (1 << (c_ord - 65))

    if math.log(bit_vector, 2).is_integer():
        return True
    
    return bit_vector == 0


# This brute-force is awful, it goes around generating all the possible permutations O(!n) and then tests each permutation for palindrome positivity with O(n) runtime and O(n) memory complexity 
def brute_force(string):
    return __brute_force(list(string), 0, len(string))


def __brute_force(a, begin, end):

    if begin == end:
        is_palindrome = isPalindrome(a)
        return is_palindrome   

    res = False

    for i in range(begin, end):
        a[i], a[begin] = a[begin], a[i]
        res = res or __brute_force(a, begin + 1, end)
        a[i], a[begin] = a[begin], a[i]

    return res 

# ------------------FIXED----------------------
# TODO: fix for this particular case "taco cat"
# ---------------------------------------------
# This function will probably run in O(n) with no additional space required
# In order to accomodate the case where we have two or more words with space in between
# we need to do O(n + n) with O(n) additional memory
def isPalindrome(string):


    string = strip_non_alphabet_chars(string)

    size = len(string) 
    bw_i = size - 1

    for i in range(0, size):

        left = string[i]
        right = string[bw_i]
        if left != right:
            return False
 
        bw_i -= 1 

    return True


def strip_non_alphabet_chars(string):
    
    new_string = []
    for c in string:
        ord_c = ord(c)
        if ord_c >= 65 and ord_c <= 90:
            new_string.append(c)     

    return ''.join(new_string)


if __name__ == '__main__':
    arguments = sys.argv[1:]
    print(isPalindromePermutation(arguments[0])) 
