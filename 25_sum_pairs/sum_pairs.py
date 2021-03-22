def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal."""

    checked_nums = set() 

    for num in nums:
        difference = goal - num

        if difference in checked_nums:
            return (difference, num)
        
        checked_nums.add(num)
    
    return ()