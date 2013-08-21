from itertoolz.core import groupby, identity

def frequencies(seq):
    """ Find number of occurrences of each value in seq

    >>> frequencies(['cat', 'cat', 'ox', 'pig', 'pig', 'cat'])  #doctest: +SKIP
    {'cat': 3, 'ox': 1, 'pig': 2}
    """
    return dict([(k, len(v)) for k, v in groupby(identity, seq).items()])
