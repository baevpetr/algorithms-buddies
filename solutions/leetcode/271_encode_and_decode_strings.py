# https://leetcode.com/problems/encode-and-decode-strings/
# https://www.lintcode.com/problem/659/

import json
import pickle


class Solution_json:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        return json.dumps(strs)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, strs):
        return json.loads(strs)


strs = ["lint", "code", "love", "you"]
sol = Solution_json()
assert strs == sol.decode(sol.encode(strs))


class Solution_pickle:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        pass

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, strs):
        pass


strs = ["lint", "code", "love", "you"]
sol = Solution_pickle()
assert strs == sol.decode(sol.encode(strs))


class Solution_counter:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        pass

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, strs):
        pass


strs = ["lint", "code", "love", "you"]
sol = Solution_counter()
assert strs == sol.decode(sol.encode(strs))
