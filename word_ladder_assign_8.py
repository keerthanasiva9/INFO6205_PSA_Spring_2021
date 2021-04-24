#Word Ladder

#Given two words, beginWord and endWord, and a dictionary wordList,
# return the number of words in the shortest transformation sequence from beginWord to endWord,
# or 0 if no such sequence exists.

#Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
#Output: 5

#Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
#Output: 0

import collections
from collections import deque

def word_ladder(beginWord, endWord, wordList):
    queue = collections.deque([(beginWord, 1)])

    directions = dict()
    for i in range(len(beginWord)):
        directions[i] = set([w[i] for w in wordList])

    wordList = set(wordList)

    while queue:
        word, ct = queue.popleft()

        if word == endWord:
            return ct

        for i in range(len(word)):
            for char in directions[i]:
                newWord = word[:i] + char + word[i + 1:]
                if char != word[i] and newWord in wordList:
                    queue.append((newWord, ct + 1))
                    wordList.remove(newWord)
    return 0

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print("The begin word is :", beginWord)
    print("The end word is :",endWord)
    print("The word list is :", wordList)
    print("Output:",word_ladder(beginWord, endWord, wordList))