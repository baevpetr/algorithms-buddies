# https://leetcode.com/problems/product-of-array-except-self/

# https://www.youtube.com/watch?v=tSRFtR3pv74
# https://www.youtube.com/watch?v=bNvIQI2wAjk

from functools import reduce
from operator import mul


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. Anyway I want ot use division op! Ruined for lists with 0
        # O(2 * n) for sure :clown_face:
        product = reduce(mul, nums)
        return [product / num for num in nums]

        # 2. 2 prefix-sum (mul) lists. O(3 * n)
        # Instead of additional indices may use pre-/postfix variables
        # and initialize results as a list with ones.
        result = []
        lefties = [1]
        righties = [1]

        for num in nums:
            lefties.append(lefties[-1] * num)
        lefties.append(1)

        for num in reversed(nums):
            righties.append(righties[-1] * num)
        righties.append(1)
        righties.reverse()

        for idx in range(1, len(nums) + 1):
            result.append(lefties[idx - 1] * righties[idx + 1])

        return result

        # 3. 1 prefix-sum (mul) list & accumulator. O(3 * n)
        # Instead of additional indices may use pre-/postfix variables
        # and initialize results as a list with ones.
        result = []
        lefties = [1]

        for num in nums:
            lefties.append(lefties[-1] * num)
        lefties.append(1)

        acc = 1
        for idx in range(len(nums) - 1, -1, -1):
            result.append(lefties[idx] * acc)
            acc *= nums[idx]

        return reversed(result)
