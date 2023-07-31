class LongestConsecutiveSequence:
    """https://leetcode.com/problems/longest-consecutive-sequence/"""

    def using_set(self, nums: list[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        nums_set = set(nums)
        longest_streak = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
