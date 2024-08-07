class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #making array a-z
        #getting the position of the current s[i] in that array a-z
        #comparing next one s[i+1] to next one array a-z[+1]
        #if theyre the same continue and add 1 to count
        #if theyre not the same, append count to the array
        #at the end return array

        arrayaz = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        count = 1
        countray = []

        for i in range(len(s)-1):
            find = arrayaz.index(s[i])

            if find < len(arrayaz) - 1 and s[i+1] == arrayaz[find + 1]:
                count += 1
            else:
                countray.append(count)
                count = 1
        
        countray.append(count)
        return max(countray)

                