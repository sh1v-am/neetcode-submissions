class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        nums = [1, 2]

        for i in range(2, n):
            nums.append(nums[i-1] + nums[i-2])

        return nums[n-1]