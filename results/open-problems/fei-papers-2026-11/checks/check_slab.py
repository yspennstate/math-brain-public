import sys, time
from fractions import Fraction as F
from itertools import combinations, product
R = r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad/zen8/toeplitz-hankel-section-profiles"
sys.path.insert(0, R + "/engine")
from exact_volume import volume_from_halfspaces

def prob(forms, d):
    # X uniform on [-1/2,1/2]^d; with Y = 2X in [-1,1]^d the event |M(X)|<=1/2 is |M(Y)|<=1
    hs = []
    for m in forms:
        hs.append((tuple(m), 1)); hs.append((tuple(-c for c in m), 1))
    return volume_from_halfspaces(hs, [(-1, 1)] * d) / 2 ** d

def forms_of(d):
    out = []
    for coeffs in product((-1, 0, 1), repeat=d):
        s = sum(1 for c in coeffs if c)
        if s >= 3 and s % 2 == 1 and sum(coeffs) == 1:
            out.append(coeffs)
    return out

mode = sys.argv[1]
if mode == "scan":
    for d in (4, 5, 6):
        L = tuple([1, 1, -1] + [0] * (d - 3))
        fs = [f for f in forms_of(d) if f != L and f != tuple(-c for c in L)]
        pairs = list(combinations(fs, 2))
        if d == 6:
            print("d=6 pairs", len(pairs)); continue
        t0 = time.time()
        vals = {}
        for M, N in pairs:
            vals[(M, N)] = prob([L, M, N], d)
        mx = max(vals.values())
        at = [k for k, v in vals.items() if v == mx]
        print(f"d={d}: pairs {len(pairs)} max {mx} attained by {len(at)} ({time.time()-t0:.0f}s)")
        for M, N in at:
            print("   ", M, N)
elif mode == "tri":
    cols = [c for c in product((-1, 0, 1), repeat=3) if any(c)]
    # multiplicity vectors: each row needs sum of mult over cols with +1 = 2 and with -1 = 1
    sols = []
    def rec(i, mult):
        if i == len(cols):
            for row in range(3):
                if sum(m for m, c in zip(mult, cols) if c[row] == 1) != 2: return
                if sum(m for m, c in zip(mult, cols) if c[row] == -1) != 1: return
            sols.append(tuple(mult)); return
        for m in range(0, 3):
            mult.append(m)
            ok = True
            for row in range(3):
                if sum(mm for mm, c in zip(mult, cols) if c[row] == 1) > 2 or sum(mm for mm, c in zip(mult, cols) if c[row] == -1) > 1:
                    ok = False
            if ok: rec(i + 1, mult)
            mult.pop()
    rec(0, [])
    def matrix(sol):
        colsx = [c for m, c in zip(sol, cols) for _ in range(m)]
        return [tuple(c[r] for c in colsx) for r in range(3)], len(colsx)
    deg = [s for s in sols if len(set(matrix(s)[0])) < 3]
    print("solutions", len(sols), "degenerate (two rows equal)", len(deg))
    good = [s for s in sols if s not in deg]
    t0 = time.time(); vals = []
    for s in good:
        rows, d = matrix(s)
        vals.append(prob(rows, d))
    vs = sorted(set(vals), reverse=True)
    print("nondegenerate", len(good), "max", vs[0], "attained", vals.count(vs[0]), "next", [str(v) for v in vs[1:6]], f"{time.time()-t0:.0f}s")
    for s, v in zip(good, vals):
        if v == vs[0]:
            print("   ", matrix(s))
