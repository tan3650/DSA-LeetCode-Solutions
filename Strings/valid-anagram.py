#https://leetcode.com/problems/valid-anagram/?envType=problem-list-v2&envId=string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in t:
            if i in s:
                pass
            else:
                return False
            return True