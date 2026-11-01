class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num,0)+1

        sorted_list = [item[0] for item in sorted(frequency.items(),key=lambda item: item[1], reverse=True)]

        return sorted_list[:k]