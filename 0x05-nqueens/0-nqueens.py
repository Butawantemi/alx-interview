#!/usr/bin/python3
"""An algorithm to solve the N-Queens problem"""
import sys


class NQueens:
    """Implementing the solution to the NQueens problem"""

    def solve_nqueens(self, n: int):
        """solves the nqueens problem"""
        # set column, positive and negative diagonal sets
        col = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)

        # store results
        res = []

        def backtrack(r, queens):
            """checks for the possible solutions"""
            # check if the end of the board is reached
            if r == n:
                res.append(
                    queens[:]
                )  # Append a copy of the current queen positions
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # add the values to the sets
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                queens.append([r, c])

                # recursively call backtrack again
                backtrack(r + 1, queens)

                # cleanup the sets and backtrack
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                queens.pop()

        # call backtrack method with row 0 as the initial row
        backtrack(0, [])

        return res


def scan(args):
    """scans if the input is a valid input"""
    if len(args) == 2:
        try:
            num = int(args[1])
        except ValueError:
            print("N must be a number")
            exit(1)
        else:
            if num < 4:
                print("N must be at least 4")
                exit(1)

            return num
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    nq = NQueens()
    n = scan(sys.argv)

    res = nq.solve_nqueens(n)

    for solution in res:
        print(solution)
