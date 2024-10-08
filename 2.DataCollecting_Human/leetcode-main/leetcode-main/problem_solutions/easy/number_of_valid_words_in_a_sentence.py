'''
A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.

A token is a valid word if all three of the following are true:

It only contains lowercase letters, hyphens, and/or punctuation (no digits).
There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

Given a string sentence, return the number of valid words in sentence.
'''
class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split(' ')
        def valid_word(w):
            if all(c not in w for c in '0123456789') and all(c not in w[:-1] for c in '!.,') and w != '' and w.count('-') < 2:
                return '-' in w[1:-2 if w[-1] in '!.,' else -1] if '-' in w else True
            return False
        valid_words = [w for w in words if valid_word(w)]
        return len(valid_words)
