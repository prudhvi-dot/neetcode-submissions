class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        for num in nums:
            dictionary[num] = dictionary.get(num,0)+1

        ordered_list =  sorted(dictionary.items(),key=lambda item: item[1], reverse=True)
        return [item[0] for item in ordered_list][:k]