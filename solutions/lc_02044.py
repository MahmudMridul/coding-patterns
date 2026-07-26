# array bracktracking

from typing import List

class Solution:

    def __init__(self) -> None:
        self.count = 0

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_val = 0

        for num in nums: 
            max_or_val |= num

        self._create_subsets(nums, 0, max_or_val, 0)
        return self.count

    def _create_subsets(self, nums: list[int], current: int, max_or_val: int, or_val: int):
        if current == len(nums):
            if or_val == max_or_val:
                self.count += 1
            return
        self._create_subsets(nums, current + 1, max_or_val, or_val)
        self._create_subsets(nums, current + 1, max_or_val, or_val | nums[current])


nums = [3,3,3]

solution = Solution()

result = solution.countMaxOrSubsets(nums)
print(result)