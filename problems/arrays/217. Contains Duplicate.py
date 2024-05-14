from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_set = set()
        for n in nums:
            if n not in count_set:
                count_set.add(n)
            else:
                return True
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        unique_values = set(nums)
        if len(unique_values) != len(nums):
            return True
        return False