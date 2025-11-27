class Solution(object):
    def isValid(self, word):
        if len (word) < 3:
            return False

        vowels = set('aeiouAEIOU')
        has_vowels = False
        has_consonant = False

        for ch in word:
            if  not ch.isalnum():
                return False
            if ch.isalpha():
                if ch in vowels:
                    has_vowels = True
                else:
                    has_consonant = True

        return has_vowels and has_consonant