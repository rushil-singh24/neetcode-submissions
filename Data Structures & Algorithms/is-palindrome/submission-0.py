class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphanumeric = "abcdefghijklmnopqrstuvwxyz123457890"
        for char in s:
            if char not in alphanumeric:
                s = s.replace(char, "")
        i = 0
        while(i < len(s)):
            if (s[i] != s[len(s) - 1 - i]):
                return False
            i += 1
        return True