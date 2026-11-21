class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        #[[1, 1], [2, 2], [3, 3]] -> [[3, 3], [2, 2], [1, 1]]로 소팅하고 k개만큼 앞에서 반환
        arr = list(freq.items())
        arr.sort(key=lambda pair: pair[1], reverse=True)
        return [num for num, count in arr[:k]]