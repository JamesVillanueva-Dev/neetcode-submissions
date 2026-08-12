class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if i < len(s) - 1:
                res += abs(ord(s[i]) - ord (s[i+1]))
                i += 1
            else:
                return res
