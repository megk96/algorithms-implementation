class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        print(n)
        n_str = str(n)
        print(n_str)
        sum = 0
        for i in n_str:
            sum+= int(i)
            print(sum)
        return sum




def main():
    x = Solution()
    n = 0x00000000000000000000000010000000
    print(n)
    print(x.hammingWeight(n))


if __name__ == "__main__":
    main()