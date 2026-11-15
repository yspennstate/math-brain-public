#!/usr/bin/env python3
"""Exact ARW absorption laws on a killed 2 x 2 lattice square, lambda=1.

An edge-mask bit means redirect that directed internal lattice edge to the
sink. All four original lattice directions retain jump probability 1/4.
No Monte Carlo, truncation, or numerical linear algebra is used.
"""

import os

for _name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
              "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_name] = "1"

import argparse
from collections import defaultdict, deque
from fractions import Fraction as F
import itertools
import json
from pathlib import Path
import resource
import signal
import sys
import time

# macOS can reject RLIMIT_AS even below its reported infinite hard limit.
# These systems have fewer than 500 states; check RSS at every completed solve.
try:
    resource.setrlimit(resource.RLIMIT_AS, (900 * 1024**2,
                                         resource.getrlimit(resource.RLIMIT_AS)[1]))
except (ValueError, OSError):
    pass
resource.setrlimit(resource.RLIMIT_CPU,
                   (1100, resource.getrlimit(resource.RLIMIT_CPU)[1]))
signal.alarm(1150)
if sys.platform == "darwin" or hasattr(os, "getpriority"):
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "Launch under nice -n 15"

from sympy import ZZ
from sympy.polys.matrices import DomainMatrix

POINTS = ((0, 0), (1, 0), (0, 1), (1, 1))
EDGES = tuple((i, j) for i, x in enumerate(POINTS)
              for j, y in enumerate(POINTS)
              if sum(abs(a-b) for a, b in zip(x, y)) == 1)
assert len(EDGES) == 8


def stable(s):
    return all(x <= 0 for x in s)


def add_particle(s, i):
    t = list(s)
    t[i] = 2 if t[i] == -1 else t[i] + 1
    return tuple(t)


def jump(s, i, j):
    t = list(s)
    assert t[i] > 0
    t[i] -= 1
    if j != -1:
        t[j] = 2 if t[j] == -1 else t[j] + 1
    return tuple(t)


def kernel(mask):
    rows = [[-1, -1] for _ in POINTS]
    for bit, (i, j) in enumerate(EDGES):
        rows[i].append(-1 if mask & (1 << bit) else j)
    return rows


def transitions(s, mask, schedule):
    """Integer event weights; -1 represents one sleeping particle.

    'first': read an instruction at the first active vertex. Sleep has
    weight 4; each jump direction has weight 1. Failed sleeps are self loops.
    'clocks': actual continuous-time ARW generator, scaled by 4. Each of
    m active particles jumps in each direction at rate m/4; a lone particle
    sleeps at rate 1. Failed sleep attempts are omitted.
    """
    assert not stable(s)
    rows = kernel(mask)
    out = defaultdict(int)
    sites = [i for i, m in enumerate(s) if m > 0]
    if schedule == "first":
        sites = sites[:1]
    for i in sites:
        m = s[i]
        if m == 1:
            t = list(s)
            t[i] = -1
            out[tuple(t)] += 4
        elif schedule == "first":
            out[s] += 4
        for j in rows[i]:
            out[jump(s, i, j)] += 1 if schedule == "first" else m
    return dict(out)


def system(initials, mask, schedule, full=False):
    """Reachable transient states and integer Dirichlet system A X = B."""
    states, seen = [], set()
    queue = deque(initials)
    trans = {}
    while queue:
        s = queue.popleft()
        if stable(s) or s in seen:
            continue
        seen.add(s)
        states.append(s)
        trans[s] = transitions(s, mask, schedule)
        queue.extend(t for t in trans[s] if not stable(t) and t not in seen)
    index = {s: i for i, s in enumerate(states)}
    width = 16 if full else 5
    a, b = [], []
    for i, s in enumerate(states):
        row, rhs = {}, {}
        row[i] = sum(trans[s].values())
        for t, w in trans[s].items():
            if stable(t):
                k = (sum((1 << j) for j, x in enumerate(t) if x == -1)
                     if full else sum(x == -1 for x in t))
                rhs[k] = rhs.get(k, 0) + w
            else:
                j = index[t]
                row[j] = row.get(j, 0) - w
        a.append({j: ZZ(v) for j, v in row.items() if v})
        b.append({j: ZZ(v) for j, v in rhs.items() if v})
    n = len(states)
    assert n < 500
    return (states, index,
            DomainMatrix(dict(enumerate(a)), (n, n), ZZ),
            DomainMatrix(dict(enumerate(b)), (n, width), ZZ))


def solve_exact(initials, mask, schedule="first", full=False):
    states, index, a, b = system(initials, mask, schedule, full)
    numerator, denominator = a.solve_den(b, method="rref")
    # Exact integer residual, checked independently of solving the equations.
    assert a.matmul(numerator) == b.scalarmul(denominator)
    rows = numerator.to_list()
    den = int(denominator)
    probs = {s: [F(int(x), den) for x in rows[i]]
             for s, i in index.items()}
    assert all(sum(v) == 1 and min(v) >= 0 for v in probs.values())
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert (rss if sys.platform == "darwin" else rss*1024) < 900*1024**2
    return probs, len(states)


def fraction_elimination(a, b):
    """Independent dense Gaussian elimination using Python fractions only."""
    n, width = a.shape[0], b.shape[1]
    aa, bb = a.to_list(), b.to_list()
    rows = [[F(int(v)) for v in aa[i] + bb[i]] for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if rows[i][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        p = rows[col][col]
        for j in range(col, n + width):
            rows[col][j] /= p
        for i in range(col+1, n):
            factor = rows[i][col]
            if factor:
                rows[i][col] = F(0)
                for j in range(col+1, n + width):
                    if rows[col][j]:
                        rows[i][j] -= factor * rows[col][j]
    x = [[F(0)] * width for _ in range(n)]
    for i in range(n-1, -1, -1):
        for k in range(width):
            x[i][k] = rows[i][n+k] - sum(
                (rows[i][j] * x[j][k] for j in range(i+1, n)
                 if rows[i][j]), F(0))
    # Recheck the original equations using fraction arithmetic, not DomainMatrix.
    for i in range(n):
        for k in range(width):
            assert sum((int(aa[i][j])*x[j][k] for j in range(n)
                        if aa[i][j]), F(0)) == int(bb[i][k])
    return x


def audit(mask, expected):
    # Different dynamics and different linear solver from the main computation.
    initials = [tuple(2 if j == i and bits & (1 << j) else
                      1 if j == i else -1 if bits & (1 << j) else 0
                      for j in range(4))
                for bits in range(16) for i in range(4)]
    initials.append((1, 1, 1, 1))
    states, index, a, b = system(initials, mask, "clocks", full=True)
    x = fraction_elimination(a, b)
    pi = x[index[(1, 1, 1, 1)]]
    law = [sum((v for bits, v in enumerate(pi) if bits.bit_count() == k), F(0))
           for k in range(5)]
    assert law == expected
    # pi must be invariant under addition at EACH of the four vertices.
    for i in range(4):
        pushed = [F(0)] * 16
        for bits, mass in enumerate(pi):
            s = tuple(-1 if bits & (1 << j) else 0 for j in range(4))
            after = add_particle(s, i)
            for t, v in enumerate(x[index[after]]):
                pushed[t] += mass * v
        assert pushed == pi
    return {"mask": mask, "transient_states": len(states),
            "clock_fraction_law": list(map(str, law)),
            "stable_configuration_law": list(map(str, pi)),
            "invariant_for_each_addition_site": True}


def tails(law):
    return [sum(law[k:], F(0)) for k in range(1, 5)]


def write_json(path, obj):
    path = Path(path)
    assert path.resolve().parent == Path(__file__).resolve().parent
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(obj, indent=2) + "\n")
    temp.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=256)
    parser.add_argument("--output", default="square_data.json")
    parser.add_argument("--audit", action="store_true")
    parser.add_argument("--audit-all", action="store_true")
    args = parser.parse_args()
    assert 1 <= args.limit <= 256
    start = time.monotonic()
    data = {"model": "killed 2x2 square in Z^2, lambda=1",
            "vertices": POINTS, "directed_edges": EDGES,
            "mask_bit": "1 redirects the corresponding edge to the sink",
            "probabilities_order": "P(S=0),...,P(S=4)",
            "nice": os.getpriority(os.PRIO_PROCESS, 0), "laws": {}}
    laws = {}
    for mask in range(args.limit):
        probs, n = solve_exact([(1, 1, 1, 1)], mask)
        law = laws[mask] = probs[(1, 1, 1, 1)]
        data["laws"][str(mask)] = {
            "probabilities": list(map(str, law)),
            "tails": list(map(str, tails(law))),
            "mean": str(sum((k*p for k, p in enumerate(law)), F(0))),
            "transient_states": n}
        write_json(args.output, data)
        if mask == 0 or (mask+1) % 32 == 0:
            print(f"masks={mask+1} elapsed={time.monotonic()-start:.3f}s "
                  f"states={n}", flush=True)
    comparisons, failures, zeros = 0, [], []
    min_gap, minimum = None, None
    for mask, law in laws.items():
        for bit in range(8):
            cut = mask | (1 << bit)
            if cut == mask or cut not in laws:
                continue
            comparisons += 1
            gaps = [x-y for x, y in zip(tails(law), tails(laws[cut]))]
            if min(gaps) < 0:
                failures.append({"mask": mask, "bit": bit,
                                 "tail_gaps": list(map(str, gaps))})
            for k, gap in enumerate(gaps, 1):
                if gap == 0:
                    zeros.append([mask, bit, k])
                if min_gap is None or gap < min_gap:
                    min_gap, minimum = gap, [mask, bit, k]
    data.update(comparisons=comparisons, failures=failures, zero_tail_gaps=zeros,
                min_tail_gap=str(min_gap), min_tail_gap_at=minimum)
    if args.limit == 256:
        assert comparisons == 1024
        # Removing every internal edge leaves four independent one-site systems.
        assert laws[255] == [F(1,16), F(4,16), F(6,16), F(4,16), F(1,16)]
        # Reflection/rotation relabelings and complementary two-edge components
        # will also be checked by an external data-only verifier.
    if args.audit or args.audit_all:
        chosen = (list(laws) if args.audit_all else
                  [m for m in (0, 1, 3, 15, 63, 85, 127, 255) if m in laws])
        data["independent_audits"] = []
        for mask in chosen:
            result = audit(mask, laws[mask])
            data["independent_audits"].append(result)
            write_json(args.output, data)
            if not args.audit_all or mask == 0 or (mask+1) % 16 == 0:
                print(f"independent audits={len(data['independent_audits'])} "
                      f"last_mask={mask} passed", flush=True)
    data["elapsed_seconds"] = time.monotonic()-start
    maxrss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    data["peak_rss_bytes"] = maxrss if sys.platform == "darwin" else maxrss*1024
    write_json(args.output, data)
    print("comparisons", comparisons, "failures", len(failures),
          "zero tail gaps", len(zeros), "min gap", min_gap)
    print("base law", list(map(str, laws[0])))
    print("base mean", data["laws"]["0"]["mean"])
    print(f"elapsed={data['elapsed_seconds']:.3f}s "
          f"peak_rss_bytes={data['peak_rss_bytes']}")
    assert not failures, "counterexample saved in data file"


if __name__ == "__main__":
    main()
