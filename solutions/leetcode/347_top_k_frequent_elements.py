# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []
        cnt = {}
        for el in nums:
            cnt[el] = cnt.get(el, 0) + 1
        # Heear could be done with heap: get top k elements from priority queue. What is a bit faster.
        return [item[0] for item in sorted(cnt.items(), key=lambda x:-x[1])][:k]
