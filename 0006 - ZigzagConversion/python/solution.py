class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        period = numRows * 2 - 2
        n = len(s)
        output = ""
        for r in range(numRows):
            substr = [s[i] for i in range(n) if i % period == r or i % period == period - r]
            output += "".join(substr)

        return output