import math, sys, numpy as np
sys.path.insert(0, r"~\AppData\Local\Temp\claude\727c9a8b9fa813fe\agent-82f2-44c5-b3e3-c0011e4a519a\scratchpad\fpp")
from fractions import Fraction as F
import itertools

def words(n, a):
    out = []
    for steps in itertools.product((1, -1), repeat=n):
        h, ok = 0, True
        for i, d in enumerate(steps):
            h += d
            if i < n - 1 and h <= -a:
                ok = False; break
        if ok and h == -a:
            out.append(''.join('U' if d == 1 else 'D' for d in steps))
    return out

def wait(pats):
    goto, fail, term = [{}], [0], [False]
    for p in pats:
        s = 0
        for c in p:
            if c not in goto[s]:
                goto.append({}); fail.append(0); term.append(False)
                goto[s][c] = len(goto) - 1
            s = goto[s][c]
        term[s] = True
    from collections import deque
    q = deque()
    for c in 'UD':
        if c in goto[0]: q.append(goto[0][c])
        else: goto[0][c] = 0
    order = []
    while q:
        s = q.popleft(); order.append(s)
        for c in 'UD':
            if c in goto[s]:
                t = goto[s][c]; fail[t] = goto[fail[s]][c]; q.append(t)
            else:
                goto[s][c] = goto[fail[s]][c]
    for s in order:
        term[s] = term[s] or term[fail[s]]
    live = [s for s in range(len(goto)) if not term[s]]
    idx = {s: i for i, s in enumerate(live)}
    N = len(live)
    A = np.eye(N); b = np.ones(N)
    for s in live:
        for c in 'UD':
            t = goto[s][c]
            if not term[t]:
                A[idx[s], idx[t]] -= 0.5
    return np.linalg.solve(A, b)[idx[0]]

paper = {3: F(8), 4: F(34, 3), 5: F(16), 6: F(296, 17), 7: F(128, 5), 8: F(68202, 2819),
         9: F(375006, 12865), 10: F(4555029, 144001), 11: F(317290872798, 8937933785),
         12: F(17663784686, 445122589)}
for n in range(3, 13):
    l = math.ceil(-math.sqrt(n))
    if (l - n) % 2: l += 1
    a = -l; W = words(n, a); e = wait(W)
    print(n, a, len(W), round(e, 6), round(float(paper[n]), 6), abs(e - float(paper[n])) < 1e-6, flush=True)
f = F(10, 100) * F(math.comb(100, 45), 2 ** 100)
print("1/f_100(10) =", round(float(1 / f), 2))
