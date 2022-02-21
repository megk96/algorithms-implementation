class Solution(object):
    def removeDuplicates(self, nums):
        front_index = 0
        back_index = 1
        while back_index < len(nums):
            if nums[front_index] != nums[back_index]:
                print("%d %d" % (front_index, back_index))
                front_index += 1
                back_index += 1
            else:
                while nums[back_index] == nums[front_index] and back_index != front_index:
                    print("%d %d" %(front_index, back_index))
                    if back_index < len(nums) - 1:
                        back_index += 1
                    else:
                        front_index += 1
                        nums[front_index] = nums[back_index]
                        print(nums[:front_index])
                        return front_index
                front_index += 1
                nums[front_index] = nums[back_index]
        print(nums[:front_index+1])
        return front_index+1


def main():
    x = Solution()
    array = [0]
    y = x.removeDuplicates(array)


if __name__ == "__main__":
    main()
