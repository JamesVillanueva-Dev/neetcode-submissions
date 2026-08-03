class Solution {
    public boolean isPalindrome(String s) {
        String modified = s.toLowerCase();
        String forward = "";
        String backward = "";

        for(int i = 0; i < modified.length(); i++){
            if(modified.charAt(i) <= 'z' && modified.charAt(i) >= 'a' || modified.charAt(i) <= '9' && modified.charAt(i) >= '0'){
                forward += modified.charAt(i);
            }
        }
        for(int i = modified.length()-1; i >= 0; i--){
            if(modified.charAt(i) <= 'z' && modified.charAt(i) >= 'a' || modified.charAt(i) <= '9' && modified.charAt(i) >= '0'){
                backward += modified.charAt(i);
            }
        }
        return forward.equals(backward);
    }
}
