class Solution:
    def intToRoman(self, num: int):  # 哈希
        hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                   5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for key in hashmap:
            if num // key != 0:
                count = num // key
                res += hashmap[key] * count
                num %= key
            return res


class Solution2:
    def intToRoman2(self, num: int):
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]

# 这道题我一直想办法避免列举但是反而没有思路，借鉴了另外两种方法用哈希或者直接列举反而轻松些
# 而且pycharm社区版怎么总是出现各种警告，变量总是不允许我大写
