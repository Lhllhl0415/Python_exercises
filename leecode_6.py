# character string to achieve z-shaped arrangement
class Solution:
    s = input("string =")
    numrows = input("numrows = ")

    def convert(self, s: str, numrows: int, zstring):
        nums = len(s) // (2 * numrows - 2)
        res = len(s) - nums * (2 * numrows - 2)
        if res <= numrows:
            col = (numrows - 1) * nums + 1
        else:
            col = nums * (numrows - 1) + 1 + (res - numrows)
        for i in range(col - 1):
            for j in range(numrows - 1):
                if i % (numrows - 1) == 0:
                    zstring[j][i] = s[j + i * 2]
                else:
                    zstring[j][nums * 4 - j] = s[j + i * 2]


class Solution:
    def convert(self, s: str, numRows: int):
        if numRows < 2:
            return s  # 行数为1的情况
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c  # str -> list
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)  # join函数拼接字符串？
