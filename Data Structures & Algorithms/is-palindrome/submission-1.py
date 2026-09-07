class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = "".join(c for c in s if c.isalnum()).lower()
        
        return (newString == newString[::-1])