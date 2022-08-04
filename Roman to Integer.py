
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                res += roman_dict[s[i]]
            elif roman_dict[s[i]] >= roman_dict[s[i + 1]]:
                res += roman_dict[s[i]]
            else:
                res -= roman_dict[s[i]]
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
