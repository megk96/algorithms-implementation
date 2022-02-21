class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unpaired = []
        for n in nums:
            if n in unpaired:
                unpaired.remove(n)
            else:
                unpaired.append(n)
        return unpaired[0]


def main():
    x = Solution()
    print(x.singleNumber(nums=[1]))


if __name__ == "__main__":
    main()
