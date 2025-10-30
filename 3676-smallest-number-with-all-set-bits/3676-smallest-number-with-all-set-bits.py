class Solution:
    def smallestNumber(self, n: int) -> int:
        # Find the smallest power of 2 that is greater than or equal to n+1
        x = 1
        while x <= n:
            x <<= 1  # Multiply x by 2 (shift left)
        return x - 1
