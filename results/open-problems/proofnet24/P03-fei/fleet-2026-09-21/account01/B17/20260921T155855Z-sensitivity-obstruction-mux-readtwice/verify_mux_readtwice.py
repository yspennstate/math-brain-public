#!/usr/bin/env python3
"""Exact/small finite checks for the B17 selector-MUX FEI composition lemma.

The analytic theorem is in REPORT.md. This checker only stress-tests the
Fourier identities and the claimed H <= 6 I closure on finite Boolean examples.
No network, external corpus, or random seed is used.
"""
from fractions import Fraction
import hashlib, json, math


def fwht(a):
    a = list(map(int, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def entropy(probs):
    out = 0.0
    for q in probs:
        if q:
            x = float(q)
            out -= x * math.log2(x)
    return out


def metrics(vals):
    N = len(vals)
    n = N.bit_length()-1
    W = fwht(vals)
    p = [Fraction(w*w, N*N) for w in W]
    H = entropy(p)
    I = sum((s.bit_count()*p[s] for s in range(N)), Fraction(0))
    mu = Fraction(sum(vals), N)
    return p, H, I, mu


def phi(x):
    if x <= 0.0:
        return 0.0
    return -x * math.log2(x)


def overhead(mu, nu):
    a = float(mu)
    b = float(nu)
    Va, Vb = 1-a*a, 1-b*b
    p0 = (a+b)**2/4
    pz = (a-b)**2/4
    return Va+Vb + phi(p0)+phi(pz) - 0.5*phi(a*a)-0.5*phi(b*b)


def mux(a, b):
    """Variables ordered x-block, y-block, then selector; z=0 chooses a, z=1 b."""
    na = len(a).bit_length()-1
    nb = len(b).bit_length()-1
    vals = []
    for z in (0, 1):
        for y in range(1 << nb):
            for x in range(1 << na):
                vals.append(a[x] if z == 0 else b[y])
    return vals


# Four-bit exact obstruction to any coupling with spectral S subset Sens(X).
# f=+1 exactly at inputs 0,1,2 and -1 elsewhere.
obs_vals = [1 if x in (0,1,2) else -1 for x in range(16)]
obs_p, _, _, _ = metrics(obs_vals)
obs_q = list(obs_p)
for i in range(4):
    for A in range(16):
        if not ((A >> i) & 1):
            obs_q[A] += obs_q[A | (1 << i)]
triple = 0b0111
sens_joint_count = 0
sens_masks = []
for x in range(16):
    sm = 0
    for i in range(4):
        if obs_vals[x] != obs_vals[x ^ (1 << i)]:
            sm |= 1 << i
    sens_masks.append(sm)
    if (sm & triple) == triple:
        sens_joint_count += 1
assert obs_q[triple] == Fraction(1,32)
assert sens_joint_count == 0

# Every two-bit Boolean branch paired with every other two-bit Boolean branch.
branches = []
for mask in range(16):
    branches.append([1 if (mask >> x) & 1 else -1 for x in range(4)])

max_h_error = 0.0
max_i_error = Fraction(0)
max_ratio = (-1.0, None)
checked = 0
for ia, a in enumerate(branches):
    _, Ha, Ia, mua = metrics(a)
    for ib, b in enumerate(branches):
        _, Hb, Ib, mub = metrics(b)
        _, Hf, If, _ = metrics(mux(a, b))
        Om = overhead(mua, mub)
        pred_H = 0.5*(Ha+Hb) + Om
        pred_I = Fraction(1,2)*(Ia+Ib) + Fraction(1,2)*(1-mua*mub)
        max_h_error = max(max_h_error, abs(Hf-pred_H))
        max_i_error = max(max_i_error, abs(If-pred_I))
        assert abs(Hf-pred_H) < 1e-12
        assert If == pred_I
        assert Hf <= 6.0*float(If) + 1e-12
        d = float(1-mua*mub)
        if d > 0:
            selector_ratio = 2*Om/d  # Omega / I_selector
            if selector_ratio > max_ratio[0]:
                max_ratio = (selector_ratio, {
                    "branch_mask_a": ia,
                    "branch_mask_b": ib,
                    "mean_a": str(mua),
                    "mean_b": str(mub),
                })
        checked += 1

# Stress the analytic scalar inequality on every dyadic bias attainable by an
# 8-bit Boolean truth table. This is not used as the proof.
dyadic_max = (-1.0, None)
N = 256
for ka in range(N+1):
    mua = Fraction(2*ka-N, N)
    for kb in range(N+1):
        mub = Fraction(2*kb-N, N)
        d = float(1-mua*mub)
        if d == 0:
            continue
        r = 2*overhead(mua, mub)/d
        if r > dyadic_max[0]:
            dyadic_max = (r, (str(mua), str(mub)))
        assert r <= 6.0 + 1e-12

result = {
    "coupling_obstruction_spectral_triple_probability": str(obs_q[triple]),
    "coupling_obstruction_sensitivity_triple_probability": f"{sens_joint_count}/16",
    "coupling_obstruction_sensitivity_masks_hex": [hex(x) for x in sorted(set(sens_masks))],
    "direct_boolean_branch_pairs_checked": checked,
    "max_entropy_formula_error": max_h_error,
    "max_influence_formula_error": str(max_i_error),
    "max_selector_overhead_ratio_direct_pairs": max_ratio[0],
    "max_selector_overhead_witness_direct_pairs": max_ratio[1],
    "dyadic_bias_denominator": N,
    "max_selector_overhead_ratio_dyadic_grid": dyadic_max[0],
    "max_selector_overhead_biases_dyadic_grid": dyadic_max[1],
    "all_direct_muxes_satisfy_H_le_6I": True,
    "all_dyadic_overheads_satisfy_Omega_le_6_Iselector": True,
}
print(json.dumps(result, indent=2, sort_keys=True))
