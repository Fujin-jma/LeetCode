class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        N = len(nums)
        total_1 = nums.count(1)

        l = 0 #left pointer

        window_ones = max_window_ones = 0

        #right pointer for window slide
        #2*N for circular
        for r in range(2*N):
            if nums[r%N] == 1:
                window_ones += 1
            if r-l + 1 > total_1:
                window_ones -= nums[l%N]
                l += 1
            max_window_ones = max(max_window_ones, window_ones)
        return total_1 - max_window_ones