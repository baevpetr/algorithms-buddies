# https://leetcode.com/problems/binary-search/

from bisect import bisect_lefts


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        (left + right) >> 1

        l_nums = len(nums)

        # 1 bisect(_left)
        # https://stackoverflow.com/questions/212358/binary-search-bisection-in-python
        # https://docs.python.org/3/library/bisect.html#bisect.bisect_left
        pos = bisect_left(nums, target, 0, l_nums)
        return pos if pos != l_nums and nums[pos] == target else -1

        # 2.1 Ruined https://en.wikipedia.org/wiki/Bisection_method
        pos = l_nums // 2

        for n_hops in range(???):
            if nums[pos] == target:
                return pos

            if nums[pos] > target:
                pos = (l_nums - pos) // 2 (???)
            else:
                pos = (l_nums + pos) // 2 (???)

        return -1

        # 2.2 Iterative
        left, right = 0, l_nums - 1

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return -1

        # 3 Recurisve
        def bin_search(nums, target, left = 0, right = l_nums - 1):
            if left > right:
                return -1

            middle = (left + right) // 2
            if target == nums[middle]:
                    return middle
            elif target < nums[middle]:
                return bin_search(nums, target, left, middle - 1)
            else:
                return bin_search(nums, target, middle + 1, right)

        return bin_search(nums, target)
