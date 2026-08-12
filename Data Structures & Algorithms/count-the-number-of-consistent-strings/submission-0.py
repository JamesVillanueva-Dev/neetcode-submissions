class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        rule = []
        for c in allowed:
            rule.append(c)
        for s in words:
            flag = False
            for c in s:
                if c in rule:
                    continue
                else:
                    flag = True
                    break
            if flag == False:
                res += 1
        return res
            