#!/usr/bin/env python3
from fractions import Fraction
import json, math

def fwht(v):
    a = list(v)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def spectral_stats(bits, n):
    N = 1 << n
    # Global-sign normalized: bit 0 = 0 means f(0)=+1.
    f = [1 if ((bits >> x) & 1) == 0 else -1 for x in range(N)]
    w = fwht(f)
    a = [z / N for z in w]
    p = [x*x for x in a]
    H = -sum(x*math.log2(x) for x in p if x > 0)
    infl = [sum(p[s] for s in range(N) if (s >> i) & 1) for i in range(n)]
    J = sum(min(q, 1-q) for q in infl)
    b = []
    kl_weighted = 0.0
    for d in range(N):
        cd = sum(p[s] * p[s ^ d] for s in range(N))
        Ad = sum(abs(a[s] * a[s ^ d]) for s in range(N))
        bd = 0.0 if cd == 0 else cd * math.log2(Ad / cd)
        b.append(bd)
        if cd > 0:
            kld = 0.0
            for s in range(N):
                num = p[s]*p[s ^ d]
                if num:
                    q = num / cd
                    e = abs(a[s]*a[s ^ d]) / Ad
                    kld += q * math.log2(q/e)
            kl_weighted += cd*kld
    B = sum(b)
    low = b[0] + sum(b[1 << i] for i in range(n))
    return H, J, B, low, kl_weighted

count = 0
max_kl_err = 0.0
max_gap = -1e99
argmax = None
for n in range(1, 5):
    N = 1 << n
    # Fix f(0)=+1 to quotient global sign.
    for tail in range(1 << (N-1)):
        bits = tail << 1
        H,J,B,low,kl = spectral_stats(bits,n)
        count += 1
        max_kl_err = max(max_kl_err, abs((B-H)-kl))
        if J > 1e-14:
            gap = H-low-4*J
            if gap > max_gap:
                max_gap = gap
                argmax = {
                    "n":n, "truth_bits_after_f0":tail,
                    "H":H, "J":J, "B":B, "B2":B-low, "low":low
                }

assert count == 32906
assert max_kl_err < 2e-12
assert max_gap < 0

# Exact L-shaped three-point defect A={0,e1,e2}, n=14.
n = 14
N = 1 << n
cH = Fraction(24*(3*N-22), N**3)
AH = Fraction(24*(N-6), N**2)
cO = Fraction(8*(N-2), N**3)
AO = Fraction(12*(N-4), N**2)
rH = AH / cH
rO = AO / cO
countH = N//4 - n + 1
countO = 3*N//4 - 2
J = Fraction(6*n-8, N)

# Strict rational lower bounds log2 rH > 62/5 and log2 rO > 29/2.
assert rH.numerator**5 > (2**62) * rH.denominator**5
assert rO.numerator**2 > (2**29) * rO.denominator**2
B2_lower = countH*cH*Fraction(62,5) + countO*cO*Fraction(29,2)
ratio_lower = B2_lower / J
assert ratio_lower > 4

# Direct floating evaluation only as a secondary magnitude check.
B2_float = countH*float(cH)*math.log2(float(rH)) + countO*float(cO)*math.log2(float(rO))
ratio_float = B2_float/float(J)

# Asymptotic ratio tends 4 from above because 26 - 12 log2 3 > 0.
assert 3**12 < 2**26

# Secondary floating accounting for the same n=14 family.
p0 = ((N-6)/N)**2
pH = (6/N)**2
pO = (2/N)**2
H_ldef = -(p0*math.log2(p0) + (N//4-1)*pH*math.log2(pH) + (3*N//4)*pO*math.log2(pO))
c0 = p0*p0 + (N//4-1)*pH*pH + (3*N//4)*pO*pO
b0 = c0*math.log2(1/c0)
bH = float(cH)*math.log2(float(rH))
bO = float(cO)*math.log2(float(rO))
low_ldef = b0 + (n-2)*bH + 2*bO
B_ldef = B2_float + low_ldef
G_ldef = B_ldef - H_ldef
refunded_ratio_ldef = (H_ldef-low_ldef)/float(J)
assert refunded_ratio_ldef < 4

out = {
    "schema_version": 1,
    "full_FEI_proved": False,
    "global_sign_symmetry_note": "One representative per global-sign pair; H,J,B,b_d and the tested inequalities are global-sign invariant.",
    "sign_normalized_boolean_functions_checked_n_le_4": count,
    "kl_slack_identity_max_abs_error": max_kl_err,
    "refunded_constant_four_candidate": {
        "statement_tested": "H(f) - b_0 - sum_i b_{e_i} <= 4 J(f)",
        "status": "FINITE_CHECK_ONLY_NOT_PROVED",
        "max_gap_over_nontrivial_sign_normalized_n_le_4": max_gap,
        "argmax": argmax
    },
    "three_point_defect_exact_certificate": {
        "n": n, "N": N,
        "q_exceptional": str(Fraction(2,N)),
        "q_bulk": str(Fraction(6,N)),
        "J": str(J),
        "c_H": str(cH), "A_H": str(AH), "A_over_c_H": str(rH),
        "c_O": str(cO), "A_O": str(AO), "A_over_c_O": str(rO),
        "count_H_multi": countH, "count_outside_H_multi": countO,
        "rigorous_log_lower_H": "62/5",
        "rigorous_log_lower_O": "29/2",
        "rigorous_B2_over_J_lower": str(ratio_lower),
        "rigorous_B2_over_J_lower_float": float(ratio_lower),
        "rigorous_excess_over_4": str(ratio_lower-4),
        "actual_B2_over_J_float": ratio_float,
        "n14_bridge_slack_G_float": G_ldef,
        "n14_refunded_ratio_(H-low)/J_float": refunded_ratio_ldef,
        "n14_H_float": H_ldef,
        "n14_low_slice_float": low_ldef,
        "asymptotic_overshoot_sign_check": "3^12 < 2^26"
    }
}
print(json.dumps(out, indent=2, sort_keys=True))
