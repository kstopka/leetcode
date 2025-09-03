# https://leetcode.com/problems/length-of-last-word/
# Easy
# String


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(list(filter(lambda x: x!= "", s.split(" ")))[-1])
        return len(s.strip().split(" ")[-1])
        

lenLastWord = Solution()
print(lenLastWord.lengthOfLastWord("Hello World"))
print(lenLastWord.lengthOfLastWord("   fly me   to   the moon  "))
print(lenLastWord.lengthOfLastWord("lu  ffy is still joyboy"))