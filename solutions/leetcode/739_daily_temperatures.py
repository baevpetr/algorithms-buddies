# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
        # задудосили на массиве [47] * 100000000...
        # temperatures.append(0)
        # wait = []
        # for i in range(len(temperatures) - 1):
        #     cnt = 0
        #     while True:
        #         if (i + cnt) > len(temperatures) - 1:
        #             wait.append(0)
        #             break
        #         if temperatures[i] < temperatures[i + cnt]:
        #             wait.append(cnt)
        #             break
        #         cnt += 1
        # return wait

        stack = [0]
        res = [0] * len(temp)
        for idx in range(len(temp)):
            while stack and temp[stack[-1]] < temp[idx]:
                index = stack.pop()
                res[index] = idx - index
            stack.append(idx)
        return res
