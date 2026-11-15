class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        left = 0
        max_freq = 0
        longest = 0

        for right, char in enumerate(s):
            idx = ord(char) - ord('A')
            counts[idx] += 1
            max_freq = max(max_freq, counts[idx])

            while (right - left + 1) - max_freq > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest