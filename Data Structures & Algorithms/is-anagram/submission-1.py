class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap_s = {}
        hmap_t = {}
        for char_s in s:
            hmap_s[char_s] = hmap_s.get(char_s, 0) + 1
        for char_t in t:
            hmap_t[char_t] = hmap_t.get(char_t, 0) + 1
        print(hmap_s)
        print(hmap_t)
        for k_s in hmap_s:
            if k_s not in hmap_t or hmap_s[k_s] != hmap_t[k_s]:
                return False 
        for k_t in hmap_t:
            if k_t not in hmap_s or hmap_t[k_t] != hmap_s[k_t]:
                return False 
        return True  
        