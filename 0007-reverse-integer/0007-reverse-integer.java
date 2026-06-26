class Solution {
    public int reverse(int x) {
        long rev = 0; // Use long to prevent overflow during calculation
        
        while (x != 0) {
            rev = rev * 10 + x % 10;
            x = x / 10;
        }
        
        // Check if the result exceeds the 32-bit integer range
        if (rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE) {
            return 0;
        }
        
        return (int) rev;
    }
}