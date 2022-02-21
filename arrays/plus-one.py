class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]

        if digits[0]+1 > 9:
            digits[0] = 0
            carry = 1
        else:
            digits[0] = digits[0]+1
            return digits[::-1]
        if carry == 1:
            for n in range(1, len(digits)):
                if digits[n] + carry > 9:
                    digits[n] = 0
                else:
                    digits[n] = digits[n] + carry
                    return digits[::-1]
            digits.append(1)
            return digits[::-1]



def main():
    x = Solution()
    print(x.plusOne(digits=[2, 9, 9, 9]))


if __name__ == "__main__":
    main()
