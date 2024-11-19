from typing import List


def groups_of_3(numbers: List[int]) -> List[List[int]]:
    """
    Groups elements of the input list into sublists of three values each.

    Args:
        numbers: A list of integers to be grouped

    Returns:
        A list of lists where each sublist contains up to three consecutive values
        from the input list. The last sublist may contain fewer than three values
        if there aren't enough remaining values.

    Examples:
        >>> groups_of_3([1,2,3,4,5,6,7,8,9])
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> groups_of_3([1,2,3,4,5,6,7,8])
        [[1, 2, 3], [4, 5, 6], [7, 8]]
    """
    result = []
    current_group = []

    for num in numbers:
        current_group.append(num)
        if len(current_group) == 3:
            result.append(current_group)
            current_group = []

    # Add any remaining numbers (will be less than 3)
    if current_group:
        result.append(current_group)

    return result




"""

def groups_of_3(lst: list[int]) -> list[list[int]]:
    groups = []
    for i in range(0, len(lst), 3):
        group = lst[i:i + 3]
        groups.append(group)
    return groups

"""

