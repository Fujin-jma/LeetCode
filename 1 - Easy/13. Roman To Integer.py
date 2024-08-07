class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_num = {
    
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        
        }  

        value = 0
        c = 0
        while c < (len(s)):
            if (c + 1 < len(s) and s[c] == "I") and (s[c+1] == "V"):
                value += 4
                c = c+2
            elif c + 1 < len(s) and (s[c] == "I") and (s[c+1] == "X"):
                value += 9
                c = c+2
            elif c + 1 < len(s) and (s[c] == "X") and (s[c+1] == "L"):
                value += 40
                c = c+2
            elif c + 1 < len(s) and (s[c] == "X") and (s[c+1] == "C"):
                value += 90
                c = c+2
            elif c + 1 < len(s) and (s[c] == "C") and (s[c+1] == "D"):
                value += 400
                c = c+2
            elif c + 1 < len(s) and (s[c] == "C") and (s[c+1] == "M"):
                value += 900
                c = c+2
            else:
                value += roman_num[s[c]]
                c += 1

        return value