#!/usr/bin/env python3
from math import factorial
from fractions import Fraction

NMAX = 45

def parts(n, maxp=None, pref=()):
    if n == 0:
        yield pref
        return
    if maxp is None or maxp > n:
        maxp = n
    for a in range(maxp, 0, -1):
        yield from parts(n-a, a, pref+(a,))

def hookdim(lam):
    n = sum(lam)
    f = factorial(n)
    w = lam[0]
    col = [sum(1 for x in lam if x > c) for c in range(w)]
    hp = 1
    for i, a in enumerate(lam):
        for c in range(a):
            hp *= (a-c) + (col[c]-i-1)
    assert f % hp == 0
    return f // hp

def ellrow(n):
    e = [0]*(n+1)
    pc = 0
    for lam in parts(n):
        d = hookdim(lam)
        e[lam[0]] += d*d
        pc += 1
    assert sum(e) == factorial(n)
    return e, pc

rows = {}
partcounts = {}
for n in range(1, NMAX+2):
    rows[n], partcounts[n] = ellrow(n)

def alpha_row(n):
    e = rows[n]
    e1 = rows[n+1]
    U = [0]*(n+1)
    U1 = [0]*(n+2)
    for k in range(1, n+1):
        U[k] = U[k-1] + e[k]
    for k in range(1, n+2):
        U1[k] = U1[k-1] + e1[k]
    a = {}
    for k in range(1, n+1):
        H = U1[k] - (n+1)*U[k-1]
        assert e[k] <= H <= n*e[k]
        a[k] = Fraction(H, (n+1)*e[k])
        Hprev = U1[k-1] - (n+1)*U[k-2] if k >= 2 else 0
        assert e1[k] == H + (n+1)*e[k-1] - Hprev
    return a

negative_cells = 0
one_sided_passes = 0
row_min = {}
global_min = None

for n in range(4, NMAX+1):
    e = rows[n]
    e1 = rows[n+1]
    a = alpha_row(n)
    p = [Fraction(v, factorial(n)) for v in e]
    q = [Fraction(v, factorial(n+1)) for v in e1]
    for k in range(3, n):
        x = p[k-1]
        y = p[k]
        r = y/x
        P = (a[k]*r + (1-a[k-1]))**2 \
            - (a[k-1]*r + (1-a[k-2]))*(a[k+1]*r + (1-a[k]))
        if P < 0:
            negative_cells += 1
            Delta_plus = y*y - x*p[k+1]
            assert Delta_plus >= 0
            V = a[k+1]*Delta_plus/x
            base = x*x*P
            rescue = V*q[k-1]
            slack = base + rescue
            assert rescue >= -base
            one_sided_passes += 1
            ratio = rescue/(-base)
            rec = (ratio, n, k, P, base, rescue, slack)
            if global_min is None or rec < global_min:
                global_min = rec
            if n not in row_min or ratio < row_min[n][0]:
                row_min[n] = rec

assert global_min is not None
ratio, n0, k0, P0, base0, rescue0, slack0 = global_min
assert (n0, k0) == (5, 4)
assert ratio == Fraction(15230475, 14585989)
assert P0 == Fraction(-14585989, 335023956)
assert base0 == Fraction(-14585989, 1296518400)
assert rescue0 == Fraction(1651, 140544)
assert slack0 == Fraction(322243, 648259200)

# A potentially useful empirical monovariant: after the sporadic n=5 minimum,
# the minimum one-sided rescue ratio across negative-envelope cells rises row by row.
for n in range(5, NMAX):
    if n in row_min and n+1 in row_min:
        assert row_min[n+1][0] > row_min[n][0]

print("P0282 exact one-sided curvature-rescue checker")
print(f"NMAX={NMAX} rows_rebuilt=1..{NMAX+1} total_partition_shapes={sum(partcounts.values())}")
print(f"negative_geometric_envelope_cells={negative_cells}")
print(f"right_curvature_only_rescue_passes={one_sided_passes}/{negative_cells}")
print(f"global_min_cell=n{n0}_k{k0}")
print(f"global_min_ratio_exact={ratio}")
print(f"global_min_ratio_decimal={float(ratio):.18f}")
print(f"global_min_P_exact={P0}")
print(f"global_min_base_exact={base0}")
print(f"global_min_right_rescue_exact={rescue0}")
print(f"global_min_slack_exact={slack0}")
print(f"row_min_ratio_strictly_increasing_n5_to_{NMAX}=True")
print(f"row5_min_ratio={row_min[5][0]}")
print(f"row{NMAX}_min_ratio={row_min[NMAX][0]}")
print("FINITE_EVIDENCE_ONLY_NOT_ALL_N_THEOREM=True")
print("ALL_EXACT_CHECKS_PASS")
