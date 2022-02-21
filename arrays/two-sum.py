class Solution(object):
    def twoSum(self, nums, target):
        collect = {}
        for i, n in enumerate(nums):
            if n not in collect:
                collect[target-n] = i
            else:
                return [collect[n], i]



def main():
    x = Solution()
    nums = [3,2,4]
    target = 7
    print(x.twoSum(nums, target))


if __name__ == "__main__":
    main()
