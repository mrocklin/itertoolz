import itertools

identity = lambda x: x

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
    key = kwargs.get('key', identity)
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

def interleave(seqs, pass_exceptions=()):
    """ Interleave a sequence of sequences

    >>> from itertoolz import interleave
    >>> list(interleave([[1, 2], [3, 4]]))
    [1, 3, 2, 4]

    >>> ''.join(interleave(('ABC', 'XY')))
    'AXBYC'

    Both the individual sequences and the sequence of sequences may be infinite

    Returns a lazy iterator
    """
    iters = itertools.imap(iter, seqs)
    while iters:
        newiters = []
        for itr in iters:
            try:
                yield next(itr)
                newiters.append(itr)
            except (StopIteration,) + tuple(pass_exceptions):
                pass
        iters = newiters


def unique(seq, key=identity):
    """ Return only unique elements of a sequence

    >>> from itertoolz import unique
    >>> tuple(unique((1, 2, 3)))
    (1, 2, 3)
    >>> tuple(unique((1, 2, 1, 3)))
    (1, 2, 3)

    Uniqueness can be defined by key keyword

    >>> def mod_10(x):
    ...     return x % 10
    >>> tuple(unique((5, 10, 15, 18, 20, 38), key=mod_10))
    (5, 10, 18)
    """
    seen = set()
    for item in seq:
        tag = key(item)
        if tag not in seen:
            seen.add(tag)
            yield item


def intersection(*seqs):
    """ Lazily evaluated intersection of sequences

    >>> from itertoolz import intersection
    >>> list(intersection([1, 2, 3], [2, 3, 4]))
    [2, 3]
    """
    return (item for item in seqs[0]
                 if all(item in seq for seq in seqs[1:]))

def iterable(x):
    """ Is x iterable?

    >>> from itertoolz import iterable
    >>> iterable([1, 2, 3])
    True
    >>> iterable('abc')
    True
    >>> iterable(5)
    False
    """
    try:
        iter(x)
        return True
    except TypeError:
        return False

def distinct(seq):
    """ All values in sequence are distinct

    >>> from itertoolz import distinct
    >>> distinct([1, 2, 3])
    True
    >>> distinct([1, 2, 1])
    False

    >>> distinct("Hello")
    False
    >>> distinct("World")
    True
    """
    return len(seq) == len(set(seq))
