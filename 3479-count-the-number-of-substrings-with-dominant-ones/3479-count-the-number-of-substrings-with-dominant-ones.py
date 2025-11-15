import bisect, math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros = [i for i, ch in enumerate(s) if ch == '0']
        m = len(zeros)
        res = 0
        maxZ = int(math.sqrt(n)) + 2

        for i in range(n):
            # index of first zero >= i
            idx = bisect.bisect_left(zeros, i)

            # z = 0 case: all-ones substrings until next zero (or end)
            next_zero = zeros[idx] if idx < m else n
            res += (next_zero - i)

            # z >= 1: consider substrings containing exactly z zeros
            for z in range(1, maxZ + 1):
                if idx + z - 1 >= m:
                    break
                L = z * z + z  # minimal required length so ones >= z^2
                if i + L - 1 >= n:
                    break

                pos_zth = zeros[idx + z - 1]
                earliest_end = max(pos_zth, i + L - 1)
                latest_end = (zeros[idx + z] - 1) if (idx + z) < m else (n - 1)

                if earliest_end <= latest_end:
                    res += (latest_end - earliest_end + 1)

        return res