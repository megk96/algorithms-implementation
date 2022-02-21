import math


class Solution(object):
    import math
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        front_index = 0
        back_index = len(s) - 1
        print(back_index)
        print(len(s))
        n = int(math.floor(len(s) / 2))
        print(n)
        for i in range(n):
            temp = s[front_index]
            s[front_index] = s[back_index]
            s[back_index] = temp
            front_index += 1
            back_index -= 1
        return


def main():
    x = Solution()
    s = ["h","e","l","l","o", "J"]
    print(x.reverseString(s))


if __name__ == "__main__":
    main()
