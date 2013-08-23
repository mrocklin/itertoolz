Itertoolz
=========

More useful tools for Python iterators.  A set of common utility functions.

[![Build Status](https://travis-ci.org/mrocklin/itertoolz.png)](https://travis-ci.org/mrocklin/itertoolz)


Relationship to `itertools`
---------------------------

The `itertools` package (with an `s`) is a package in the standard library.  It differs from `itertoolz` (with a `z`) in the following ways.

*   `itertools` has an `s`.  `itertoolz` has a `z`.
*   `itertools` is strictly a library of [*streaming algorithms*](http://en.wikipedia.org/wiki/Streaming_algorithm) while `itertoolz` accepts functions that require finite iterators.
*   `itertools` changes very slowly and is managed by the official Python community (you submit a `PEP`).  `itertoolz` is more loose (you submit a pull request)
*   `itertools` is minimal.  `itertoolz` accepts recipes.

Author
------

[Matthew Rocklin](http://matthewrocklin.com)

LICENSE
-------

New BSD.  See [License File](LICENSE.TXT).

Install
-------

`itertoolz` is on the Python Package Index (PyPi)

    pip install itertoolz

or 
    
    easy_install itertoolz

or from source

    ./setup.py install

Dependencies
------------

`itertoolz` supports Python 2.6+ and Python 3.2+ with a common codebase.

It has no dependencies outside of the standard library.

See Also
--------

*   [`functoolz`](http://github.com/mrocklin/functoolz)
*   [`classtoolz`](http://github.com/mrocklin/classtoolz)
