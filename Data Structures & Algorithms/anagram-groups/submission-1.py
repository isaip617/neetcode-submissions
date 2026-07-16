class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet_key = 26 * [0]

        group_of_anagrams = {}

        for string in strs:
            specific_key = 26 * [0]
            for char in string:
                specific_key[ord(char) - ord("a")] += 1
            specific_key = tuple(specific_key)
            if specific_key in group_of_anagrams:
                group_of_anagrams[specific_key].append(string)
            else:
                group_of_anagrams[specific_key] = []
                group_of_anagrams[specific_key].append(string)

        return_value = []
        for value in group_of_anagrams.values():
            return_value.append(value)
        
        return return_value
