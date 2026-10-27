class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        q = deque()
        q.append((beginWord, 1))
        while q:
            curr, count = q.popleft()
            if curr == endWord:
                return count
            curr_word = list(curr)
            for i, ch in enumerate(curr_word):
                temp = ch
                for c in string.ascii_lowercase:
                    curr_word[i] = c
                    new_word = "".join(curr_word)
                    if new_word in word_set:
                        q.append((new_word, count + 1))
                        word_set.remove(new_word)
                curr_word[i] = temp
        return 0

