class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == "*":
                star.append(i)
            else: # ch == ")"
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while stack and star:
            # there is a star but happens to be before an opening "("
            # in that case we cnnot balance so return a false
            if stack.pop() > star.pop():
                return False
        # only True if stack is empty else we return False
        # thats the case where number of rem open par was greater than number of  rem stars
        return True if len(stack) == 0 else False


