class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        azzay = []
        for i in range(1, (n+1)):
            if i%5==0 and i%3==0:
                azzay.append("FizzBuzz")
            elif i%3==0:
                azzay.append("Fizz")
            elif i%5==0:
                azzay.append("Buzz")
            else:
                azzay.append(str(i))
        return azzay


def main():
    x = Solution()
    print(x.fizzBuzz(16))


if __name__ == "__main__":
    main()