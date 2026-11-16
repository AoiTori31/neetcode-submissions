class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for num in nums:
            if num in hmap and hmap[num] >= 1:
                return True
            hmap[num] = hmap.get(num, 0) + 1
        return False