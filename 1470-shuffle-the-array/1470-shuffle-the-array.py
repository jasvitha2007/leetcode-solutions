class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        r=len(nums)
        x=nums[:n]
        y=nums[n:]
        res=[]
        for i in range(n):
            res.append(x[i])
            res.append(y[i])
        return res
        
        