class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap={0:1}
        prefix_sum=0
        count=0
        for num in nums:
            prefix_sum += num
            if prefix_sum-k in hashMap:
                count+=hashMap[prefix_sum-k]
            hashMap[prefix_sum]=hashMap.get(prefix_sum,0)+1
        return count