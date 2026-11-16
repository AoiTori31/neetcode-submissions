class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c)-97] += 1
            if str(freq) in hmap: # update val
                hmap[str(freq)].append(s)
            else: hmap[str(freq)] = [s]
        arr = []
        for i, v in hmap.items():
            arr.append(v)
        return arr