class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = defaultdict(int)
        # get last occurance of ch
        for i,ch in enumerate(s):
            last[ch] = i
        res = []
        end = 0
        size = 0
        for i, ch in enumerate(s):
            size += 1
            end = max(end, last[ch])
            if i == end:
                # reached end of my current partition:
                res.append(size)
                size = 0
        return res
