class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = 'aeiou'
        for i in vowels:
            s = s.replace(i, '')
        return s
