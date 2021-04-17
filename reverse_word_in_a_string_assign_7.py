#Reverse words in a string

#Given an input string s, reverse the order of the words.
#A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
#Return a string of the words in reverse order concatenated by a single space.

#Input: s = "the sky is blue"
#Output: "blue is sky the"

#Input: s = "  hello world  "
#Output: "world hello"
#Explanation: Your reversed string should not contain leading or trailing spaces.

def reverse_words(s):
    reversedlist = s.split()
    reversedlist = reversedlist[::-1]
    string = ""
    for word in reversedlist:
        string += word
        string += " "
    return string.strip()

if __name__ == '__main__':
    s = "the sky is blue"
    print("Input string is:",s)
    print("Output string is:",reverse_words(s))
