from itertoolz.recipes import frequencies

def test_frequencies():
    assert (frequencies(["cat", "pig", "cat", "eel",
                        "pig", "dog", "dog", "dog"]) ==
            {"cat": 2, "eel": 1, "pig": 2, "dog": 3})
    assert frequencies([]) == {}
    assert frequencies("onomatopoeia") == {"a": 2, "e": 1, "i": 1, "m": 1,
                                           "o": 4, "n": 1, "p": 1, "t": 1}
