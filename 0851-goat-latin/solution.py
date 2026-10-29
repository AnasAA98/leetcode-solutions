class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        res = []
        count = 1
        vowels = set("aeiouAEIOU")
        for word in sentence:
            if word[0] in vowels:
                new_word = word + "ma" + ("a" * count)
            else:
                ch = word[0]
                new_word = word[1:] + ch + "ma" + ("a" * count)
            count += 1
            res.append(new_word)
        return " ".join(res) 
