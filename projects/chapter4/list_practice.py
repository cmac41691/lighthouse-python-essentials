"""
Chapter 4 — Practice Set (Mini-Challenges)

Each function includes quick tests so you can confirm behavior in VS Code.
"""

def shopping_add_remove(items, to_add=None, to_remove=None):
    """
    Given a starting list:
      - append each item in to_add (if provided)
      - remove the first occurrence of each item in to_remove (if present)
    Return the final list.
    """
    items = items[:]  # work on a copy
    if to_add:
        for x in to_add:
            items.append(x)
    if to_remove:
        for x in to_remove:
            if x in items:
                items.remove(x)
    return items

def dedupe_preserve_order(items):
    """Remove duplicates while preserving first occurrence ordering."""
    seen = set()
    out = []
    for x in items:
        if x not in seen:
            out.append(x)
            seen.add(x)
    return out

def average_only_numbers(values):
    """
    Return the average of numeric values, ignoring non-numerics.
    If there are no numeric values, return None.
    """
    nums = [v for v in values if isinstance(v, (int, float))]
    if not nums:
        return None
    return sum(nums) / len(nums)

def flatten_one_level(nested):
    """
    Flatten a list one level deep:
      [[1,2], 3, [4,5]] -> [1,2,3,4,5]
    Non-list items are passed through.
    """
    out = []
    for x in nested:
        if isinstance(x, list):
            out.extend(x)
        else:
            out.append(x)
    return out

def unique_sorted_case_insensitive(names):
    """
    Return unique names sorted A->Z case-insensitively,
    but keep the first original casing seen.
    """
    seen_lower = set()
    unique = []
    for n in names:
        key = n.lower()
        if key not in seen_lower:
            unique.append(n)
            seen_lower.add(key)
    return sorted(unique, key=str.lower)

def word_frequency(text):
    """
    Return a dict {word: count} for a simple space-separated text.
    Lowercases and strips basic punctuation.
    """
    import string
    table = str.maketrans("", "", string.punctuation)
    words = text.lower().translate(table).split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


# ----------------- quick checks -----------------
def _run_tests():
    assert shopping_add_remove(["eggs"], to_add=["milk", "bread"], to_remove=["eggs"]) == ["milk", "bread"]
    assert dedupe_preserve_order([1, 2, 1, 3, 2, 4]) == [1, 2, 3, 4]
    assert average_only_numbers([10, "x", 20, None, 30]) == 20
    assert average_only_numbers(["a", None]) is None
    assert flatten_one_level([[1, 2], 3, [4, 5]]) == [1, 2, 3, 4, 5]
    assert unique_sorted_case_insensitive(["alice", "Bob", "ALICE", "carol"]) == ["alice", "Bob", "carol"]
    sample = "Spam spam eggs! SPAM? eggs."
    assert word_frequency(sample) == {"spam": 3, "eggs": 2}

    print("list_practice.py: all tests passed ✅")

if __name__ == "__main__":
    _run_tests()
