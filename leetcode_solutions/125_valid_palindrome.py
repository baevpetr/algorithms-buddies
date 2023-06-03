# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 1.1 Dumb Python
        s_filtered = ''.join(map(str.lower, filter(str.isalnum, s)))
        return s_filtered == s_filtered[::-1]

        # 1.2 Prettier Dumb Python
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]

        # 2.1 Two Pointers
        head = 0
        tail = len(s) - 1

        while head <= tail:
            head_char = s[head]
            tail_char = s[tail]

            if not str.isalnum(head_char):
                head += 1
                continue

            if not str.isalnum(tail_char):
                tail -= 1
                continue

            if head_char.lower() != tail_char.lower():
                return False

            head += 1
            tail -= 1

        return True

        # 2.2 Prettier Two Pointers
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    i, j = i + 1, j - 1
                    continue
            i, j = i + (not a.isalnum()), j - (not b.isalnum())
        return True

        # 3 Regex
        import re

        s = re.sub(r"[^a-z0-9]", '', s.lower())
        return s == ''.join(reversed(s))
