#description
#Given an input string, reverse the string word by word.
#reversed string should not contain leading or trailing spaces.
#For example,
#Given s = "the sky is blue",
#return "blue is sky the".

class Solution(object):
    # @param s, a string
    # @return a string
    
    def reverseWords(self, s):
        reversed_string = ''
        if s is None:
            print 'Null input string'
        
        word_list = s.split()
        if word_list:
            reversed_word_list = word_list[::-1]
            reversed_string =  ' '.join(reversed_word_list)
            
        return reversed_string 
