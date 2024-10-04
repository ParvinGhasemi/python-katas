class ReverseInteger:
    """
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    
    Example 1:
    Input: x = 123
    Output: 321

    Example 2:
    Input: x = -123
    Output: -321

    Constraints:
    -2**31 <= x <= 2**31 - 1
    """
    def reverse_integer(self, num: int) -> int:
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        string_num = str(abs(num))
        reversed_num = int(string_num[::-1])
        
        if num < 0:
            reversed_num = -reversed_num
        if reversed_num > MAX_INT or reversed_num < MIN_INT:
            return 0
        
        return reversed_num