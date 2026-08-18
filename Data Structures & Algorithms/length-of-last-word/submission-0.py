class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        words = []
        
        for ch in s:
            if ch == " ":
                if word:            
                    words.append(word)
                    word = ""
            else:
                word += ch

        if word:                     
            words.append(word)

        return len(words[-1])