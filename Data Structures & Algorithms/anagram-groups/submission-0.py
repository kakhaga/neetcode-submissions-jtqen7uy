class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            arr = [0]*26
            for i in s:
                arr[ord(i) - ord('a')] += 1
            dic[tuple(arr)].append(s)
        
        return [value for value in dic.values()]

            
