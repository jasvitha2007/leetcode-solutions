class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        even=0
        odd=1
        for i in nums:
            if i%2==0:
                res[even]=i
                even+=2
            else:
                res[odd]=i
                odd+=2
        return res

            
        