import numpy as np

class Solution(object):

    def checkSet(self, strip):
        collect = []
        for n in strip:
            if n.isdigit():
                if n not in collect:
                    collect.append(n)
                else:
                    return False
        return True
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        isValid = True
        for row in board:
            isValid = self.checkSet(row)
        if isValid:
            t_board = zip(*board)
            for row in t_board:
                isValid = self.checkSet(row)
        if isValid:
            n = 0








def main():
    x = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(x.isValidSudoku(board))


if __name__ == "__main__":
    main()
