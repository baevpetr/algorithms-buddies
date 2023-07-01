# https://leetcode.com/problems/car-fleet/


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions = position
        speeds = speed

        cars = [[p, s] for p, s in zip(positions, speeds)]

        stack = []
        for p, s in sorted(cars, reverse=True):
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
