#!/usr/bin/env python3
from fractions import Fraction
from math import log2
import json


def phi(t):
    return 0.0 if t == 0 else -t * log2(t)


def walsh(vals):
    N = len(vals)
    n = N.bit_length() - 1
    assert 1 << n == N
    out = []
    for a in range(N):
        s = 0
        for x, v in enumerate(vals):
            s += v * (-1 if ((a & x).bit_count() & 1) else 1)
        out.append(Fraction(s, N))
    return out


def entropy_influence(coeff):
    H = 0.0
    I = 0.0
    for a, c in enumerate(coeff):
        if c:
            p = float(c*c)
            H += phi(p)
            I += a.bit_count() * p
    return H, I


def selector_values(d):
    return [-1 if x == 0 else 1 for x in range(1 << d)]


def selector_lift(d, hvals):
    m = len(hvals).bit_length() - 1
    out = []
    for z in range(1 << (d+m)):
        x = z & ((1 << d) - 1)
        y = z >> d
        out.append(hvals[y] if x == 0 else 1)
    return out


def R(q):
    m = 1 - 2*q
    return phi((1-q)**2) + phi(q*q) - 0.5*phi(m*m) + 4*q*(1-q)


def gate_ratio(d):
    eps = 2.0**(-d)
    gate = phi((1-eps)**2) + 4*d*eps - 2*d*eps*eps
    return gate/(d*eps)


def selector_formula(d, Hh, Ih):
    eps = 2.0**(-d)
    A = gate_ratio(d)
    H = eps*(d*A + Hh)
    I = eps*(d + Ih)
    return H, I, A


# Balanced quadratic phase h(y)=(-1)^(y1*y2+y3).
hvals = []
for y in range(8):
    y1, y2, y3 = (y >> 0)&1, (y >> 1)&1, (y >> 2)&1
    q = (y1*y2) ^ y3
    hvals.append(-1 if q else 1)
hc = walsh(hvals)
Hh, Ih = entropy_influence(hc)
assert sum(hvals) == 0
assert Hh == 2.0 and Ih == 2.0
assert sorted(abs(c) for c in hc if c) == [Fraction(1,2)]*4

bruteforce = []
for d in range(1,5):
    fc = walsh(selector_lift(d, hvals))
    H, I = entropy_influence(fc)
    Hp, Ip, A = selector_formula(d, Hh, Ih)
    assert abs(H-Hp) < 1e-13
    assert abs(I-Ip) < 1e-13
    bruteforce.append({
        "d": d, "H": H, "I": I, "ratio": H/I,
        "formula_H": Hp, "formula_I": Ip, "selector_cost_ratio": A
    })

# Exact identity K(s)=H(s)/2+R(q) for one-point selectors.
identity = []
for d in range(1,9):
    sc = walsh(selector_values(d))
    Hs, Is = entropy_influence(sc)
    eps = 2.0**(-d)
    K = 0.5*Hs + R(eps)
    A = gate_ratio(d)
    assert abs(K/(Is/2.0) - A) < 2e-13
    identity.append({"d": d, "Hs": Hs, "Is": Is, "K": K, "A": A})

Avals = [(d, gate_ratio(d)) for d in range(1,257)]
dmax, Amax = max(Avals, key=lambda z:z[1])

# Rigorous analytic 4.6 bound certificate.
# ln 2 = 2 * sum_{j>=0} 1/((2j+1)3^(2j+1)); first three terms suffice.
ln2_lower = Fraction(2,3) + Fraction(2,81) + Fraction(2,1215)
assert ln2_lower > Fraction(69,100)
L = Fraction(69,100)
bounds = {}
for d in range(1,5):
    eps = Fraction(1, 1 << d)
    B = Fraction(4,1) - 2*eps + 2*(1-eps)/(d*L)
    assert B < Fraction(46,10)
    bounds[str(d)] = float(B)
tail = Fraction(4,1) + Fraction(2,1)/(5*L)
assert tail < Fraction(46,10)

# Balanced-hypothesis boundary: unbalanced two-bit one-point defect h_u.
# With a two-bit one-point selector, the lift is the four-bit one-point defect.
hu = selector_values(2)
Hhu, Ihu = entropy_influence(walsh(hu))
fu = selector_lift(2, hu)
Hfu, Ifu = entropy_influence(walsh(fu))
Hfalse, Ifalse, _ = selector_formula(2, Hhu, Ihu)
assert abs(sum(hu)/len(hu) - 0.5) < 1e-15
assert abs(Hfu-Hfalse) > 0.5
assert abs(Ifu-Ifalse) > 0.1
assert fu == selector_values(4)

out = {
    "balanced_phase": {
        "truth_sum": sum(hvals),
        "nonzero_fourier": [str(c) for c in hc if c],
        "H": Hh, "I": Ih, "ratio": Hh/Ih
    },
    "bruteforce_selector_formula": bruteforce,
    "one_point_selector_identity": identity,
    "selector_cost_scan": {
        "d_range": [1,256], "max_d": dmax, "max_A": Amax,
        "note": "finite numerical scan only; theorem uses analytic 4.6 bound"
    },
    "analytic_4p6_certificate": {
        "ln2_lower_fraction": str(ln2_lower),
        "ln2_lower_float": float(ln2_lower),
        "case_bounds_d1_to_d4": bounds,
        "tail_d_ge_5_bound": float(tail),
        "all_below": 4.6
    },
    "unbalanced_boundary_counterexample": {
        "h_mean": sum(hu)/len(hu), "h_H": Hhu, "h_I": Ihu,
        "lift_is_four_bit_one_point_defect": fu == selector_values(4),
        "actual_H": Hfu, "actual_I": Ifu,
        "false_balanced_formula_H": Hfalse,
        "false_balanced_formula_I": Ifalse
    }
}
print(json.dumps(out, indent=2, sort_keys=True))
