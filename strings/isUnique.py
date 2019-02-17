import sys


# Brute-Force solution O(l^2) where l is the length of the passed string
def isUnique(sequence):
    for i in range(0, len(sequence)):
        for j in range(0, len(sequence)):
            if i == j:
                continue
            if sequence[i] == sequence[j]:
                return False

    return True

def isUniqueWithMap(sequence):
    
    m = {}
    for c in sequence:
	if c in m:
	    return False
        m[c] = 1

    return True


# This solution goes for O(n) where n is the size of the string
# and O(a) memory where a is the size of the alphabet
# here we assume ascii
def isUniqueWithBitVector(sequence):
    
    alphabet_size = 255
    bit_vector = 1 << (alphabet_size + 1)   
    
    for c in sequence:
        mask = ( 1 << ord(c) )
        if bit_vector & mask != 0:
            return False
        bit_vector |= (1 << ord(c)) 
    
    return True 


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception("The program expects 1 argument")

    if isUniqueWithBitVector(sys.argv[1]):
    	print("{0} has only distinct characters".format(sys.argv[1]))
    else:
	print("{0} has recurring characters".format(sys.argv[1]))
