beginWord = "hit"
endWord = "cog"
wordList = ["hit","dot","dog","lot","log","cog"]
def ladderLength(beginWord,endWord,wordList):
    l = len(wordList)
    cnt = l-1
    if(wordList[l-1]==endWord):
        if(wordList[0]==beginWord):
            cnt = cnt-1
    else:
        return 0
    return cnt
c = ladderLength(beginWord,endWord,wordList)
print(c)