"""
Chapter 4 — Iteration Patterns Over Lists

Covers:
- for-each iteration
- index-based iteration
- enumerate for (index, value)
- while loops (when index control matters)
- building new lists (filter/map style)
- basic list comprehension (preview)
"""

def for_each_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def index_iteration_concat(strings):
    out = ""
    for i in range(len(strings)):
        out += strings[i]
        if i < len(strings) - 1:
            out += ","
    return out

def enumerate_collect_indices(items, target):
    """Return indices where items[i] == target using enumerate."""
    indices = []
    for i, v in enumerate(items):
        if v == target:
            indices.append(i)
    return indices

def while_remove_negatives(numbers):
    """
    Return a new list with negatives removed using a while loop.
    (Shows manual index control.)
    """
    i = 0
    result = []
    while i < len(numbers):
        if numbers[i] >= 0:
            result.append(numbers[i])
        i += 1
    return result

def filter_evens(numbers):
    """Return even numbers (classic loop)."""
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return evens

def square_all(numbers):
    """Return squares using a list comprehension (preview of Chapter 5)."""
    return [n * n for n in numbers]


# ----------------- quick checks -----------------
def _run_tests():
    assert for_each_sum([1, 2, 3]) == 6
    assert index_iteration_concat(["a", "b", "c"]) == "a,b,c"
    assert enumerate_collect_indices(["x", "y", "x", "z"], "x") == [0, 2]
    assert while_remove_negatives([3, -1, 4, -5, 0]) == [3, 4, 0]
    assert filter_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert square_all([2, 3, 4]) == [4, 9, 16]
    print("list_iteration.py: all tests passed ✅")

if __name__ == "__main__":
    _run_tests()
