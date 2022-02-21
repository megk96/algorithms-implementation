class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersect = []
        if len(nums1) <= len(nums2):
            for n in nums1:
                if n in nums2:
                    intersect.append(n)
                    nums2.remove(n)
        else:
            for n in nums2:
                if n in nums1:
                    intersect.append(n)
                    nums1.remove(n)
        return intersect


def main():
    x = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(x.intersect(nums1, nums2))


if __name__ == "__main__":
    main()
