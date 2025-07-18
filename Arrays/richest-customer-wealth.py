#https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l=[]
        for cust in accounts:
            suml=sum(cust)
            l.append(suml)
        return max(l)   
