class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        
        # For each position where nums[i] == 0
        for i in range(n):
            if nums[i] == 0:
                # Calculate sum of elements to the left
                sum_left = sum(nums[:i])
                # Calculate sum of elements to the right
                sum_right = sum(nums[i+1:])
                
                # If sums are equal, both directions work
                if sum_left == sum_right:
                    count += 2
                # If sums differ by 1, one direction works
                elif abs(sum_left - sum_right) == 1:
                    count += 1
        
        return count