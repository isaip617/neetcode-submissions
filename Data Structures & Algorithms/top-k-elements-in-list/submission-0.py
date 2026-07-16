class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for integer in nums:
            if integer in hashmap:
                hashmap[integer] += 1
            else:
                hashmap[integer] = 1

        tuples_of_elements = []
        for key, value in hashmap.items():
            tuples_of_elements.append((value, key))
        
        tuples_of_elements.sort(reverse=True)
        return_value = []
        for i in range(k):
            return_value.append(tuples_of_elements[i][1])
        return return_value
        