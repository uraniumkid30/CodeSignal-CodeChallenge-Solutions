"""
    Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

    Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

    Example

    For sequence = [1, 3, 2, 1], the output should be
    solution(sequence) = false.

    There is no one element in this array that can be removed in order to get a strictly increasing sequence.

    For sequence = [1, 3, 2], the output should be
    solution(sequence) = true.

    You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
"""
from .utils import timefunc


@timefunc("Almost Increasing Sequence.")
def solution(sequence: list) -> bool:
    removed_one: bool = False
    prev_maxval: int = None
    maxval: int = None
    for item in sequence:
        if (not maxval) or (item > maxval):
            prev_maxval = maxval
            maxval = item
        elif (not prev_maxval) or (item > prev_maxval):
            if removed_one:
                return False
            removed_one = True
            maxval = item
        else:
            if removed_one:
                return False
            removed_one = True
    return True
