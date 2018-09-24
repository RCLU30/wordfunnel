#! python 3
"""
/r/dailyprogrammer exercise 366
# source: https://www.reddit.com/r/dailyprogrammer/comments/98ufvz/20180820_challenge_366_easy_word_funnel_1/
import os
"""

def funnel(arg1, arg2):
    """
Input: two strings, 2nd string is the word to be found in the first
string by removing a single letter from the first string
Output: true if the 2nd word is found inside the first word, false otherwise
    """
    word1 = list(arg1)
    word2 = list(arg2)
    removedletter = False

    #checking lengths of words
    if len(word1) > len(word2) + 1 or len(word2) > len(word1):
        return False
    for index, letter in enumerate(word2):
        if word1[index] != letter:
            if word1[index+1] == letter:
                if removedletter:
                    return False
                del word1[index]
                removedletter = True
    return True

# bonus exercise
def letter_removal(string, text):
    """
    Input: a single string, and the name of the name of the textfile
    Output: a list of words found in the text file formed by removing a
    single letter from the first string argument
    """
    textfile = open(text, 'r')
    wordlist = [] # list of words from the file
    foundWords = [] #list of found words
    # create a list of words
    for word in textfile:
        wordlist.append(word.rstrip())
    # iterate through list, search for word
    for index, letter in enumerate(string):
        slicedword = string[0:index] + string[index+1:]
        if slicedword in wordlist and slicedword not in foundWords:
            foundWords.append(slicedword)
    return foundWords

# print(funnel("leave", "eave"))
# print(funnel("reset", "rest"))
# print(funnel("dragoon", "dragon"))
# print(funnel("eave", "leave"))
# print(funnel("sleet", "lets"))
# print(funnel("skiff", "ski"))

print(letter_removal('boats', "enable1.txt"))
