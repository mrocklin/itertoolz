from itertoolz.core import remove, groupby

def even(x):
    return x % 2 == 0
def odd(x):
    return x % 2 == 1

def test_remove():
    assert remove(even, range(5)) == filter(odd, range(5))

def test_groupby():
    assert groupby(even, [1, 2, 3, 4]) == {True: [2, 4], False: [1, 3]}
