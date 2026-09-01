class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res=[]
        ans=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                res.append(nums[i])
            else:
                ans.append(nums[i])
        return res+ans
        
        
        