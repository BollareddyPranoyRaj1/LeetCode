class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i,j=0,1
        newA=[0]*len(nums)
        for x in nums:
            if x>=0:
                newA[i]=x
                i+=2
            if x<0:
                newA[j]=x
                j+=2
        return newA

        