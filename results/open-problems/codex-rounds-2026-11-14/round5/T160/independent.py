"""Independent certificate recomputation by bitset transitive closure."""
import csv
from fractions import Fraction as Q
import os
from pathlib import Path
import resource
import signal
import time

signal.alarm(120)
started = time.monotonic()
assert os.environ.get("OMP_NUM_THREADS") == "1"
# Data duplicated intentionally. No audit helpers are imported.
cases = [
    ("two_sources_cycle", (0,1), (2,3),
     ((0,2),(0,3),(1,2),(1,3),(2,3)),
     ((2,4),(3,4),(4,5),(2,5),(3,5)), (5,)),
    ("outer_merger", (0,1,2), (3,4,5),
     ((0,3),(1,4),(2,5)), ((3,6),(4,6),(5,6),(6,8)), (8,)),
    ("two_stage_outer_merger", (0,1,2), (3,4,5),
     ((0,3),(1,4),(2,5)), ((3,6),(4,7),(5,9),(6,7),(7,9),(9,8)), (8,)),
    ("local_return", (0,1,2), (3,4),
     ((0,3),(3,1),(2,4)), ((3,5),(4,6),(5,6),(6,8)), (8,)),
    ("cyclic_local_return", (0,1,2), (3,4,5),
     ((0,3),(3,4),(4,1),(1,5),(2,5)), ((3,6),(5,7),(6,7),(7,8)), (8,)),
    ("two_targets", (0,1,2), (3,4,5),
     ((0,3),(1,4),(2,5)), ((3,6),(4,7),(5,9),(6,7),(7,9)), (6,9)),
]


def closure(edges, size):
    rows = [1 << i for i in range(size)]
    for u, v in edges:
        rows[u] |= 1 << v
        rows[v] |= 1 << u
    for k in range(size):
        for i in range(size):
            if rows[i] & (1 << k):
                rows[i] |= rows[k]
    return rows


def selected(edges, mask):
    return [edge for j, edge in enumerate(edges) if (mask >> j) & 1]


def mass(mask, size, p):
    return p**mask.bit_count() * (1-p)**(size-mask.bit_count())


def code(rows, terminals):
    return tuple(sorted({tuple(v for v in terminals if rows[u] & (1 << v))
                         for u in terminals}))


saved = {(r["graph"], r["p"]): r for r in csv.DictReader(
    Path("certificates.csv").open(newline=""))}
checks = 0
for name, S, R, local, far, T in cases:
    # STAR has a fresh nonnegative index, different from audit.py.
    star = max(v for edge in local+far for v in edge)+1
    size = star+1
    Sbits = sum(1 << s for s in S)
    Rbits = sum(1 << v for v in R)
    Tbits = sum(1 << v for v in T)
    terminals = tuple(sorted(S+(star,)))
    for p in (Q(1,3), Q(1,2), Q(2,3)):
        b_far = b_local = bad = mismatch = Q(0)
        actual, approx = {}, {}
        for lm in range(1 << len(local)):
            le = selected(local, lm)
            lrows = closure(le, size)
            components = {lrows[s] for s in S}
            active = sorted(C for C in components if C & Rbits)
            N = len(active)
            wl = mass(lm, len(local), p)
            b_local += wl*bool(N)
            mark = (min((s for s in S if lrows[s] & Rbits)),) if N else ()
            lmarked_rows = closure(le+[(star, s) for s in mark], size)
            lcode = code(lmarked_rows, terminals)
            for fm in range(1 << len(far)):
                fe = selected(far, fm)
                rows = closure(le+fe, size)
                h = any(rows[s] & Tbits for s in S)
                if not h:
                    continue
                w = wl*mass(fm, len(far), p)
                b_far += w
                bad += w*(N >= 2)
                marked_rows = closure(le+fe+[(star, t) for t in T], size)
                fullcode = code(marked_rows, terminals)
                mismatch += w*(fullcode != lcode)
                actual[fullcode] = actual.get(fullcode, Q(0))+w
                approx[lcode] = approx.get(lcode, Q(0))+w
        partition_tv = sum(abs(actual.get(x,0)-approx.get(x,0))
                           for x in actual.keys() | approx.keys())/(2*b_far)
        # Here every edge leaving S already hits R. Failure of HR is exactly
        # that every such edge is closed, a third check of b_local.
        crossing_edges = sum((u in S and v in R) or (v in S and u in R)
                             for u, v in local)
        assert b_local == 1-(1-p)**crossing_edges
        result = dict(b_far=b_far, b_local=b_local,
                      conditional_multi_active=bad/b_far,
                      coupling_error=mismatch/b_far, partition_TV=partition_tv)
        record = saved[name, str(p)]
        assert int(record["states"]) == (1 << len(local))*(1 << len(far))
        for key, value in result.items():
            assert value == Q(record[key]), (name, p, key, value, record[key])
            checks += 1
        assert partition_tv <= mismatch/b_far <= bad/b_far <= b_local

assert len(saved) == 18
print(f"PASS: {checks} independently recomputed exact probability certificates")
print("PASS: 18 local/far product decompositions and independent closed-cut formulas")
print("PASS: 2560 configurations counted by six separate edge-count products")
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1_000_000_000
print(f"Priority: {os.getpriority(os.PRIO_PROCESS, 0)}; OMP_NUM_THREADS=1")
print(f"Elapsed seconds: {time.monotonic()-started:.3f}")
print(f"Peak RSS bytes (macOS): {rss}")
print("PASS: all independent checks")
