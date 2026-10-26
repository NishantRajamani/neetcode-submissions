class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for item in nums:
            print(item,"\n")
            if item in my_dict.keys():
                return True
            else:
                my_dict[item] = 1
        return False

        