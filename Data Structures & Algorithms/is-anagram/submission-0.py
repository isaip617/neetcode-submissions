class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1_dict = {}
        string2_dict = {}

        for char in s:
            if char in string1_dict:
                string1_dict[char] += 1
            else:
                string1_dict[char] = 1
        
        for char in t:
            if char in string2_dict:
                string2_dict[char] += 1
            else:
                string2_dict[char] = 1

        if string1_dict == string2_dict:
            return True
        else:
            return False