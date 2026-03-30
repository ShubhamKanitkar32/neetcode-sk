class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i, n in  enumerate(nums):
            for j, r in enumerate(res):
                if (i != j):
                    res[j] *= n
        
        return res