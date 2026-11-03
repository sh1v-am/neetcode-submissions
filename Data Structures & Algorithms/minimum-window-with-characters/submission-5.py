
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        required = Counter(t)

        # Store (index, character) for relevant characters
        positions = [
            (i, char)
            for i, char in enumerate(s)
            if char in required
        ]

        window = Counter()
        left = 0
        formed = 0
        required_types = len(required)

        best_start = 0
        best_length = float("inf")

        for right, (end, char) in enumerate(positions):
            window[char] += 1

            if window[char] == required[char]:
                formed += 1

            while formed == required_types:
                start = positions[left][0]
                length = end - start + 1

                if length < best_length:
                    best_length = length
                    best_start = start

                left_char = positions[left][1]
                window[left_char] -= 1

                if window[left_char] < required[left_char]:
                    formed -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]
