

def hash_basic(s):
    """Simple integer hash for string s."""
    return sum(ord(ch) for ch in s)


def make_set(m):
    """Return a new set table with m empty buckets."""
    return [[] for _ in range(m)]


def add(s, key):
    """Add key to set s. Return True if added, False if already present."""
    index = hash_basic(key) % len(s)
    bucket = s[index]

    if key in bucket:
        return False  # already present
    bucket.append(key)
    return True


def contains(s, key):
    """Return True if key is in set s, else False."""
    index = hash_basic(key) % len(s)
    bucket = s[index]
    return key in bucket


def remove(s, key):
    """Remove key from set s. Return True if removed, False if not present."""
    index = hash_basic(key) % len(s)
    bucket = s[index]
    try:
        bucket.remove(key)
        return True
    except ValueError:
        return False


def size(s):
    """Return total number of keys in set s."""
    return sum(len(bucket) for bucket in s)


if __name__ == "__main__":
    # Optional manual check
    event_set = make_set(5)
    print(add(event_set, "evt1"))  # True
    print(add(event_set, "evt2"))  # True
    print(add(event_set, "evt1"))  # False
    print(contains(event_set, "evt2"))  # True
    print(remove(event_set, "evt1"))  # True
    print(size(event_set))  # 1
