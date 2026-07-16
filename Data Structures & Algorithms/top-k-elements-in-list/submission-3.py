class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = len(nums) * [0]
        hashmap = {}
        print(buckets)
        
        for integer in nums:
            if integer in hashmap:
                hashmap[integer] += 1
            else:
                hashmap[integer] = 1
        
        for integer, freq in hashmap.items():
            if buckets[freq - 1] == 0:
                buckets[freq - 1] = []
                buckets[freq - 1].append(integer)
            else:
                buckets[freq - 1].append(integer)
        
        return_list = []
        result_counter = k

        for i in range(len(buckets) - 1, -1, -1):
            print(buckets[i])
            if buckets[i] != 0:
                print(buckets[i])
                for integer in buckets[i]:
                    return_list.append(integer)
                    result_counter -= 1
            if result_counter == 0:
                break
        return return_list

        