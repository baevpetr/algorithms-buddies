# https://leetcode.com/problems/valid-anagram/

from collections import Counter, dafaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1 Solved in 10 seconds
        return Counter(s) == Counter(t)

        # 2 Counting again...
        if len(s) != len(t):  # may check it in every solution
            return False

        for char in set(s):  # maybe it's better to generate set from shortest string
            if s.count(char) != t.count(char):
                return False
        return True

        # 3 With defaultdicts. Almost identical to the first solution, but
        tracker = defaultdict(int)
        for x in s: tracker[x] += 1
        for x in t: tracker[x] -= 1
        return all(x == 0 for x in tracker.values())
