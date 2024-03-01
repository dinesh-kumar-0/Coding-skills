class Solution:
    def minimumMoves(self, s: str) -> int:
        count=0
        i = 0
        while i<len(s):
            if s[i]=='O':
                i+=1
            else:
                i+=3
                count+=1
        return count
