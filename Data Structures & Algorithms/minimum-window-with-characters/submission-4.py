
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        has = {}

        for char in t:
            has[char] = has.get(char, 0) + 1

        left = 0
        min_len = float("inf")
        start = 0
        required = len(has)
        formed = 0
        window = {}

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in has and window[char] == has[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in has and window[left_char] < has[left_char]:
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]
