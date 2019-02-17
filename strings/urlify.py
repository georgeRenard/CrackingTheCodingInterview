import sys




# Assumption 1 : We don't want to shuffle the original string -> Therefore, we exclude sorting
# Assumption 2 : We need to allocate +2 buffer size for each white space since %20 has 3 characters while a white space is a single byte character


# Question 1 : How do we find the value 32(whitespace) in the string
# Question 2 : What is the most efficient way to allocate more buffer size


def urlify(string, size):
         
    return __urlify(list(string), size)
    # return brute_force(string)



# This might be a better solution memory wise since it assumes that the string has some auxiliry space and does all the replacement inplace
def __urlify(string, size):
    
    for i in range(size - 1 , 0, -1):
        if string[i] == ' ':
            for j in range(len(string) - 1, i + 1, -1):
		string[j] = string[j-2]
 
            string[i] = '%'
            string[i+1] = '2'
            string[i+2] = '0'


    return ''.join(string)  


# This solution does O(n) operations at most and uses O(n) space
def brute_force(string):
   
    string = string.strip() 
    url = []
    char_buffer = list(string)
     
    for c in char_buffer:
        if ord(c) == 32:
            url.append("%20")    
        else:
            url.append(c)
     
    return ''.join(url) 




if __name__ == '__main__':
    args = sys.argv[1:]
    print(urlify(args[0], int(args[1]))) 
