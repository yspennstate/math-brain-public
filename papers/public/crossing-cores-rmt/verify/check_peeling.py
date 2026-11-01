"""Direct verification of the ear-peeling layer:

  - Proposition 3.2 (confluence): two different deletion strategies reach the
    same reduced core (same canonical dihedral representative), for every
    pairing at 2k = 8, 10, 12 and every parity-mixing pairing there
  - Proposition 3.3: empty core exactly for noncrossing pairings
  - Theorem 12.2 / (12.3): the exact law of the complete cascading deletion
    count D_k matches  Pr(D=m) = C(2k,m) c_{k-m} / N  for m <= k-2,
    0 at m = k-1, Cat_k / N at m = k  -- verified by exhaustive peeling at
    k = 4, 5, 6 for both ensembles

Run:  python -u check_peeling.py
"""
import sys, os
from math import comb, factorial

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
import tk_core

FAIL = []

def check(name, got, expect):
    ok = (got == expect)
    print(f"{'OK  ' if ok else 'FAIL'} {name}: {got}" + ("" if ok else f"  expected {expect}"), flush=True)
    if not ok:
        FAIL.append((name, got, expect))

def cat(k):
    return comb(2 * k, k) // (k + 1)

def dfact(n):
    r = 1
    while n > 1:
        r *= n
        n -= 2
    return r

def find_ears(pm):
    n = len(pm)
    return [i for i in range(n) if pm[i] == (i + 1) % n and i < pm[i] or
            (pm[i] == 0 and i == n - 1)]

def delete_ear(pm, i):
    """Delete the ear at slots (i, i+1 mod n), keep induced cyclic order."""
    n = len(pm)
    j = (i + 1) % n
    keep = [s for s in range(n) if s != i and s != j]
    relabel = {s: t for t, s in enumerate(keep)}
    out = [0] * (n - 2)
    for s in keep:
        out[relabel[s]] = relabel[pm[s]]
    return tuple(out)

def peel(pm, strategy):
    """Complete cascade; strategy 'first' deletes the lowest-index ear,
    'last' the highest.  Returns (deleted_pairs, core)."""
    deleted = 0
    cur = pm
    while len(cur):
        ears = find_ears(cur)
        if not ears:
            break
        i = ears[0] if strategy == "first" else ears[-1]
        cur = delete_ear(cur, i)
        deleted += 1
    return deleted, cur

def reduced_count(r, kind):
    if r == 0:
        return 1
    if r == 1:
        return 0
    def qq(rr, j):
        from fractions import Fraction as Fr
        return (2 * rr * comb(2 * rr - j, j)) // (2 * rr - j)
    if kind == "T":
        return sum((-1) ** j * qq(r, j) * dfact(2 * r - 2 * j - 1) for j in range(r + 1))
    return sum((-1) ** j * qq(r, j) * factorial(r - j) for j in range(r + 1))

for k in (4, 5, 6):
    n2k = 2 * k
    for kind in ("T", "H"):
        gen = tk_core.all_pairings(n2k) if kind == "T" else tk_core.parity_pairings(n2k)
        histo = {}
        confl_bad = 0
        empty_ok = True
        for pm in gen:
            d1, c1 = peel(pm, "first")
            d2, c2 = peel(pm, "last")
            if d1 != d2 or (len(c1) != len(c2)) or \
               (len(c1) and tk_core.canonical(c1) != tk_core.canonical(c2)):
                confl_bad += 1
            histo[d1] = histo.get(d1, 0) + 1
            if (len(c1) == 0) != (not tk_core.is_crossing(pm)):
                empty_ok = False
        check(f"k={k} {kind}: confluence violations", confl_bad, 0)
        check(f"k={k} {kind}: empty core iff noncrossing", empty_ok, True)
        N = dfact(2 * k - 1) if kind == "T" else factorial(k)
        want = {}
        for m in range(0, k - 1):
            c = reduced_count(k - m, kind)
            if c:
                want[m] = comb(2 * k, m) * c
        want[k] = cat(k)
        check(f"k={k} {kind}: exact peeling law (12.3)", histo, want)
        check(f"k={k} {kind}: no mass at m=k-1", histo.get(k - 1, 0), 0)

print(flush=True)
if FAIL:
    print(f"*** {len(FAIL)} FAILURES ***")
    for f in FAIL:
        print("   ", f)
    sys.exit(1)
print("ALL PEELING CHECKS PASSED")
