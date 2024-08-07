class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums2 = nums
        numsset = set(nums)

        if len(numsset) != len(nums2):
            return True
        else:
            return False
        