class Solution:
    def reverseWords(self, s: str) -> str:

        # Split the string into words.
        # split() automatically removes extra spaces.
        words = s.split()

        # Reverse the list of words.
        words.reverse()

        # Join the words with a single space.
        return " ".join(words)