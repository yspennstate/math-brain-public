import math, sys
sys.path.insert(0, r"~\AppData\Local\Temp\claude\727c9a8b9fa813fe\agent-82f2-44c5-b3e3-c0011e4a519a\scratchpad\fpp")
from et4 import words, et_exact
for n, a in ((11, 3), (12, 4)):
    e = et_exact(words(n, a))
    print("EXACT", n, a, e, round(float(e), 6), flush=True)
