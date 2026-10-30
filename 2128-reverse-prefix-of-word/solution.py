class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = ""
        indx = -1
        for i in range(len(word)):
            if word[i] == ch:
                indx = i
                break
        if indx == -1:
            return word
        revs = word[: indx + 1]
        revs = revs[::-1]
        res = revs + word[indx + 1:]
        return res

