def remove(predicate, coll):
    """ Return those items of collection for which predicate(item) is true.

    >>> from itertoolz import remove
    >>> def even(x):
    ...     return x % 2 == 0
    >>> remove(even, [1, 2, 3, 4])
    [1, 3]
    """
    return filter(lambda x: not predicate(x), coll)


def groupby(f, coll):
    """ Group a collection by a key function

    >>> from itertoolz import groupby
    >>> names = ['Alice', 'Bob', 'Charlie', 'Dan', 'Edith', 'Frank']
    >>> groupby(len, names)
    {3: ['Bob', 'Dan'], 5: ['Alice', 'Edith', 'Frank'], 7: ['Charlie']}
    """
    d = dict()
    for item in coll:
        key = f(item)
        if key not in d:
            d[key] = []
        d[key].append(item)
    return d
