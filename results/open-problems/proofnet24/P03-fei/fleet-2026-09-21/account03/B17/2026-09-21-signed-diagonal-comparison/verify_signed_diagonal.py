#!/usr/bin/env python3
"""
Exact/small-finite verifier for the signed diagonal comparison mechanism.

Boolean convention: f:{-1,+1}^n -> {-1,+1}; spectral weights are hat f(S)^2.
All Walsh numerators, influences and collision masses are exact Fractions.
Floating logs are used only for the finite entropy stress-test; theorem proof in
REPORT.md is analytic and does not depend on this numerical sweep.
"""
from fractions import Fraction
from itertools import product
import json, math

def cube(n):
    return list(product((-1,1), repeat=n))

def vals_from_mask(n, mask):
    return [1 if ((mask >> k) & 1) else -1 for k in range(1 << n)]

def walsh(vals):
    n = (len(vals).bit_length() - 1)
    xs = cube(n)
    out = []
    den = 1 << n
    for S in range(1 << n):
        total = 0
        for f,x in zip(vals,xs):
            chi = 1
            for i in range(n):
                if (S >> i) & 1:
                    chi *= x[i]
            total += f*chi
        out.append(Fraction(total, den))
    return out

def entropy_from_coeffs(coeffs):
    h = 0.0
    for c in coeffs:
        w = float(c*c)
        if w:
            h -= w*math.log2(w)
    return h

def influence_from_coeffs(coeffs):
    return sum(Fraction(S.bit_count()) * c*c for S,c in enumerate(coeffs))

def collision_mass(coeffs, i, j):
    return sum(c*c for S,c in enumerate(coeffs)
               if ((S >> i)&1) and ((S >> j)&1))

def diagonal(vals, i, j, sigma):
    n = len(vals).bit_length() - 1
    xs = cube(n)
    lookup = dict(zip(xs, vals))
    rem = [k for k in range(n) if k != j]
    out = []
    for y in cube(n-1):
        x = [None]*n
        for k,v in zip(rem,y):
            x[k] = v
        x[j] = sigma*x[i]
        out.append(lookup[tuple(x)])
    return out

def exact_weight_multiset(coeffs):
    return sorted([c*c for c in coeffs if c])

# Boundary example A: selector. Ignore x4.
# F(x1,x2,x3,x4) = -x1 if x3=+1, and -x2 if x3=-1.
selector = []
for x1,x2,x3,x4 in cube(4):
    selector.append(-x1 if x3 == 1 else -x2)
cs = walsh(selector)
sp = walsh(diagonal(selector,0,1,+1))
sm = walsh(diagonal(selector,0,1,-1))
assert exact_weight_multiset(cs) == [Fraction(1,4)]*4
assert collision_mass(cs,0,1) == 0
assert exact_weight_multiset(sp) == [Fraction(1,1)]
assert exact_weight_multiset(sm) == [Fraction(1,1)]
assert influence_from_coeffs(cs) == Fraction(3,2)
assert influence_from_coeffs(sp) == Fraction(1,1)
assert influence_from_coeffs(sm) == Fraction(2,1)

# Boundary example B: ratio jump under both signs.
# F=x1 G(x2,x3,x4), with G=-1 if x2=+1 or (x2,x3,x4)=(-1,+1,+1), else +1.
ratio_jump = []
for x1,x2,x3,x4 in cube(4):
    G = -1 if (x2 == 1 or (x2,x3,x4) == (-1,1,1)) else 1
    ratio_jump.append(x1*G)
cr = walsh(ratio_jump)
rp = walsh(diagonal(ratio_jump,0,1,+1))
rm = walsh(diagonal(ratio_jump,0,1,-1))
target_weights = sorted([Fraction(9,16)] + [Fraction(1,16)]*7)
assert exact_weight_multiset(cr) == target_weights
assert exact_weight_multiset(rp) == target_weights
assert exact_weight_multiset(rm) == target_weights
assert influence_from_coeffs(cr) == Fraction(9,4)
assert influence_from_coeffs(rp) == Fraction(3,4)
assert influence_from_coeffs(rm) == Fraction(3,4)
assert collision_mass(cr,0,1) == Fraction(3,4)

# Finite stress-test: all 4-variable Boolean functions, fixed pair (x1,x2).
# Checks exact influence identity and the analytic entropy sandwich numerically.
tol = 2e-12
max_upper_violation = 0.0
max_lower_violation = 0.0
max_min_ratio_gain = (-1.0, None)
max_zero_collision_loss = (-1.0, None)
tested = 0
for mask in range(1 << 16):
    vals = vals_from_mask(4, mask)
    c = walsh(vals)
    H = entropy_from_coeffs(c)
    I = influence_from_coeffs(c)
    W = collision_mass(c,0,1)
    vp = diagonal(vals,0,1,+1)
    vm = diagonal(vals,0,1,-1)
    cp,cm = walsh(vp),walsh(vm)
    Hp,Hm = entropy_from_coeffs(cp),entropy_from_coeffs(cm)
    Ip,Im = influence_from_coeffs(cp),influence_from_coeffs(cm)
    assert (Ip+Im)/2 == I - 2*W
    avgH = (Hp+Hm)/2
    max_upper_violation = max(max_upper_violation, avgH-H)
    max_lower_violation = max(max_lower_violation, (H-2)-avgH)
    if I > 0 and Ip > 0 and Im > 0:
        gain = min(Hp/float(Ip), Hm/float(Im)) - H/float(I)
        if gain > max_min_ratio_gain[0]:
            max_min_ratio_gain = (gain, mask)
    if W == 0:
        loss = H-avgH
        if loss > max_zero_collision_loss[0]:
            max_zero_collision_loss = (loss, mask)
    tested += 1

assert max_upper_violation < tol
assert max_lower_violation < tol
assert max_min_ratio_gain[1] == 2040
assert max_zero_collision_loss[1] == 975
assert abs(max_zero_collision_loss[0]-2.0) < tol

Hjump = 4.0 - Fraction(9,16)*math.log2(9)
out = {
    "status":"PASS",
    "scope":"finite stress-test only; theorem is proved analytically in REPORT.md",
    "functions_tested": tested,
    "pair":"x1,x2",
    "selector_boundary": {
        "mask":975,
        "H_parent_exact":"2",
        "I_parent_exact":"3/2",
        "W12_exact":"0",
        "H_plus_exact":"0",
        "I_plus_exact":"1",
        "H_minus_exact":"0",
        "I_minus_exact":"2",
        "entropy_loss_exact":"2"
    },
    "both_sign_ratio_jump": {
        "mask":2040,
        "spectral_weights_exact":["9/16"]+["1/16"]*7,
        "H_exact":"4-(9/16)log2(9)",
        "H_decimal":Hjump,
        "I_parent_exact":"9/4",
        "W12_exact":"3/4",
        "I_plus_exact":"3/4",
        "I_minus_exact":"3/4",
        "parent_ratio":Hjump/(9/4),
        "plus_ratio":Hjump/(3/4),
        "minus_ratio":Hjump/(3/4),
        "ratio_multiplier_each_sign_exact":"3"
    },
    "exhaustive_n4_fixed_pair": {
        "max_upper_sandwich_violation":max_upper_violation,
        "max_lower_sandwich_violation":max_lower_violation,
        "max_min_both_sign_ratio_gain_mask":max_min_ratio_gain[1],
        "max_min_both_sign_ratio_gain":max_min_ratio_gain[0],
        "max_entropy_loss_among_W12_zero_mask":max_zero_collision_loss[1],
        "max_entropy_loss_among_W12_zero":max_zero_collision_loss[0]
    }
}
print(json.dumps(out, indent=2, sort_keys=True))
