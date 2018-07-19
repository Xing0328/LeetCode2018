#leetcode709 to Lower Case
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        newstr = ''
        for char in str:
            if char.isupper():
                newstr += char.lower()
            else:
                newstr += char
        return newstr

str1 = 'Hello'
sol =Solution()
print sol.toLowerCase(str1)