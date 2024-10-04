class GreatestCommonDivisor:
    """
    Given the head of a linked list, in which each node contains an integer value.
    Between every pair of adjacent nodes, insert a new node with a value equal to 
    the greatest common divisor of them. Return the linked list after insertion.
    The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
    """
    def __init__(self, numbers: list[int]):
        self.num1 = num1
        self.num2 = num2

    def calculate_gcd(self, head: list[int]) -> list[int]:
        if not head:
            return []
        if len(head) == 0:
            return head

        