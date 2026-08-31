class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new_s = ""

        for ch in s:
            if ch.isalnum():
                new_s += ch

        if new_s == new_s[::-1]:
            return True

        return False
        
        