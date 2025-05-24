class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum =0
        product = 1
        result = 0 
        temp=0
        while temp< n:
            product *= n%10
            sum += n%10
            n=n//10
        result = product-sum
        return result    