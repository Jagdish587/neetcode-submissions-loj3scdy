class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [""] * numRows
        row = 0
        direction = 1

        if numRows == 1:
            return s

        for ch in s:
            res[row] += ch

            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

            row += direction

        return  "".join(res)