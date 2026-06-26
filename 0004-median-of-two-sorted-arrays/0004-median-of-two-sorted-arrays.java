import java.util.Arrays;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // 1. Create the new array
        int[] num3 = new int[nums1.length + nums2.length];
        
        // 2. Copy elements from both arrays into num3
        int k = 0;
        for (int i = 0; i < nums1.length; i++) num3[k++] = nums1[i];
        for (int i = 0; i < nums2.length; i++) num3[k++] = nums2[i];
        
        // 3. Sort it
        Arrays.sort(num3);
        
        int n = num3.length;
        double median;
        
        // 4. Calculate median using indices []
        if (n % 2 == 0) {
            // Average of the two middle elements
            median = (num3[n / 2 - 1] + num3[n / 2]) / 2.0;
        } else {
            // The exact middle element
            median = num3[n / 2];
        }
        
        return median;
    }
}