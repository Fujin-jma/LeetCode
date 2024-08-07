class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """

        count = 0
        for c in details:
            check = c
            if check[11] > "6":
                count += 1
            elif check[11] == "6":
                if check[12] > "0":
                    count += 1
        
        return count
        