class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
    
        freq = []
        itemlist = []
        for item in word:
            if item not in itemlist:
                itemlist.append(item)
                freq.append(word.count(item))
        
        freq.sort(reverse = True)

        ans = 0
    
        for i in range(len(freq)):
            ans += (((i//8)+1)*freq[i])
        return ans
        
    

        