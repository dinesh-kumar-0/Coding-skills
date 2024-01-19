# convert to lower case

class Solution:
    def toLowerCase(self, s: str) -> str:
        answerString = ""
        for i in s:
            if 'A' <= i <= 'Z':
                answerString = answerString + chr(ord(i)+32)
            else:
                 answerString = answerString + i

        return answerString
            
