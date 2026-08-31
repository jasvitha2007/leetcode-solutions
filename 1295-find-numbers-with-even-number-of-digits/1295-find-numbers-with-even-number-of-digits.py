class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if(10<=i<=99 or 1000<=i<=9999 or 100000<=i<=999999):
                c+=1
        return c
        