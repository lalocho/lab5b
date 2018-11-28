class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = dict()
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        answer = []
        for i in range(k):
            answer.append(max(frequency, key=frequency.get))
            frequency[max(frequency, key=frequency.get)] = 0
        return answer