#Make an algorithm to find the longest palindrome that is a subsequence in a string

def find_palindrome(string):
    if string == string[::-1]:
        return string
    else:
        return max(find_palindrome(string[1:]), find_palindrome(string[:-1]), key=len)