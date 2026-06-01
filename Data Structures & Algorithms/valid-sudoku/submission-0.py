class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for i in range(len(board)):
            # print(i, len(board))
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i // 3, j // 3)]):
                    return False
                # print(j, len(board[i]))
                # print(i, j, board[i][j])
                rows[i].add(board[i][j])
                # print(rows[i], board[i][j])
                cols[j].add(board[i][j])
                # idx = (i // 3) * 3 + (j // 3)
                squares[(i // 3, j // 3)].add(board[i][j])
        return True