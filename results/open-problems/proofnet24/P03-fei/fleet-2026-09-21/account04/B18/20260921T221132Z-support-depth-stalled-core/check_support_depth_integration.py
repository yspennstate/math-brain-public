from fractions import Fraction
import math

def idx(bits):
    out = 0
    for i,b in enumerate(bits):
        out |= int(b) << i
    return out

def mixed_sums(vals, n):
    p_total = Fraction(0)
    o_total = Fraction(0)
    d_total = Fraction(0)
    ordered_pairs = 0
    for i in range(n):
        others = [k for k in range(n) if k != i]
        N = 1 << (n-1)
        g = [Fraction(0) for _ in range(N)]
        for y in range(N):
            bits = [0]*n
            for t,k in enumerate(others):
                bits[k] = (y >> t) & 1
            bits[i] = 0
            x0 = idx(bits)
            bits[i] = 1
            x1 = idx(bits)
            g[y] = Fraction(vals[x0] - vals[x1], 2)
        di = Fraction(0)
        for t,k in enumerate(others):
            pcount = 0
            ocount = 0
            dsq = Fraction(0)
            for y in range(N):
                u = g[y]
                v = g[y ^ (1 << t)]
                if (u != 0) != (v != 0):
                    pcount += 1
                if u != 0 and u == -v:
                    ocount += 1
                dsq += ((u-v)/2)**2
            p_total += Fraction(pcount, N)
            o_total += Fraction(ocount, N)
            di += dsq / N
            ordered_pairs += 1
        d_total += di
    M = p_total / 4
    return M, o_total, d_total, ordered_pairs

functions = 0
pair_cases = 0
for n in range(1,5):
    N = 1 << n
    local = 0
    for mask in range(1 << (N-1)):  # quotient by global output sign: vals[0]=+1
        vals = [1] + [1 if ((mask >> (x-1)) & 1) else -1 for x in range(1,N)]
        M,O,D,pairs = mixed_sums(vals,n)
        assert D == M + O, (n, mask, M, O, D)
        local += 1
        pair_cases += pairs
    functions += local
    print(f"n={n} functions_mod_sign={local}")

eps = Fraction(1,16)
load_constant = Fraction(2,1) / (1 - 2*eps)
assert load_constant == Fraction(16,7)

# Scalar certificate diagnostics. The analytic proof in REPORT.md is all-r.
min_ratio = (float("inf"), None)
for r in range(1,41):
    q = 2.0**(-r)
    jmax = min(0.5, q*(1.0 + 1.0/(16.0*r)))
    h = -jmax*math.log2(jmax) - (1-jmax)*math.log2(1-jmax)
    ratio = h/(r*jmax)
    if ratio < min_ratio[0]:
        min_ratio = (ratio, r)
    assert ratio > 1.0

gamma = Fraction(14,15)
generic_crossing_constant = 9*12/(2*float(gamma))
print("PASS support-depth integration checker")
print("functions_mod_sign_total", functions)
print("ordered_derivative_pair_cases", pair_cases)
print("identity", "D_total = M_support + O_opposite_sign")
print("robust_load_constant_eps_1_16", f"{load_constant.numerator}/{load_constant.denominator}")
print("C12_crossing_gamma", f"{gamma.numerator}/{gamma.denominator}")
print("C12_direct_critical_ratio_cap", 12)
print("generic_crossing_compiler_ratio_cap", generic_crossing_constant)
print("min_h2_over_rj_r_1_40", repr(min_ratio[0]), "at_r", min_ratio[1])
