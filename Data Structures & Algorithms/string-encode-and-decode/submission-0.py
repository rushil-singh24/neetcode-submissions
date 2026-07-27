class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            length = len(string)
            output += str(length)
            output += "#"
            output += string  
        return output
    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            length = int(s[i: s.find("#", i)])
            start = s.find("#", i) + 1
            sub = s[start:start+length]
            output.append(sub)
            i = start + length
        return output
            