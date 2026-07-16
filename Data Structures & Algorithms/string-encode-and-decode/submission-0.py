class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            length = len(string)
            prefix = str(length) + "#"
            encoded_string = encoded_string + prefix
            encoded_string = encoded_string + string
        print(encoded_string)
        return encoded_string


    def decode(self, s: str) -> List[str]:
        index = 0
        return_list = []
        word_length_string = ""
        word_length_integer = 0
        length_of_string = len(s)
        while index < length_of_string:
            if s[index].isdigit() == True:
                word_length_string += s[index]
                index += 1
            else:
                word_length_integer = int(word_length_string)
                word_length_string = ""
                return_list.append(s[index + 1: index + word_length_integer + 1])
                index = index + word_length_integer + 1
        
        return return_list








