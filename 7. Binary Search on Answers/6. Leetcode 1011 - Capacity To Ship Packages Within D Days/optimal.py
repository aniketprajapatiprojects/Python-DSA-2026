from typing import List


class Solution:
    def find_days(self, weights, capacity):
        total_days = 1
        current_load = 0

        for weight in weights:
            if current_load + weight > capacity:
                total_days += 1
                current_load = 0
            current_load += weight

        return total_days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Do the below calculation using FOR loop
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            numberOfDays = self.find_days(weights, mid)
            if numberOfDays <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low
