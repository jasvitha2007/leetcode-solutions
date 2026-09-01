class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        res=0
        for i in range(len(nums)):
            if(nums[i]==1):
                c+=1
            if nums[i]==0:
                c=0
            res=max(res,c)
        return res
            
        