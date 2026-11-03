class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count=set()

        for num in nums:
            if num not in count:
                count.add(num)
            else:
                return True
        else:
            return False