class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        centerj = len(grid[0])-1
        centeri = len(grid)-1
        ans = 0

        if len(grid[0]) < 3:
            return 0

        def checknum(num, num2):
            arr = []
            for row in range(num-1, num+2):
                if grid[num2-1][row] not in arr:
                    arr.append(grid[num2-1][row])
                if grid[num2][row] not in arr:
                    arr.append(grid[num2][row])
                if grid[num2+1][row] not in arr:
                    arr.append(grid[num2+1][row])
                else:
                    return False
            for m in arr:
                if m > 9:
                    return False
                elif m < 1:
                    return False
            return True


        for j in range(1, centeri):
            for i in range(1, centerj):
                check = checknum(i, j)
                if check:
                    if ((grid[j-1][i-1])+(grid[j-1][i])+(grid[j-1][i+1])) == ((grid[j][i-1])+(grid[j][i])+(grid[j][i+1]))  == ((grid[j+1][i-1])+(grid[j+1][i])+(grid[j+1][i+1])) == ((grid[j-1][i-1])+(grid[j][i])+(grid[j+1][i+1])) == ((grid[j+1][i-1])+(grid[j][i])+(grid[j-1][i+1])) == ((grid[j-1][i-1])+(grid[j][i-1])+(grid[j+1][i-1])) == ((grid[j-1][i])+(grid[j][i])+(grid[j+1][i])) == ((grid[j-1][i+1])+(grid[j][i+1])+(grid[j+1][i+1])):

                        ans+=1

        return ans


        
        