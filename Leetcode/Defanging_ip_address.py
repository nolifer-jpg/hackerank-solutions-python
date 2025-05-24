class Solution(object):
    def defangIPaddr(self, address):
        if "." in address:
            address = address.replace(".", "[.]")
        return address        
        