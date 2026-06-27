class Solution {
    public int[] plusOne(int[] digits) {
        // Start from the last digit (least significant)
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits; // No more carryover, we can return early!
            }
            
            // If it was 9, it becomes 0, and we carry the 1 to the next iteration
            digits[i] = 0;
        }
        
        // If we reach here, all digits were 9 (e.g., 999 -> 000)
        // We need a new array of size n + 1 (e.g., 1000)
        int[] newDigits = new int[digits.length + 1];
        newDigits[0] = 1; // The rest defaults to 0 automatically in Java
        
        return newDigits;
    }
}