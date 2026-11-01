"""Exact polytope-volume verification of the specific volume claims in the
crossing-cores paper, using the frozen rational volume engine (engine/).

Checks, all in exact rational arithmetic:
  - the named extremal cores: 1212 -> 2/3; the four three-pair words -> 1/2;
    12123434 -> 9/20; 12314324 -> 11/30 (Toeplitz AND Hankel); 1234512345 -> 1/3
  - termwise Hankel=Toeplitz equality p_H(pi) = p_T(pi) for EVERY parity-mixing
    pairing at 2k = 4, 6, 8 (Theorem 4.1)
  - the five-pair reduced parity-mixing layer: 13 labelled cores, volume
    histogram {1/3:1, 13/45:5, 49/180:5, 1/4:2}, unique 1/3 core 1234512345
    (Proposition 10.2)
  - the six-pair reduced parity-mixing layer: 80 cores, maximum 23/90; the six
    cores with exactly four exceptional states form one dihedral orbit, all 23/90
  - exceptional-state counts (Definition 2.3): e(12123434) = 2; every reduced
    parity-mixing core with >= 5 pairs has >= 4 exceptional states (Cor 7.3,
    checked exhaustively at r = 5, 6)
  - Appendix A: all 54 rows of the two-slab table I_r(c)
  - Appendix B: both critical-companion tables (3/8, 17/48 / 2/5, 11/30)
  - Lemma 8.1 shape: the 1/2 rows are exactly the critical companions

Run:  python check_volumes_spot.py
"""
import sys, os
from fractions import Fraction as Fr
from itertools import permutations

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import tk_core
from exact_volume import pairing_volume_exact, volume_from_halfspaces

FAIL = []

def check(name, got, expect):
    ok = (got == expect)
    print(f"{'OK  ' if ok else 'FAIL'} {name}: {got}" + ("" if ok else f"  expected {expect}"), flush=True)
    if not ok:
        FAIL.append((name, got, expect))

def word_to_pm(w):
    """Double-occurrence word like '12123434' -> partner tuple."""
    pos = {}
    for i, ch in enumerate(w):
        pos.setdefault(ch, []).append(i)
    pm = [0] * len(w)
    for ch, (a, b) in pos.items():
        pm[a], pm[b] = b, a
    return tuple(pm)

# ------------------------------------------------------------ named volumes
check("p_T(1212) = 2/3", pairing_volume_exact(word_to_pm("1212"), "T"), Fr(2, 3))
for w in ("121323", "123123", "123132", "123213"):
    check(f"p_T({w}) = 1/2", pairing_volume_exact(word_to_pm(w), "T"), Fr(1, 2))
check("p_H(123123) = 1/2", pairing_volume_exact(word_to_pm("123123"), "H"), Fr(1, 2))
check("123123 is parity mixing", tk_core.is_parity_mixing(word_to_pm("123123")), True)
for w in ("121323", "123132", "123213"):
    check(f"{w} NOT parity mixing", tk_core.is_parity_mixing(word_to_pm(w)), False)

check("p_T(12123434) = 9/20", pairing_volume_exact(word_to_pm("12123434"), "T"), Fr(9, 20))
check("12123434 NOT parity mixing", tk_core.is_parity_mixing(word_to_pm("12123434")), False)

for kind in ("T", "H"):
    check(f"p_{kind}(12314324) = 11/30",
          pairing_volume_exact(word_to_pm("12314324"), kind), Fr(11, 30))
check("12314324 parity mixing", tk_core.is_parity_mixing(word_to_pm("12314324")), True)
check("12342143 parity mixing", tk_core.is_parity_mixing(word_to_pm("12342143")), True)
check("p_H(12342143) = 11/30", pairing_volume_exact(word_to_pm("12342143"), "H"), Fr(11, 30))
check("p_H(1234512345) = 1/3",
      pairing_volume_exact(word_to_pm("1234512345"), "H"), Fr(1, 3))

# ------------------------------------------------ Theorem 4.1 termwise equality
for n2k in (4, 6, 8):
    bad = 0
    for pm in tk_core.parity_pairings(n2k):
        if pairing_volume_exact(pm, "T") != pairing_volume_exact(pm, "H"):
            bad += 1
    check(f"Thm 4.1 termwise p_H = p_T at 2k={n2k} (violations)", bad, 0)

# --------------------------------------------------------- reduced H layers
def is_reduced(pm):
    n = len(pm)
    return all(pm[i] != (i + 1) % n and pm[i] != (i - 1) % n for i in range(n))

def exceptional_count(pm):
    """Definition 2.3: distinct open states minus the k+1 basis states."""
    n = len(pm)
    first = set()
    for i in range(n):
        if pm[i] > i:
            first.add(i)
    states = []
    cur = frozenset()
    seen_states = {cur}
    basis = {cur}
    open_set = set()
    for l in range(n):
        c = min(l, pm[l])  # pair label by first occurrence
        if l in first:
            open_set.add(c)
        else:
            open_set.discard(c)
        st = frozenset(open_set)
        seen_states.add(st)
        if l in first:
            basis.add(st)
    return len(seen_states) - len(basis)

check("e(12123434) = 2", exceptional_count(word_to_pm("12123434")), 2)
check("e(1234512345) = 4", exceptional_count(word_to_pm("1234512345")), 4)

# five-pair layer (Prop 10.2)
red5 = [pm for pm in tk_core.parity_pairings(10) if is_reduced(pm)]
check("13 labelled reduced parity-mixing five-pair cores", len(red5), 13)
hist5 = {}
third_words = []
for pm in red5:
    v = pairing_volume_exact(pm, "H")
    hist5[v] = hist5.get(v, 0) + 1
    if v == Fr(1, 3):
        third_words.append(pm)
check("five-pair volume histogram", dict(sorted(hist5.items())),
      {Fr(1, 4): 2, Fr(49, 180): 5, Fr(13, 45): 5, Fr(1, 3): 1})
check("unique 1/3 core is 1234512345",
      third_words == [word_to_pm("1234512345")]
      or [tk_core.canonical(p) for p in third_words] == [tk_core.canonical(word_to_pm("1234512345"))],
      True)
check("Cor 7.3 at r=5: all e >= 4", min(exceptional_count(p) for p in red5) >= 4, True)

# six-pair layer
red6 = [pm for pm in tk_core.parity_pairings(12) if is_reduced(pm)]
check("80 reduced parity-mixing six-pair cores", len(red6), 80)
vols6 = {}
for pm in red6:
    vols6[pm] = pairing_volume_exact(pm, "H")
check("six-pair maximum = 23/90", max(vols6.values()), Fr(23, 90))
e4 = [pm for pm in red6 if exceptional_count(pm) == 4]
check("six-pair cores with exactly 4 exceptional states", len(e4), 6)
check("all six have volume 23/90", all(vols6[p] == Fr(23, 90) for p in e4), True)
check("the six form one dihedral orbit", len({tk_core.canonical(p) for p in e4}), 1)
check("Cor 7.3 at r=6: all e >= 4", min(exceptional_count(p) for p in red6) >= 4, True)

# ------------------------------------------------------ Appendix A: 54 rows
def I_r(c, r):
    """Pr{|Z1+Z2+Z3|<=1/2, |c.Z + sum of r externals|<=1/2}, Z uniform on
    [-1/2,1/2]^(3+r).  Computed as an exact polytope volume in w = 2z."""
    d = 3 + r
    L = [1, 1, 1] + [0] * r
    M = list(c) + [1] * r
    hs = [(tuple(L), 1), (tuple(-x for x in L), 1),
          (tuple(M), 1), (tuple(-x for x in M), 1)]
    vol = volume_from_halfspaces(hs, [(-1, 1)] * d)
    return vol / 2 ** d

tableA = {
    0: {(-3, -1, -1): Fr(11, 36), (-2, -1, 0): Fr(5, 12), (-1, -1, 1): Fr(5, 12),
        (0, 1, 2): Fr(5, 12), (1, 2, 2): Fr(5, 12), (1, 3, 3): Fr(8, 27),
        (2, 2, 3): Fr(11, 36), (2, 3, 4): Fr(17, 72), (3, 3, 5): Fr(26, 135)},
    1: {(-4, -2, -2): Fr(23, 96), (-3, -2, -1): Fr(11, 36), (-2, -2, 0): Fr(17, 48),
        (-2, -1, -1): Fr(5, 12), (-2, 0, 0): Fr(17, 48), (-1, -1, 0): Fr(1, 2),
        (-1, 0, 1): Fr(5, 12), (0, 0, 2): Fr(17, 48), (0, 1, 1): Fr(1, 2),
        (0, 2, 2): Fr(17, 48), (1, 1, 2): Fr(5, 12), (1, 2, 3): Fr(11, 36),
        (2, 2, 2): Fr(17, 48), (2, 2, 4): Fr(23, 96), (2, 3, 3): Fr(29, 108),
        (2, 4, 4): Fr(41, 192), (3, 3, 4): Fr(47, 216), (3, 4, 5): Fr(13, 72),
        (4, 4, 6): Fr(89, 576)},
    2: {(-5, -3, -3): Fr(407, 2160), (-4, -3, -2): Fr(41, 180), (-3, -3, -1): Fr(583, 2160),
        (-3, -2, -2): Fr(23, 80), (-3, -1, -1): Fr(23, 80), (-2, -2, -1): Fr(17, 48),
        (-2, -1, 0): Fr(17, 48), (-1, -1, -1): Fr(9, 20), (-1, -1, 1): Fr(17, 48),
        (-1, 0, 0): Fr(9, 20), (-1, 1, 1): Fr(17, 48), (0, 0, 1): Fr(9, 20),
        (0, 1, 2): Fr(17, 48), (1, 1, 1): Fr(9, 20), (1, 1, 3): Fr(23, 80),
        (1, 2, 2): Fr(17, 48), (1, 3, 3): Fr(583, 2160), (2, 2, 3): Fr(23, 80),
        (2, 3, 4): Fr(41, 180), (3, 3, 3): Fr(13, 54), (3, 3, 5): Fr(407, 2160),
        (3, 4, 4): Fr(19, 96), (3, 5, 5): Fr(1, 6), (4, 4, 5): Fr(27, 160),
        (4, 5, 6): Fr(7, 48), (5, 5, 7): Fr(9, 70)},
}
nA = 0
badA = 0
for r, rows in tableA.items():
    for c, want in rows.items():
        got = I_r(c, r)
        nA += 1
        if got != want:
            badA += 1
            check(f"Appendix A I_{r}{c}", got, want)
if badA == 0:
    print(f"OK   Appendix A: all {nA} rows verified exactly", flush=True)
check("Appendix A row count", nA, 54)
check("Appendix A mismatches", badA, 0)

# the 1/2 rows are exactly the critical-companion sign patterns
halves = [(r, c) for r, rows in tableA.items() for c, v in rows.items() if v == Fr(1, 2)]
check("exactly two 1/2 rows, both r=1", sorted(halves),
      [(1, (-1, -1, 0)), (1, (0, 1, 1))])

# ------------------------------------------------------ Appendix B tables
# L = X1+X2-X3.  A_j = X1+X2-X_j, B_j = X1-X3+X_j, C_j = -X1+X3+X_j,
# D_j = X2-X3+X_j, E_j = -X2+X3+X_j.
def form(letter, j, d):
    v = [0] * d
    if letter == "A":
        v[0], v[1], v[j] = 1, 1, -1
    elif letter == "B":
        v[0], v[2], v[j] = 1, -1, 1
    elif letter == "C":
        v[0], v[2], v[j] = -1, 1, 1
    elif letter == "D":
        v[1], v[2], v[j] = 1, -1, 1
    elif letter == "E":
        v[1], v[2], v[j] = -1, 1, 1
    return v

def triple_prob(P, Q):
    """Pr{|L|<=1/2, |P|<=1/2, |Q|<=1/2}; P, Q integer coefficient rows."""
    d = len(P)
    L = [1, 1, -1] + [0] * (d - 3)
    hs = []
    for M in (L, P, Q):
        hs.append((tuple(M), 1))
        hs.append((tuple(-x for x in M), 1))
    return volume_from_halfspaces(hs, [(-1, 1)] * d) / 2 ** d

same = {("A", "B"): Fr(3, 8), ("A", "C"): Fr(3, 8), ("A", "D"): Fr(3, 8),
        ("A", "E"): Fr(3, 8), ("B", "C"): Fr(17, 48), ("B", "D"): Fr(3, 8),
        ("B", "E"): Fr(3, 8), ("C", "D"): Fr(3, 8), ("C", "E"): Fr(3, 8),
        ("D", "E"): Fr(17, 48)}
for (p, qv), want in same.items():
    got = triple_prob(form(p, 3, 4), form(qv, 3, 4))
    if got != want:
        check(f"Appendix B same-external {p}{qv}", got, want)
print("OK   Appendix B same-external table: all 10 entries verified", flush=True)

diff = {("A", "A"): Fr(2, 5), ("A", "B"): Fr(11, 30), ("A", "C"): Fr(11, 30),
        ("A", "D"): Fr(11, 30), ("A", "E"): Fr(11, 30), ("B", "B"): Fr(2, 5),
        ("B", "C"): Fr(2, 5), ("B", "D"): Fr(11, 30), ("B", "E"): Fr(11, 30),
        ("C", "C"): Fr(2, 5), ("C", "D"): Fr(11, 30), ("C", "E"): Fr(11, 30),
        ("D", "D"): Fr(2, 5), ("D", "E"): Fr(2, 5), ("E", "E"): Fr(2, 5)}
for (p, qv), want in diff.items():
    got = triple_prob(form(p, 3, 5), form(qv, 4, 5))
    if got != want:
        check(f"Appendix B different-external {p}{qv}", got, want)
print("OK   Appendix B different-external table: all 15 entries verified", flush=True)
check("Appendix B largest different-external entry = 2/5",
      max(diff.values()), Fr(2, 5))

print(flush=True)
if FAIL:
    print(f"*** {len(FAIL)} FAILURES ***")
    for f in FAIL:
        print("   ", f)
    sys.exit(1)
print("ALL VOLUME SPOT CHECKS PASSED")
