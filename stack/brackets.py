class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if len(stack)>0:
                    x = stack.pop()
                    if i!=pairs[x]:
                        return False
                else:
                    return False
        if(len(stack)==0):
            return True
        else:
            return False

def main():
    x = Solution()
    s = "{()[]{}{}[[()]}"
    print(x.isValid(s))


if __name__ == "__main__":
    main()