class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            count = {}

            for letters in zip(s):
                count[letters[0]] = count.get(letters[0], 0) + 1

            for letters in zip(t):
                if letters[0] not in count:
                    return False
                count[letters[0]] -= 1

                if count[letters[0]] < 0:
                    return False

            return True
