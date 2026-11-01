#!/usr/bin/env python3
"""
R17 exact finite checker for the Chvatal-Sankoff binary LCS track.

No Monte Carlo.  All finite checks use exact integer/rational arithmetic.

Certificates:
  R17-C001: rectangular match-field parity / 3-wise but not 4-wise independence.
  R17-C002: all-k counterexample to an exact k-local suffix-boundary transition.
  R17-C003: finite-iid prediction-error floor for that state class.
  Metric: current certified interval width from published bounds.
"""
from collections import Counter
from fractions import Fraction
from itertools import product, combinations

LOWER = Fraction(792665992, 10**9)
UPPER = Fraction(826280, 10**6)
WIDTH = UPPER - LOWER
assert WIDTH == Fraction(4201751, 125000000)

def lcs_table(x, y):
    m, n = len(x), len(y)
    d = [[0]*(n+1) for _ in range(m+1)]
    for i, a in enumerate(x, 1):
        for j, b in enumerate(y, 1):
            if a == b:
                d[i][j] = d[i-1][j-1] + 1
            else:
                d[i][j] = max(d[i-1][j], d[i][j-1])
    return d

def lcs(x, y):
    return lcs_table(x, y)[-1][-1]

def hinc(x, y):
    """Target-prefix boundary increments."""
    d = lcs_table(x, y)
    m = len(x)
    return tuple(d[m][j] - d[m][j-1] for j in range(1, len(y)+1))

def vinc(x, y):
    """Source-prefix boundary increments."""
    d = lcs_table(x, y)
    n = len(y)
    return tuple(d[i][n] - d[i-1][n] for i in range(1, len(x)+1))

def state(k, x, y):
    """
    Strong k-local suffix-boundary state:
      total score,
      last k raw source letters,
      last k raw target letters,
      last k source-boundary increments,
      last k target-boundary increments.
    """
    return (
        lcs(x, y),
        tuple(x[-k:]),
        tuple(y[-k:]),
        tuple(vinc(x, y)[-k:]),
        tuple(hinc(x, y)[-k:]),
    )

def comp(w):
    return tuple(1-b for b in w)

# ----------------------------------------------------------------------
# R17-C001: true match field on a 2x2 rectangle.
# ----------------------------------------------------------------------
pat = Counter()
underlying = list(product((0,1), repeat=4))  # x1,x2,y1,y2
for x1,x2,y1,y2 in underlying:
    M = (
        int(x1 == y1),
        int(x1 == y2),
        int(x2 == y1),
        int(x2 == y2),
    )
    assert (M[0] ^ M[1] ^ M[2] ^ M[3]) == 0
    pat[M] += 1

assert len(pat) == 8
assert set(pat.values()) == {2}

# Every choice of any 3 corners is exactly uniform.
for I in combinations(range(4), 3):
    c = Counter(tuple(M[i] for i in I) for M, mult in pat.items()
                for _ in range(mult))
    assert len(c) == 8
    assert set(c.values()) == {2}

all_four = sum(mult for M,mult in pat.items() if M == (1,1,1,1))
assert Fraction(all_four, 16) == Fraction(1, 8)
assert Fraction(1, 8) != Fraction(1, 16)

# ----------------------------------------------------------------------
# R17-C002/C003: all-k local-boundary non-closure family.
# ----------------------------------------------------------------------
tested = []
for k in range(1, 65):
    U = (0,)*k
    YA = (0,1) + (0,)*k
    YB = (1,) + (0,)*(k+1)

    SA = state(k, U, YA)
    SB = state(k, U, YB)

    expected_initial = (
        k,
        (0,)*k,
        (0,)*k,
        (1,)*k,
        (1,)*(k-1) + (0,),
    )
    assert SA == expected_initial
    assert SB == expected_initial

    X = 1
    OA = state(k, U+(X,), YA)
    OB = state(k, U+(X,), YB)
    assert OA != OB

    # Explicit output formulas used in the written proof.
    if k == 1:
        assert lcs(U+(1,), YA) == 2
        assert lcs(U+(1,), YB) == 1
    else:
        assert lcs(U+(1,), YA) == k
        assert lcs(U+(1,), YB) == k
        assert hinc(U+(1,), YA)[-k:] == (0,) + (1,)*(k-2) + (0,)
        assert hinc(U+(1,), YB)[-k:] == (1,)*(k-1) + (0,)

    # Complemented witness gives a disjoint second ambiguous input.
    UC, YAC, YBC, XC = comp(U), comp(YA), comp(YB), 0
    assert state(k, UC, YAC) == state(k, UC, YBC)
    assert state(k, UC+(XC,), YAC) != state(k, UC+(XC,), YBC)

    # Each original world under iid fair U of length k, iid fair Y of
    # length k+2, and one fresh fair X has mass 2^(-2k-3).
    world_mass = Fraction(1, 2**(2*k+3))
    # A deterministic predictor must fail on one of the two equally likely
    # worlds at this shared input; complementing gives another disjoint input.
    error_floor = 2*world_mass
    assert error_floor == Fraction(1, 2**(2*k+2))
    tested.append((k, error_floor))

print("R17 exact checker")
print(f"metric_lower={LOWER} = {float(LOWER):.9f}")
print(f"metric_upper={UPPER} = {float(UPPER):.6f}")
print(f"metric_width={WIDTH} = {float(WIDTH):.9f}")
print("R17-C001 rectangle parity: PASS")
print("  support_size=8; each pattern multiplicity=2 among 16 underlying bit assignments")
print("  every 3 corners are iid Bernoulli(1/2)")
print("  P(all four match)=1/8; iid-cell model would give 1/16")
print("R17-C002 all-k k-local boundary non-closure: PASS for k=1..64")
print("  analytic witness family U=0^k, YA=010^k, YB=10^(k+1), append X=1")
print("  bit-complemented witness family also PASS")
print("R17-C003 deterministic next-state prediction error floor:")
for k in (1,2,4,8,16,32,64):
    print(f"  k={k}: floor={Fraction(1,2**(2*k+2))}")
print("  general exact floor >= 2^(-2k-2) under iid finite dimensions used by the witness")
print("ALL PASS")
