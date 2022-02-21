class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        collect = []
        for n in nums:
            if n not in collect:
                collect.append(n)
            else:
                return True
        return False


def main():
    x = Solution()
    print(x.containsDuplicate(nums=[1, 2, 3, 4]))


if __name__ == "__main__":
    main()
