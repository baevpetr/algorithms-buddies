# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opening_parentheses = ['(', '{', '[']
        closing_parentheses = [')', '}', ']']

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for parenthesis in s:
            if parenthesis in opening_parentheses:
                stack.append(parenthesis)
            elif parenthesis in closing_parentheses:

                if len(stack) == 0:
                    return False

                last_parenthesis = stack.pop()

                if pairs[parenthesis] != last_parenthesis:
                    return False

        if len(stack) > 0:
            return False

        return True
