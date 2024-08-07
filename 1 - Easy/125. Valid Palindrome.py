class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        schar = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                schar = schar + char
        schar = schar.lower()
        length = int(len(schar)/2)

        for i in range(0, length):
            if schar[i] == schar[-(i+1)]:
                pass
            else:
                return False
        return True


        