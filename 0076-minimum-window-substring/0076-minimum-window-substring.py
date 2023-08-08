from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ''
        min_length = float('inf')

        required_counter = Counter(t)
        required_chars = len(required_counter)

        current_counter = Counter()
        found_chars = 0

        l, r = 0, 0

        while r < len(s):
            current_counter[s[r]] += 1

            if s[r] in required_counter and current_counter[s[r]] == required_counter[s[r]]:
                found_chars += 1

            while found_chars == required_chars and l <= r:
                if (r - l + 1) < min_length:
                    min_length = r - l + 1
                    ans = s[l:r+1]
                
                if s[l] in required_counter and current_counter[s[l]] == required_counter[s[l]]:
                    found_chars -= 1

                current_counter[s[l]] -= 1
                l += 1
            
            r += 1
        
        return ans


