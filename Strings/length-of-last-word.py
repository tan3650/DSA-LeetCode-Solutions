#https://leetcode.com/problems/length-of-last-word/?envType=problem-list-v2&envId=string
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        for i in range(len(s),0,-1): 
            if s[i-1]!=" ":
                c=c+1
            elif c!=0:  #if counting started then only break cuz otherwise first space loop gets broken
                break
        return c