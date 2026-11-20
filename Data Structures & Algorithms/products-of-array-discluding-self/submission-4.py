class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,    1, 1x2, 1x2x4]
        # [2x4x6,4x6, 6,   1]
        left = [1]*len(nums)
        right = [1]*len(nums)
        curr = 1
        ans = [0]*len(nums)
        for i in range(len(nums)-1):
            curr = curr * nums[i]
            left[i+1] = curr

        curr = 1
        for i in range(len(nums)-1, 0, -1):
            curr = curr * nums[i]
            right[i-1] = curr

        # right = right[::-1]

        for i in range(len(nums)):
            ans[i] = left[i] * right[i]

        return ans