class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)
        prefix = ""

        for i in range(min_len):
            char = strs[0][i]
            if all(s[i] == char for s in strs):
                prefix += char
            else:
                break

        return prefix


# Test qismi
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))  # ""
