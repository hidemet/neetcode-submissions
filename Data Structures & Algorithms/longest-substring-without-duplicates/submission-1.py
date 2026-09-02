"""
Time Complexity: O(N) in ogni caso.
Space Complexity: O(min(N,M))
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen: dict[str, int] = {}
        left: int = 0
        max_len: int = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                # Salto istantaneo oltre il duplicato
                left = last_seen[char] + 1

            last_seen[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len