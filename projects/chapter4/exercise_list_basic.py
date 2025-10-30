"""
Chapter 4 — Exercise: List Basics

Covers:
- Create lists
- Indexing & slicing
- Mutating items
- Length & membership
- Concatenation and copying
"""

def first_last(items):
    """Return a tuple of (first, last) from a non-empty list."""
    return items[0], items[-1]

def middle_slice(items):
    """
    Return a slice of all items except the first and last.
    If the list is too small, return an empty list.
    """
    return items[1:-1]

def replace_at(items, index, new_value):
    """Replace the value at index with new_value and return the modified list."""
    items[index] = new_value
    return items

def count_membership(items, target):
    """Return (exists, count) for target in items."""
    return (target in items, items.count(target))

def concat_and_copy(a, b):
    """
    Return (concat, copy_a):
      - concat is a + b
      - copy_a is a shallow copy of a
    """
    concat = a + b
    copy_a = a[:]         # or list(a) or a.copy()
    return concat, copy_a

def stats_of(numbers):
    """Return (length, total, minimum, maximum) for a list of numbers."""
    return len(numbers), sum(numbers), min(numbers), max(numbers)


# ----------------- quick checks -----------------
def _run_tests():
    fruits = ["apple", "banana", "cherry", "date"]
    assert first_last(fruits) == ("apple", "date")
    assert middle_slice(fruits) == ["banana", "cherry"]

    nums = [10, 20, 30]
    assert replace_at(nums, 1, 99) == [10, 99, 30]

    letters = list("banana")
    assert count_membership(letters, "a") == (True, 3)
    assert count_membership(letters, "z") == (False, 0)

    c, copy_a = concat_and_copy([1, 2], [3, 4])
    assert c == [1, 2, 3, 4]
    assert copy_a == [1, 2] and copy_a is not [1, 2]  # different object than literal

    length, total, mn, mx = stats_of([5, 1, 9, 2])
    assert (length, total, mn, mx) == (4, 17, 1, 9)

    print("exercise_list_basics.py: all tests passed ✅")

if __name__ == "__main__":
    _run_tests()
