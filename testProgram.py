
class testProgram():

    def __init__(self, word):
        self.lenLongestWord = len(word)
        self.words = [word]
        self.longestWord = word
    
    def addWord(self, string):
        if (not isinstance(string, str)):
            raise TypeError('Added word is not a string')
        self.words.append(str(string))
        if len(string) > self.lenLongestWord:
            self.longestWord = string
            self.lenLongestWord = len(string)
                
        
    def getLongest(self):
        return self.longestWord

    def clear(self):
        self.words.clear()
        self.longestWord = ''
        self.lenLongestWord = 0
