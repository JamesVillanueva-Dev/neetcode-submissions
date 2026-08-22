class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        numSet = set(nums)

        currMax = 0

        for num in numSet:
            if num - 1 not in numSet:
                curr = 1
                while num + 1 in numSet:
                    curr += 1
                    num += 1
                if curr > currMax:
                    currMax = curr

        return currMax