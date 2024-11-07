#!/usr/bin/python3

"""
Defines NQueens Solver
"""

import sys


class Solution:
    def solve(self, n):
        col = set()
        pos_diag = set()
        neg_diag = set()
        res = []
        board = [["."] * n for _ in range(n)]

        def backtracking(r):
            if r == n:
                tmp = []
                for i in range(n):
                    for j in range(n):
                        if board[i][j] == "Q":
                            tmp.append([i, j])
                        if len(tmp) == n:
                            res.append(tmp)
                            tmp = []
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                backtracking(r + 1)
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtracking(0)
        return res


def main():

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    sol = Solution()
    res = sol.solve(int(sys.argv[1]))
    for row in res:
        print(row)


if __name__ == "__main__":
    main()
