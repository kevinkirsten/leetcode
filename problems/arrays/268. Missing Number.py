from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        max_n = max(nums)

        nums_set = set(nums)

        for i in range(0, max_n + 1):
            if i not in nums_set:
                return i

        return max_n + 1


sol = Solution()
nums = [3, 0, 1]
print(sol.missingNumber(nums))

nums = [0, 1]
print(sol.missingNumber(nums))

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(sol.missingNumber(nums))

nums = [1]
print(sol.missingNumber(nums))
