class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        rev_x= x[::-1]
        if rev_x==x:
            return True
        else:
            return False        
        