class Solution:
    def ispalindrome(self, x: int):
        x = input('x = ?')
        return str(x) == str(x)[::-1]  # 大佬的算法
# 我想的稍微麻烦点，把倒序表示出来再进行比较
