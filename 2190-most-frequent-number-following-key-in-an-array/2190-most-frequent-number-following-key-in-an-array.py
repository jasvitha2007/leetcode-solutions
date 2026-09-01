class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        hm={}
        for i in range(len(nums)-1):
            if nums[i]==key:
                target=nums[i+1]
                hm[target]=hm.get(target,0)+1
        return max(hm,key=hm.get)

        