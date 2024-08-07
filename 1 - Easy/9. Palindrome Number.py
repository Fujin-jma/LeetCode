class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        #start


        xstr = str(x)
        length = int(len(xstr)/2)

        for i in range(0, length):
            if xstr[i] == xstr[-(i+1)]:
                pass
            else:
                return False
        return True


        

        

        
        