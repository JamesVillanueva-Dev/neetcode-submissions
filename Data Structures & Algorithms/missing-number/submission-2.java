class Solution {
    public int missingNumber(int[] nums) {
        int normSum = 0;
        int sum = 0;
        for(int i = 0; i <= nums.length; i++){
            normSum += i;
        }
        for(int i = 0; i < nums.length; i++ ){
            sum += nums[i];
        }
        return normSum - sum;
    }
}
