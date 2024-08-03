class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in nums:
            nums_set.add(i)
        
        # print(len(nums_set))
        # print(len(nums))
        if len(nums_set) == len(nums):
            return False
        else:
            return True