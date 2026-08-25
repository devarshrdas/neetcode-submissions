class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        top_k_elements = counter.most_common(k)
        values = [item[0] for item in top_k_elements]
        return values