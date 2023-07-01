# https://leetcode.com/problems/group-anagrams/

# https://www.youtube.com/watch?v=vzdNOK2oB2E

from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Sorting. m*log(n)
        result = defaultdict(list)

        for s in strs:
            result[''.join(sorted(s))].append(s)

        return result.values()

        # 2. Count using ordial. m * n * 26
        result = defaultdict(list)

        for s in strs:
            counter = [0] * 26  # a ... z

            for char in s:
                counter[ord(char) - ord('a')] += 1

            result[tuple(counter)].append(s)

        return result.values()

        # 3. Freeze Counter.  m * n * 26
        result = defaultdict(list)

        for s in strs:
            counter = Counter(s)
            frozen_counter = frozenset(dict(counter).items())
            result[frozen_counter].append(s)

        return result.values()
