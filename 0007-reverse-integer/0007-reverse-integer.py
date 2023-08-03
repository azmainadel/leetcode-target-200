class Solution:
    def reverse(self, x: int) -> int:
        reverse_string = str(abs(x))[::-1]
        res = int(reverse_string)

        if res.bit_length() >= 32:
            return 0
        else:
            return res if x > 0 else -res