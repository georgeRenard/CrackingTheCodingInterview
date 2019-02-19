import sys






def problem():
    """
    One Away: There are three types of edits that can be performed on strings: insert a character,
    remove a character, or replace a character. Given two strings, write a function to check if they are
    one edit (or zero edits) away.

    EXAMPLE
        pale, ple -> true
        pales, pale -> true
        pale, bale -> true
        pale, bake -> false 
    """
    pass


# This function is O(n) where n is the length of the longer string
# and requires no additional memory to run O(1)
# Apparently, this is an optimal solution even though you might be able to optimized it in some way
# There might be some redundant or unnecessary code
def isOneAway(str1, str2):

    str1_len = len(str1)
    str2_len = len(str2)
    len_delta = abs(str1_len - str2_len)
 

    if len_delta > 1:
        return False

    longer_str = str1 if str1_len > str2_len else str2
    smaller_str = str1 if str1_len < str2_len else str2

    if smaller_str == longer_str:
        smaller_str = str1

    smaller_str_len = len(smaller_str)

    j = 0
    inconsistencies = 0
    for i in range(max(str1_len, str2_len)):
        
        c1 = longer_str[i]
        c2 = smaller_str[j] 

        if c1 == c2:
             j = j + 1 if i < smaller_str_len else j
             if j >= smaller_str_len:
                 j -= 1
             continue
        elif str1_len == str2_len:
             j += 1

        inconsistencies += 1

        if inconsistencies > 1:
            return False
        
    
    return False if inconsistencies > 1 else True   



if __name__ == '__main__':
    args = sys.argv[1:]
    result = isOneAway(list(args[0]), list(args[1]))
    print(result)
