import sys
PY3 = sys.version_info[0] > 2

if PY3:
    import queue as Queue
    range = range
    imap = map
else:
    import Queue
    range = xrange
    from itertools import imap
