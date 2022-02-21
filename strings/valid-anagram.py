class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count1 = {}
        for char in s:
            if char in count1:
                count1[char] += 1
            else:
                count1[char] = 1

        count2 = {}
        for char in t:
            if char in count2:
                count2[char] += 1
            else:
                count2[char] = 1

        if len(count1)!=len(count2):
            return False
        for c in count1:
            if c not in count2:
                return False
            if count1[c] != count2[c]:
                return False
        return True

def main():
    x = Solution()
    s = "aanaxxgarahm"
    t = "aanagrahmax"
    print(x.isAnagram(s, t))


if __name__ == "__main__":
    main()