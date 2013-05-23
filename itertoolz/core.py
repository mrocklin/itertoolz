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

from Queue import PriorityQueue
def merge_sorted(*iters, **kwargs):
    """ Merge and sort a collection of sorted collections

    >>> from itertoolz import merge_sorted
    >>> list(merge_sorted([1, 3, 5], [2, 4, 6]))
    [1, 2, 3, 4, 5, 6]

    >>> ''.join(merge_sorted('abc', 'abc', 'abc'))
    'aaabbbccc'
    """
    key = kwargs.get('key', lambda x: x)
    iters = map(iter, iters)
    pq = PriorityQueue()

    def inject_first_element(it):
        try:
            item = next(it)
            pq.put((key(item), item, it))
        except StopIteration:
            pass

    # Initial population
    for it in iters:
        inject_first_element(it)

    # Repeatedly yield and then repopulate from the same iterator
    while not pq.empty():
        _, item, it = pq.get()
        yield item
        inject_first_element(it)

def merge_dict(*dicts):
    """ Merge a collection of dictionaries

    >>> from itertoolz import merge_dict
    >>> merge_dict({1: 'one'}, {2: 'two'})
    {1: 'one', 2: 'two'}

    Later dictionaries have precedence

    >>> merge_dict({1: 2, 3: 4}, {3: 3, 4: 4})
    {1: 2, 3: 3, 4: 4}
    """
    rv = dict()
    for d in dicts:
        rv.update(d)
    return rv
