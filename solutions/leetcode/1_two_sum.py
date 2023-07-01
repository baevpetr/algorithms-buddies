# https://leetcode.com/problems/two-sum/

# todo add brute force
# todo add reversed hash map

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for distance in range(1, len(nums)):
            for i in range(len(nums) - distance):
                if nums[i] + nums[i + distance] == target:
                    return [i, i + distance]
