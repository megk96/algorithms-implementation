class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        total_sum = N*(N+1)/2
        array_sum = sum(nums)
        missing_number = total_sum - array_sum
        return missing_number



def main():
    x = Solution()
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(x.missingNumber(nums))


if __name__ == "__main__":
    main()
