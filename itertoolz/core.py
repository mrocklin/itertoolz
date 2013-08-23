import itertools
from functools import partial


identity = lambda x: x


def remove(predicate, coll):
    """ Return those items of collection for which predicate(item) is true.

    >>> def even(x):
    ...     return x % 2 == 0
    >>> list(remove(even, [1, 2, 3, 4]))
    [1, 3]
    """
    return filter(lambda x: not predicate(x), coll)


def groupby(f, coll):
    """ Group a collection by a key function

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


from itertoolz.compatibility import Queue
def merge_sorted(*iters, **kwargs):
    """ Merge and sort a collection of sorted collections

    >>> list(merge_sorted([1, 3, 5], [2, 4, 6]))
    [1, 2, 3, 4, 5, 6]

    >>> ''.join(merge_sorted('abc', 'abc', 'abc'))
    'aaabbbccc'
    """
    key = kwargs.get('key', identity)
    iters = map(iter, iters)
    pq = Queue.PriorityQueue()

    def inject_first_element(it, tiebreaker=None):
        try:
            item = next(it)
            pq.put((key(item), item, tiebreaker, it))
        except StopIteration:
            pass

    # Initial population
    for i, it in enumerate(iters):
        inject_first_element(it, i)

    # Repeatedly yield and then repopulate from the same iterator
    while not pq.empty():
        _, item, tb, it = pq.get()
        yield item
        inject_first_element(it, tb)


def merge_dict(*dicts):
    """ Merge a collection of dictionaries

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

    >>> list(interleave([[1, 2], [3, 4]]))
    [1, 3, 2, 4]

    >>> ''.join(interleave(('ABC', 'XY')))
    'AXBYC'

    Both the individual sequences and the sequence of sequences may be infinite

    Returns a lazy iterator
    """
    iters = map(iter, seqs)
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

    >>> tuple(unique((1, 2, 3)))
    (1, 2, 3)
    >>> tuple(unique((1, 2, 1, 3)))
    (1, 2, 3)

    Uniqueness can be defined by key keyword

    >>> tuple(unique(['cat', 'mouse', 'dog', 'hen'], key=len))
    ('cat', 'mouse')
    """
    seen = set()
    for item in seq:
        tag = key(item)
        if tag not in seen:
            seen.add(tag)
            yield item


def intersection(*seqs):
    """ Lazily evaluated intersection of sequences

    >>> list(intersection([1, 2, 3], [2, 3, 4]))
    [2, 3]
    """
    return (item for item in seqs[0]
                 if all(item in seq for seq in seqs[1:]))

def iterable(x):
    """ Is x iterable?

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

def take(n, seq):
    """ The first n elements of a sequence

    >>> list(take(2, [10, 20, 30, 40, 50]))
    [10, 20]
    """
    return itertools.islice(seq, n)

def drop(n, seq):
    """ The sequence following the first n elements

    >>> list(drop(2, [10, 20, 30, 40, 50]))
    [30, 40, 50]
    """
    return itertools.islice(seq, n, None)

def first(seq):
    """ The first element in a sequence

    >>> first('ABC')
    'A'
    """
    return next(iter(seq))

def nth(n, seq):
    """ The nth element in a sequence

    >>> nth(1, 'ABC')
    'B'
    """
    try:
        return seq[n]
    except TypeError:
        return next(itertools.islice(seq, n, None))

def last(seq):
    """ The last element in a sequence

    >>> last('ABC')
    'C'
    """
    try:
        return seq[-1]
    except TypeError:
        old = None
        it = iter(seq)
        while True:
            try:
                old = next(it)
            except StopIteration:
                return old


second = partial(nth, 1)
rest = partial(drop, 1)
