#!/usr/bin/env python3
"""
Exact/small exhaustive support for the B12 FEI global depth-rigidity run.

This script does two things:
1. Exhaustively checks n<=4 Boolean functions for the exact zero-depth-defect
   condition used in REPORT.md and confirms every eligible equality case is a
   one-point defect after dummy coordinates are removed.
2. Evaluates the explicit "subcube plus one point" family that refutes any
   universal positive normalized-depth-defect gap away from exact equality.

Only the Python standard library is used.
"""
from fractions import Fraction
import math


def fwht(a):
    a = list(a)
    h = 1
    n = len(a)
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def is_power_of_two(x):
    return x > 0 and (x & (x-1)) == 0


def exact_zero_defect(values, n):
    """Return (eligible, equality, active, influence_numerators)."""
    N = 1 << n
    coeff = fwht(values)
    den = N * N
    nums = []
    active = []
    equality = True
    for i in range(n):
        num = sum(coeff[s]*coeff[s] for s in range(N) if (s >> i) & 1)
        nums.append(num)
        if num:
            active.append(i)
            if 2*num > den:  # j_i > 1/2
                return False, False, active, nums
            # j_i = num / den must equal 2^{-m}; den/num is a power of two.
            if den % num:
                equality = False
                continue
            ratio = den // num
            if not is_power_of_two(ratio):
                equality = False
                continue
            m = ratio.bit_length() - 1
            znum = sum((s.bit_count()-1) * coeff[s]*coeff[s]
                       for s in range(N) if (s >> i) & 1)
            # E Z = znum/num, equality means 2 E Z = m.
            if 2*znum != m*num:
                equality = False
    if not active:
        return False, False, active, nums
    return True, equality, active, nums


def one_point_after_dummies(values, n, active):
    if not active:
        return False
    table = {}
    for x, val in enumerate(values):
        key = sum(((x >> i) & 1) << k for k, i in enumerate(active))
        if key in table and table[key] != val:
            return False
        table[key] = val
    if len(table) != (1 << len(active)):
        return False
    counts = {1: 0, -1: 0}
    for val in table.values():
        counts[val] += 1
    return min(counts.values()) == 1


def exhaustive():
    out = []
    for n in range(1, 5):
        N = 1 << n
        eligible = equality = onepoint = bad = 0
        for truthbits in range(1 << N):
            vals = [1 if ((truthbits >> x) & 1) else -1 for x in range(N)]
            ok, eq, active, _ = exact_zero_defect(vals, n)
            if not ok:
                continue
            eligible += 1
            if eq:
                equality += 1
                good = one_point_after_dummies(vals, n, active)
                onepoint += int(good)
                bad += int(not good)
        out.append((n, eligible, equality, onepoint, bad))
    return out


def subcube_plus_point_values(r, d):
    n = r+d
    N = 1 << n
    vals = []
    # minority: first r bits all zero (free d-bit subcube), plus point
    # x_0=1, x_1=...=x_{r-1}=0 and all free bits zero.
    extra = 1
    fixed_mask = (1 << r) - 1
    for x in range(N):
        in_subcube = (x & fixed_mask) == 0
        in_extra = x == extra
        vals.append(-1 if (in_subcube or in_extra) else 1)
    return vals


def spectral_metrics(values, n):
    N = 1 << n
    a = fwht(values)
    denom = N*N
    probs = [Fraction(v*v, denom) for v in a]
    H = 0.0
    I = Fraction(0, 1)
    for s,p in enumerate(probs):
        if p:
            pf = float(p)
            H -= pf * math.log2(pf)
            I += s.bit_count() * p
    infl = []
    for i in range(n):
        infl.append(sum((probs[s] for s in range(N) if (s>>i)&1), Fraction()))
    M2 = sum((s.bit_count()*(s.bit_count()-1))*probs[s] for s in range(N))
    D = float(M2) - 0.5*sum(float(j)*math.log2(1.0/float(j)) for j in infl if j)
    return H, float(I), D, [float(x) for x in infl]


def family_closed_form(r, d):
    eps = Fraction(1, 1 << d)
    a = Fraction(1, 1 << (r-1))
    j1 = a*(1-eps)
    jother = a*(1+eps)
    jfree = a*eps
    infl = [j1] + [jother]*(r-1) + [jfree]*d
    I = sum(infl, Fraction())
    num = ((1 << d)-1)*r*(r-1) + (r-1)*(r-2) + (r+d-1)*(r+d-2) + 2*d
    M2 = Fraction(num, 1 << (r+d))
    D = float(M2) - 0.5*sum(float(j)*math.log2(1.0/float(j)) for j in infl)
    return float(I), D, [float(x) for x in infl], M2


def main():
    print("EXHAUSTIVE_ZERO_DEFECT_N_LE_4")
    print("n eligible equality onepoint bad")
    rows = exhaustive()
    for row in rows:
        print(*row)
    assert all(row[-1] == 0 for row in rows)
    assert [r[2] for r in rows] == [0, 8, 40, 144]
    print("PASS equality cases: 0,8,40,144; counterexamples: 0")

    print()
    print("SUBCUBE_PLUS_POINT_R3")
    print("d n H_over_I D_over_I I max_j min_j closed_form_delta")
    for d in range(1, 13):
        r = 3
        vals = subcube_plus_point_values(r, d)
        H,I,D,inf = spectral_metrics(vals, r+d)
        Ic,Dc,infc,_ = family_closed_form(r,d)
        assert abs(I-Ic) < 1e-12
        assert max(abs(x-y) for x,y in zip(inf,infc)) < 1e-12
        assert abs(D-Dc) < 1e-10
        print(d, r+d, f"{H/I:.12f}", f"{D/I:.12f}",
              f"{I:.12f}", f"{max(inf):.12f}", f"{min(inf):.12f}",
              f"{abs(D-Dc):.3e}")
    for d in range(1, 13):
        _,_,infl,_ = family_closed_form(3,d)
        assert max(infl) <= 0.5
    print("PASS family formulas and low-influence condition for r=3,d=1..12")
    print("ASYMPTOTIC: for fixed r>=3, D/I = O_r(d^2 2^-d) -> 0")


if __name__ == "__main__":
    main()
