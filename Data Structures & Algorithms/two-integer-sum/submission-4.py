class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={}

        for i,num in enumerate(nums):
            difference=target-num
            
            if difference in result:
                return [result[difference], i]
            result[num] = i

        return []