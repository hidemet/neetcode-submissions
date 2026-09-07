class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time Complexity: O(N log N)
        Space Complexity: O(1)
        """
        
        low: int = 0
        high: int = len(nums) - 1
        while low <= high:
            mid: int = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
            
