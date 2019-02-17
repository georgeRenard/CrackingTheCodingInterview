import sys


def arePermutations(left, right):
    
    # if encoding(left) != encoding(right) throw;

    # General base case
    if len(left) != len(right):
        return False

    # I am not completely sure that equal strings are not permutations of each other
    if left == right:
	return False

    return brute_force(list(left), right)
    #return xor_solution(left, right)


# Probably one of the worst case scenarios is to generate all the permutations of strig a/b and check against b/a to determine whether one is permutation of the other

# This brute_force does O(!n) computations
def brute_force(left, right):
    return generate_permutations(left, 0, len(left), right)
         

def generate_permutations(seq, start, end, match):

    if start == end:
        return match == ''.join(seq) 

    result = False
    for i in range(start, end):
        seq[i], seq[start] = seq[start], seq[i] 
        res = generate_permutations(seq,start + 1, end, match)
        result = result or res
        seq[i], seq[start] = seq[start], seq[i]
        
    return result

# This solution (if general) has runtime of O(n) and memory complexity of O(1)
# where n is the length of the strings (we do n computations only when the strings are of equal length)
def xor_solution(left, right):
    
    left_sum = sum([ord(c) for c in left])    
    right_sum = sum([ord(c) for c in right])
    return left_sum ^ right_sum == 0


if __name__ == '__main__':
    
    arguments = sys.argv[1:]
    result = arePermutations(arguments[0], arguments[1])
    print(result)    
