from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []

        unique_numbers = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in unique_numbers:
                result.append(i)

        return result
