class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        
        for i, num in enumerate(nums):
            # If num was seen before and the index difference is <= k, return True
            if num in seen and i - seen[num] <= k:
                return True
            # Update/store the latest index for this number
            seen[num] = i
            
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna