from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums):
        # Count occurrences of each number
        counts = Counter(nums)
        # Find numbers that appear twice
        result = [num for num, cnt in counts.items() if cnt == 2]
        return result
