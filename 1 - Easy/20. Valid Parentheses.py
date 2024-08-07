class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        opbrack = '(', '{', '['
        clobrack = ')', '}', ']'

        if s[0] in clobrack:
            return False
            
    
        for c in range(len(s)-1):
            if (s[c] in opbrack) and (s[c+1] in clobrack):
                if opbrack.index(s[c]) == clobrack.index(s[c+1]):
                    pass
                else:
                    return False
            elif (s[c] in clobrack) and (s[c-1] in opbrack):
                if clobrack.index(s[c]) == opbrack.index(s[c-1]):
                    pass
                else:
                    return False
            else:
                return False

        return True

