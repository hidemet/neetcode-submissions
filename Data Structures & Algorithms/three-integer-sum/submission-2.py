"""
time complexity O(N^2). The sort operation takes O(N*logN), the outer loop O(N) and the scan of the two pointers O(N), giving a total of O(N*logN + N?2) = O(N^2)

Space complexity O(1)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result : List[List[int]] = []
        n: int = len(nums)
        for i in range(n-2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue
            left: int = i + 1
            right: int = n - 1
        
            while left < right:
                total : int = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result



        