class Solution:
    def reverse(self, x: int) -> int:
        rev_x = int(str(abs(x))[::-1]) # -123 -> 123 -> 321(str) -> 321(int)

        if rev_x.bit_length() >= 32:
            return 0
        else:
            return rev_x if x > 0 else -rev_x

        