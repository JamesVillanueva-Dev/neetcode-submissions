class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        lis = [0] * 26
        for c in s:
            lis[ord(c)-ord("a")] += 1
        cnt = 0
        for i in range(len(lis)):
            if lis[i] % 2 == 1:
                cnt += 1
        
        return not cnt > 1
