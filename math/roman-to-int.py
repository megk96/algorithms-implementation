class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sub_rules = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        value = 0
        index_tracker = []
        for i in range(len(s)-1):
            byte = s[i:i+2]
            if byte in sub_rules:
                value += sub_rules[byte]
                index_tracker.append(i)
                index_tracker.append(i+1)
        for i in range(len(s)):
            if i not in index_tracker:
                value += val[s[i]]
        return value



def main():
    x = Solution()
    print(x.romanToInt(s="MCMXCIV"))


if __name__ == "__main__":
    main()