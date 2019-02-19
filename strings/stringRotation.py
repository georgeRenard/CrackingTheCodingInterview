import sys
from time import time


def problem():
    """
    String Rotation:Assumeyou have a method isSubstringwhich checks if oneword is a substring
    of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
    call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat"). 
    """
    pass


# Example
# waterbottle -> left_circular_shift("waterbottle", 3) -> erbottlewat
# watteerrbbottle -> errbbottlewatte
# bottle -> lebott


# This function runs in O(h) where h is the length of the haystack (the supposed superstring)
def is_substring(needle, haystack):

    needle_len = len(needle)    

    i = 0
    for c in haystack:

        sub_c = needle[i]

        if c != sub_c:
            i = 0
            if i + 1 < needle_len and needle[i+1] == c:
                i += 1
            continue
        
        i += 1
        if i >= needle_len:
            return True


    return False 


def is_substring_optimized(haystack, needle, start, end):

    if start > end:
        return False

    i = 0
    j = 0 
    for c in haystack:
        j += 1 
        sub_c = needle[start + i]

        if c != sub_c:
            i = 0
            if start + i + 1 < end and needle[start + i + 1] == c and not needle[start + i + 1] == haystack[j]:
                i += 1
            continue
        
        i += 1

        if i + start >= end:
            return True


    return False

# This function runs in O(n) and requires O(n) memory
# The reason why I do it this way is because I am required to use the is_substring function atleast once
# Even then we could do some index manipulations in order to allow this function to require constant memory
def is_rotation(str1, str2):
    
    length = len(str1)

    if length != len(str2):
        return False 

    j = 0  
    x = []

    for i in range(length):
    
        c1 = str1[j]
        c2 = str2[i]
        equal = c1 == c2

        if not equal:
            x.append(c2)
        else:
            j += 1  
        
    return is_substring(''.join(x), str1)   
        

# I decided to implement the optimized version where we work with buffers instead of strings and we achieve O(1) memory
# while preserving the original O(n) runtime
def is_rotation_optimized(str1, str2):
 
    length = len(str1) 

    if length != len(str2):
        return False

    j = 0
    start = -1
    end = -1 
    for i in range(length):
    
        c1 = str1[j]
        c2 = str2[i]
        equal = c1 == c2
        
        if not equal:
            start = start if start != -1 else i  
        else:
            j += 1
            end = end if end != -1 else i 
             
    return is_substring_optimized(str1, str2, start, end)


# This solution is not mine
# Apparently, there is a way better solution that runs in O(1) and requires O(1) memory
def correct_solution(str1, str2):
    
    if len(str1) == len(str2):
        
       return is_substring(str1 * 2, str2)

 
    return False

def performance_test():
    
    long_str = """What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.

Where can I get some?
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
5paragraphs
	words
	bytes
	lists
	Start with 'Lorem
ipsum dolor sit amet...'"""
    rotated_str = """xt ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.

Where can I get some?
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
5paragraphs
        words
        bytes
        lists
        Start with 'Lorem
ipsum dolor sit amet...'""What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy te"""
    

    start = time()
    my_res = is_rotation_optimized(long_str, rotated_str) 
    end = time() 
    delta = end - start
    print("My solution finished in: {0}ms".format(delta))


    start = time()
    correct_solution_res = correct_solution(long_str, rotated_str)
    end = time()
    delta = end - start 

    print("The correct solution finished in: {0}ms".format(delta))


if __name__ == '__main__':

    args = sys.argv[1:]
    performance_test()
