class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        out = []
        i = 0
        while i < n:
            out.append(word1[i])
            out.append(word2[i])
            i += 1
        
        out.append(word1[i:])
        out.append(word2[i:])
        
        return "".join(out)
