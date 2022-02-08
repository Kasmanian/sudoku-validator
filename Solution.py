class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Box, Row, Col = {}, {}, {}
        r, c = 0, 0
        for row in board:
            c = 0
            for col in row:
                if col == '.':
                    c += 1
                    continue
                if r not in Row: Row[r] = {}
                if col not in Row[r]: Row[r][col] = ''
                else: return False
                if c not in Col: Col[c] = {}
                if col not in Col[c]: Col[c][col] = ''
                else: return False
                b = (3*((r*9+c)//27))+c//3
                if b not in Box: Box[b] = {}
                if col not in Box[b]: Box[b][col] = ''
                else: return False
                c += 1
            r += 1
        return True
