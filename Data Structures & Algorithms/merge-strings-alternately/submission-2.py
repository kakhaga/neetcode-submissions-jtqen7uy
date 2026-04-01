class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n = len(word1), len(word2)
        res = []
        pt1, pt2 = 0,0

        while pt1 < m and pt2 < n:
            res.append(word1[pt1])
            res.append(word2[pt2])
            pt1 += 1
            pt2 += 1

        while pt1 < m:
            res.append(word1[pt1])
            pt1 += 1
            
        while pt2 < n:
            res.append(word2[pt2])
            pt2 += 1

        return "".join(res)