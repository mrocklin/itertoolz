from itertoolz.core import remove

def even(x):
    return x % 2 == 0
def odd(x):
    return x % 2 == 1

def test_remove():
    assert remove(even, range(5)) == filter(odd, range(5))
