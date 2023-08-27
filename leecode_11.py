class Solution:  # 设置两个指针
    def maxarea(self, height: List[int]):
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
                return res


class Solution2:  # n * n次遍历，稍微麻烦点
    def maxarea2(self, height: List[int]):
        for i in range(len(height) - 1):
            for j in range(len(height) - 1):
                while i != j:
                    area = [area, height[i] * abs(j - i)]
                    return max(area)
