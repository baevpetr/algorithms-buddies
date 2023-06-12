# https://leetcode.com/problems/3sum/description/
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i != 0 and v == nums[i-1]:
                    continue
                
            l = i+1
            r = len(nums)-1
            target = -v
            
            while l < r:
                if nums[l] + nums[r] == target:
                    res.add((v, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        
        return [[*items] for items in res]
