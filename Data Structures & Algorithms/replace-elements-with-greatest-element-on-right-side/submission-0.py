class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            currMax = 0
            for j in range(i+1, len(arr)):
                if arr[j] > currMax:
                    currMax = arr[j]
            arr[i] = currMax
        arr[len(arr)-1] = -1
        return arr