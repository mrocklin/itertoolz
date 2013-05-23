from itertoolz.core import remove, groupby, merge_sorted, merge_dict

def even(x):
    return x % 2 == 0
def odd(x):
    return x % 2 == 1

def test_remove():
    assert remove(even, range(5)) == filter(odd, range(5))

def test_groupby():
    assert groupby(even, [1, 2, 3, 4]) == {True: [2, 4], False: [1, 3]}

def test_merge_sorted():
    assert list(merge_sorted([1,2,3], [1,2,3])) == [1,1,2,2,3,3]
    assert list(merge_sorted([1,3,5], [2,4,6])) == [1,2,3,4,5,6]
    assert list(merge_sorted([1], [2, 4], [3], [])) == [1, 2, 3, 4]

def test_merge_dict():
    assert merge_dict({1: 1, 2: 2}, {3: 4}) == {1: 1, 2: 2, 3: 4}
