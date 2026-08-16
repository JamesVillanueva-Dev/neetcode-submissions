class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        z = 1
        z_cnt = 0
        for num in nums:
            pro *= num
            if(num == 0):
                z_cnt += 1
            else:
                z *= num
        res = []
        for num in nums:
            if num == 0:
                if z_cnt > 1:
                    res.append(0)
                else:
                    res.append(z)
            else:
                res.append(pro//num)
        return res