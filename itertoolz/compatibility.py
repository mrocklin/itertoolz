import sys
PY3 = sys.version_info[0] > 2

if PY3:
    import queue as Queue
else:
    import Queue
