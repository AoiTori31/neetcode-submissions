class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d_num = {index: value for index, value in enumerate(nums)}
        arr = []
        print(d_num)
        for i1, v2 in d_num.items():
            diff = target - d_num.get(i1)
            for i2, v2 in d_num.items():
                if i2 == i1:
                    continue
                if diff == d_num.get(i2):
                    arr.append(i1)
                    arr.append(i2)
                    return arr
                
        
            