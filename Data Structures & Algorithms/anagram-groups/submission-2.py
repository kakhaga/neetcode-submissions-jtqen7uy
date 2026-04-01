class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map[list(len-26)] = list(strs)

        anagrams = defaultdict(list)

        for word in strs:
            arr = [0]*26
            for w in word:
                arr[ord(w)-ord('a')] += 1
            
            anagrams[tuple(arr)].append(word)
        return list(anagrams.values())