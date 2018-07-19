class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
      
        morse_dic = {
            "a" : ".-",
            "b" : '-...',
            "c" : '-.-.',
            "d" : "-..",
            "e" :".",
            "f" : "..-.",
            "g" : "--.",
            "h" : "....",
            "i" : "..",
            "j" : ".---",
            "k" : "-.-",
            "l" : ".-..",
            "m" : "--",
            "n" : "-.",
            "o" : "---",
            "p" : ".--.", "q" : "--.-","r" : ".-.", "s": "...",
            "t":  "-",  "u":  "..-","v":  "...-","w":  ".--", "x":"-..-",
            "y": "-.--", "z": "--.."
        }
        
        res = []
        
        for word in words:
            morse = ''
            for char in word:
                morse += morse_dic[char]
            if morse not in res:
                res.append(morse)
        print res
        return len(res)
words = ["gin", "zen", "gig", "msg"]
sol = Solution()
print sol.uniqueMorseRepresentations(words)