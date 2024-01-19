# truncate sting

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(" ")
        S = s[0:k]
        return " ".join([str(i) for i in S]) 
