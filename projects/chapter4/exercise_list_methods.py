"""
Chapter 4 — Exercise: Common List Methods

Covers:
- append, extend, insert
- remove, pop
- clear, copy
- sort (in-place) vs sorted (new list)
- reverse
- index, count
"""

def add_items(base, to_end, at_index=None, to_insert=None, extend_with=None):
    """
    Mutates 'base' by:
      - appending 'to_end'
      - inserting 'to_insert' at 'at_index' if provided
      - extending with 'extend_with' if provided
    Returns base.
    """
    base.append(to_end)
    if at_index is not None and to_insert is not None:
        base.insert(at_index, to_insert)
    if extend_with:
        base.extend(extend_with)
    return base

def remove_safe(items, value):
    """
    Remove first occurrence of value if it exists.
    Return True if removed, False if not found.
    """
    if value in items:
        items.remove(value)
        return True
    return False

def pop_last(items):
    """Pop and return the last item (or None if empty)."""
    if items:
        return items.pop()
    return None

def sorted_copy(items, reverse=False, key=None):
    """
    Return a NEW sorted list, leaving original untouched.
    Demonstrates 'sorted' vs in-place 'list.sort'.
    """
    return sorted(items, reverse=reverse, key=key)

def reverse_in_place(items):
    """Reverse the list in-place; return the mutated list for convenience."""
    items.reverse()
    return items

def find_info(items, value):
    """
    Return (count, first_index_or_minus1).
    """
    count = items.count(value)
    idx = items.index(value) if value in items else -1
    return count, idx

def clear_copy(items):
    """
    Return (copy_before_clear, now_empty_list).
    """
    cpy = items.copy()
    items.clear()
    return cpy, items


# ----------------- quick checks -----------------
def _run_tests():
    data = [1, 2, 3]
    out = add_items(data, to_end=99, at_index=1, to_insert=42, extend_with=[7, 8])
    assert out == [1, 42, 2, 3, 99, 7, 8] and out is data

    animals = ["cat", "dog", "dog", "eel"]
    assert remove_safe(animals, "dog") is True and animals == ["cat", "dog", "eel"]
    assert remove_safe(animals, "cow") is False

    assert pop_last([]) is None
    assert pop_last([1, 2]) == 2

    names = ["Bob", "alice", "Carol"]
    names_sorted_ci = sorted_copy(names, key=str.lower)
    assert names_sorted_ci == ["alice", "Bob", "Carol"] and names == ["Bob", "alice", "Carol"]

    nums = [3, 2, 1]
    assert reverse_in_place(nums) == [1, 2, 3] and nums == [1, 2, 3]

    fruits = ["apple", "banana", "banana", "cherry"]
    assert find_info(fruits, "banana") == (2, 1)
    assert find_info(fruits, "mango") == (0, -1)

    tmp = [10, 20]
    before, after = clear_copy(tmp)
    assert before == [10, 20] and after == [] and tmp == []

    print("exercise_list_methods.py: all tests passed ✅")

if __name__ == "__main__":
    _run_tests()
