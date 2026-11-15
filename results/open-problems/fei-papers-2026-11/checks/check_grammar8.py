import sys, json, time
from fractions import Fraction as F
from math import comb
R = r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad/zen8/toeplitz-hankel-section-profiles"
RMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10

def pmul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                out[i + j] += a * b
    return tuple(out)
def pint(p):
    return sum((c / (i + 1) for i, c in enumerate(p)), F(0))
def fw(r):
    # (1-x^r)/r + (1-(1-x)^r)/r
    c = [F(0)] * (r + 1)
    c[0] += F(1, r); c[r] -= F(1, r)
    c[0] += F(1, r)
    for i in range(r + 1):
        c[i] -= F(comb(r, i) * (-1) ** i, r)
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return tuple(c)

# states per r: set of (poly, nest) for linearly ear-free words of the class
S = {0: set()}
t0 = time.time()
best = {}
vols = {}
for r in range(1, RMAX + 1):
    st = set()
    if r >= 2:
        st.add((fw(r), False))
    # nesting a U a, U ear-free with r-1 pairs
    for p, _ in S.get(r - 1, ()):
        st.add(((pint(p),), True))
    # concatenation U V, U indecomposable (w_s or nest), V any; to avoid blowup use all splits
    for a in range(1, r):
        for p, na in S[a]:
            for q, nb in S[r - a]:
                st.add((pmul(p, q), False))
    S[r] = st
    red = {pint(p) for p, nest in st if not nest}
    vols[r] = red
    best[r] = max(red) if red else None
    print(r, "states", len(st), "max", best[r], "distinct reduced volumes", len(red), round(time.time() - t0, 1), "s", flush=True)

# coverage against complete sweeps
from collections import defaultdict
sys.path.insert(0, R + "/engine")
def reduced(pm):
    n = len(pm)
    return all(pm[i] != (i + 1) % n for i in range(n))
for n in (10, 12, 14):
    r = n // 2
    if r > RMAX:
        break
    d = json.load(open(f"{R}/data/volumes_T{n}.json"))
    true = {F(v["volume"]) for k, v in d["orbits"].items() if reduced(json.loads(k))}
    g = vols[r]
    print(f"r={r}: true reduced distinct {len(true)}, class {len(g)}, class in true {len(g & true)}, class max {max(g)}, true max {max(true)}")
