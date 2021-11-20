class Solution():
    def reverseString(self,s):
        for i in range(len(s)//2):
            temp = s[::-1]