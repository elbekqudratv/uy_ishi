class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

# Test qismi
solution = Solution()
print(solution.strStr("sadbutsad", "sad"))  # 0
print(solution.strStr("leetcode", "leeto"))  # -1
