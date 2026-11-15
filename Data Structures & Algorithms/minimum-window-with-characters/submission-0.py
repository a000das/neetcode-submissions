class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        window = {}
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # This character's requirement was just satisfied
            if c in count_t and window[c] == count_t[c]:
                have += 1

            # Shrink while the window is valid
            while have == need:
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                left = s[l]
                window[left] -= 1
                # Removing this character broke a requirement
                if left in count_t and window[left] < count_t[left]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""