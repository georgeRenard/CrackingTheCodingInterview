import sys



def problem():
    """
    String Compression: Implement a method to perform basic string compression using the counts
    of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
    "compressed" string would not become smaller than the original string, your method should return
    the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
    """
    pass



def compress(string):
    
    prior_len = len(string)
    prior = string
    string = list(string)    
    __brute_force_inplace(string)    
    
    compressed_string = ''.join(string)

    return compressed_string if len(compressed_string) < prior_len else prior 



# This algorithm requires O(n) spaces and O(n) time where n is the length of the string being compressed
def __brute_force(string):

    compressedString = [] 
    
    prevCharacter = '' 
    i = 0
    for c in string:
       
        if prevCharacter == '':
            prevCharacter = c
            i = 1
            continue

        if c != prevCharacter: 
            compressedString.append(prevCharacter + str(i))
            prevCharacter = c
            i = 1
            continue
        
        i+=1
    
    compressedString.append(prevCharacter + str(i))
    string_after = ''.join(compressedString)   
 
    return string_after if (len(string_after) < len(string)) else string


# This function requires no additional space O(1) since it does everything in-place at the same time
# it preserves the desired O(n) runtime
# Unless the language has a way to allocate buffers, you cannot pretty much do better than this inplace algorithm (at least that is what I thin - and I might be wrong)
def __brute_force_inplace(string):
    
    i = 1
    prevCharacter = string[0]

    for j in range(1, len(string)):

        if prevCharacter != string[j]:

            if i != 1:
                string[j - 1] = str(i)

            prevCharacter = string[j]
            i = 1
            continue

        string[j] = ''
        i += 1
    
    string[-1] = str(i)    
    

if __name__ == '__main__':
    args = sys.argv[1:]
    string = args[0]
    compressedString = compress(string)
    print(compressedString)
