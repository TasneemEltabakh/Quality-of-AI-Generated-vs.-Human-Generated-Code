'''
You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.

Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.

Return the string after rearranging the spaces.
'''
class Solution:
    def reorderSpaces(self, text: str) -> str:
        text_split = text.split(' ')
        words = [w for w in text_split if w] 
        n_spaces = text.count(' ')
        if len(words) == 1:
            return words[0] + (' ' * n_spaces)
        equal_spaces_n = n_spaces // (len(words) - 1)
        spaced_text = (' ' * equal_spaces_n).join(words)
        return spaced_text +  (' ' * (n_spaces % (len(words) - 1)))
