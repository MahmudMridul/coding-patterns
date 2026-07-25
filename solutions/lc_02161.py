# array two_pointers

from typing import List

class Solution:

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lc, ec, gc = 0, 0, 0
        li, ei, gi = 0, 0, 0
        result = [0] * len(nums)

        for num in nums:
            if num < pivot:
                lc += 1
            elif num == pivot:
                ec += 1
            else:
                gc += 1

        ei = lc
        gi = (lc + ec)

        for num in nums:
            if num < pivot:
                result[li] = num
                li += 1
            elif num == pivot:
                result[ei] = num
                ei += 1
            else:
                result[gi] = num
                gi += 1

        return result


    def pivotArray_v1(self, nums: List[int], pivot: int) -> List[int]:
        result = []

        for num in nums:
            if num < pivot:
                result.append(num)

        for num in nums:
            if num == pivot:
                result.append(num)

        for num in nums:
            if num > pivot:
                result.append(num)

        return result


solution = Solution()
output = solution.pivotArray([10,2,3,5,5,6], 4)
print(output)