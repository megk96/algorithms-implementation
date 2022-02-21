class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos_index = 0
        track_index = 0

        while track_index < len(nums):
            #print("%d %d" % (pos_index, track_index))
            if nums[track_index] !=0:
                nums[pos_index] = nums[track_index]
                pos_index+=1
                track_index+=1
            else:
                track_index+=1
        for i in range(pos_index, len(nums)):
            nums[i] = 0
        return nums


def main():
    x = Solution()
    array = [0, 0, 1, 0, 1, 0, 0]
    print(x.moveZeroes(array))


if __name__ == "__main__":
    main()
