def arguments_length(*args: object) -> int:
    """
    Returns the number of arguments passed to the function.
    
    Args:
        *args (object): Any number of arguments of any type.
        
    Returns:
        int: The number of arguments passed.
    
    Time complexity: O(1)
    Space complexity: O(1)
    """
    return len(args)