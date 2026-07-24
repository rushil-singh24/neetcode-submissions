class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list = []
        if len(s) != len(t):
            return False
        for char in s:
            list.append(char)
        for chars in t:
            if chars not in list:
                return False
            list.remove(chars)
        return True