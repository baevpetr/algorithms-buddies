class ContainsDuplicate:
    """https://leetcode.com/problems/contains-duplicate/"""

    def brutforce(self, nums: list[int]) -> bool:
        # Time complexity: O(n^2)
        # Space complexity: O(1)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def sorting(self, nums: list[int]) -> bool:
        # Time complexity: O(nlogn)
        # Space complexity: O(1)

        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    def hashset(self, nums: list[int]) -> bool:
        # Time complexity: O(n)
        # Space complexity: O(n)

        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

    def lengths(self, nums: list[int]) -> bool:
        # Time complexity: O(n)
        # Space complexity: O(n)

        return len(set(nums)) != len(nums)
