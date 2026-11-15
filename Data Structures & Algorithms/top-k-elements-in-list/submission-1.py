from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        freq = sorted(freq.items(), key=lambda item: item[1], reverse = True)
        ans = []
        for i in range(0, k):
            ans.append(freq[i][0])
        return ans