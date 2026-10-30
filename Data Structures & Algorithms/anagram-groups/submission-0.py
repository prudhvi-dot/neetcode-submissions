class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in dictionary:
                dictionary[sorted_word] = []
            
            dictionary[sorted_word].append(word)
        
        ans = list(dictionary.values())

        return ans