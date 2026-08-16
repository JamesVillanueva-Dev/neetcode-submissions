class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num_ones = 0
        num_zeroes = 0

        for c in s:
            if c == '1':
                num_ones += 1
            if c == '0':
                num_zeroes += 1
        
        res = ""
        while num_ones > 1:
            res += '1'
            num_ones -= 1
        while num_zeroes:
            res += '0'
            num_zeroes -= 1
        
        res += '1'

        return res