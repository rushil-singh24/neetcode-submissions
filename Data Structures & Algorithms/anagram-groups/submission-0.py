class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            newWord = ''.join(sorted(word))
            if newWord not in dictionary:
                dictionary[newWord] = [word]
            else:
                dictionary[newWord].append(word)
        return list(dictionary.values())