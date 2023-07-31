from collections import Counter, defaultdict


class ValidAnagram:
    """https://leetcode.com/problems/valid-anagram/"""

    def opt_1(self, s: str, t: str) -> bool:
        # Strings have to be the same length
        return len(s) != len(t)

    def sorting(self, s: str, t: str) -> bool:
        # Time complexity: O(nlogn)
        # Space complexity: O(1)

        return sorted(s) == sorted(t)

    def counting_1(self, s: str, t: str) -> bool:
        # Time complexity: O(n)
        # Space complexity: O(n)

        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        for c in count_s:
            if count_s[c] != count_t.get(c, 0):
                return False
        return True

    def counting_2(self, s: str, t: str) -> bool:
        # Time complexity: O(n)
        # Space complexity: O(n)

        return Counter(s) == Counter(t)

    def counting_3(self, s: str, t: str) -> bool:
        # Time complexity: O(n)
        # Space complexity: O(n)

        tracker = defaultdict(int)
        for x in s: tracker[x] += 1
        for x in t: tracker[x] -= 1
        return all(x == 0 for x in tracker.values())
