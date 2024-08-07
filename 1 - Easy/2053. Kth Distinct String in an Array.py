class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """

        count = 0
        map = {}

        #checks whether the items are unique
        for item in arr:
            if item in map:
                map[item] = False
            else:
                map[item] = True

        #checks the kth position for each unique item
        for item in arr:
            if map[item]:
                count += 1
                if count == k:
                    return item

        #if there's nothing the returns ""
        return ""

    
        