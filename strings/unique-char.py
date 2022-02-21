class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique = []
        repeated = []
        for i, char in enumerate(s):
            if char in unique:
                unique.remove(char)
                repeated.append(char)
            elif char not in repeated:
                unique.append(char)





def main():
    x = Solution()
    s = "loveleetcode"
    print(x.firstUniqChar(s))


if __name__ == "__main__":
    main()