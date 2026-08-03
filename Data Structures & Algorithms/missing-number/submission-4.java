class Solution {
    public int missingNumber(int[] nums) {
        int manipulate = nums.length;
        for(int i = 0; i < nums.length; i++){
            manipulate = manipulate ^ nums[i] ^ i;
        }
        return manipulate;
    }
}