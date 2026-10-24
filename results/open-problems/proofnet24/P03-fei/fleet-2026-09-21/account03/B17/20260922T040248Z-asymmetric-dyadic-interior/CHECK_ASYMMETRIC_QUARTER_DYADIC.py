#!/usr/bin/env python3
"""
Computer-assisted check for the account03/B17 asymmetric interior FEI slice.

Gate: G on five inputs.
Biases: p0 = 1/4, p1=...=p4=1/2.
Write A,B subset Q_4 for the true (-1) outputs on x0=0,1.
We exhaust all gates whose output mass r=(3|A|+|B|)/64 is one of
{1/64,1/32,1/16,1/8,1/4}.  Output/input negation gives the mirrored
high-output / p0=3/4 cases.

For the source-exact read-once base potential Gamma_RO with C0=6.4548,
all Gamma values used here are at dyadic arguments, so they are computed
from the exact AND-chain equality rather than from the unavailable NPZ.

The parent spectral weights have integer numerators over 4096:
  q_T     = (3 u_T + v_T)^2 / 4096
  q_{T+0} = 3 (u_T - v_T)^2 / 4096,
where u_T,v_T are the unnormalised Q4 Walsh sums of the two slices.

The exhaustive arithmetic is integer until evaluation of logarithms.
log2(q), q<=4096, is enclosed by a rational atanh series.  We evaluate
the midpoint in binary64 and use a deliberately loose 1e-8 global
roundoff envelope; the smallest non-equality defect is >0.0568.  Every
case inside the envelope is separately checked to be a coordinate
subcube, for which D=0 analytically by the dyadic AND-chain identity.
"""
import math
from fractions import Fraction
import numpy as np

C0Q = Fraction(16137, 2500)   # 6.4548 exactly
C0 = float(C0Q)
A_STAR = 0.2682048
CERT_EPS = 1.0e-8

def ln_bounds_ratio(num, den=1, N=35):
    """Rigorous rational enclosure of ln(num/den), for 1 <= num/den <= 2."""
    x = Fraction(num, den)
    z = (x - 1) / (x + 1)
    zz = z*z
    term = z
    s = Fraction(0)
    for j in range(N):
        s += term / (2*j + 1)
        term *= zz
    lo = 2*s
    # Positive tail, using 1/(2j+1) <= 1/(2N+1).
    rem = 2*term / ((2*N + 1) * (1 - zz))
    return lo, lo + rem

LN2_LO, LN2_HI = ln_bounds_ratio(2, 1)

def log2_bounds_int(n):
    """Rigorous rational enclosure of log2(n), n positive integer."""
    if n <= 0:
        raise ValueError(n)
    k = n.bit_length() - 1
    p2 = 1 << k
    if n == p2:
        return Fraction(k), Fraction(k)
    ly_lo, ly_hi = ln_bounds_ratio(n, p2)
    return Fraction(k) + ly_lo/LN2_HI, Fraction(k) + ly_hi/LN2_LO

LOG_BOUNDS = [None] + [log2_bounds_int(q) for q in range(1,4097)]
LOGMID = np.zeros(4097, dtype=np.float64)
max_log_mid_err = Fraction(0)
for q in range(1,4097):
    lo, hi = LOG_BOUNDS[q]
    mid = float((lo+hi)/2)
    LOGMID[q] = mid
    mf = Fraction.from_float(mid)
    err = max(abs(mf-lo), abs(hi-mf))
    if err > max_log_mid_err:
        max_log_mid_err = err

# A conservative forward-error envelope.  The exact spectra have 32
# nonnegative weights with integer numerators summing to 4096, and
# log2(q)<=12.  This bound intentionally overprices every binary64
# multiplication/summation several times.
u = 2.0**-53
derived_float_error_bound = (
    float(max_log_mid_err)               # weighted log-table error after /4096
    + 32*u*12*8                          # q*log, sum, division, subtraction
    + 64*u*C0*8                          # C0/lambda/Gamma arithmetic
)
assert derived_float_error_bound < CERT_EPS/100

def gamma_dyadic_float(k):
    """Gamma_RO(2^-k) from exact AND_k equality, using enclosed log table midpoint."""
    # H(AND_k): constant spectral numerator relative to denominator 2^(2k-2)
    den = 1 << (2*k-2)
    c = (1 << (k-1)) - 1
    q0 = c*c
    qn = 1
    # weights q0/den and 1/den (for each nonempty subset).
    # H = log2(den) - [q0 log2 q0 + (2^k-1)*1*log2(1)]/den
    H = float(2*k-2) - (q0 * LOGMID[q0]) / den
    I = k / float(1 << (k-1))
    return C0*I - H

GAMMA = {
    1: gamma_dyadic_float(6),  # r=1/64
    2: gamma_dyadic_float(5),  # r=1/32
    4: gamma_dyadic_float(4),  # r=1/16
    8: gamma_dyadic_float(3),  # r=1/8
    16: gamma_dyadic_float(2), # r=1/4
}

# h2(3/4)=2-(3/4)log2(3), so the p0 contribution minus C0 is
# lambda = C0/3 - log2(3).
LAM = C0/3.0 - LOGMID[3]

# Q4 Walsh matrix and all 2^16 slice transforms.
H4 = np.empty((16,16), dtype=np.int16)
LEVEL = np.empty(16, dtype=np.int16)
for s in range(16):
    LEVEL[s] = s.bit_count()
    for x in range(16):
        H4[s,x] = -1 if ((s & x).bit_count() & 1) else 1

MASKS = np.arange(65536, dtype=np.uint32)
VALUES = np.ones((65536,16), dtype=np.int16)
for x in range(16):
    VALUES[:,x] = np.where((MASKS >> x) & 1, -1, 1)
WALSH = (VALUES @ H4.T).astype(np.int16)
BYCOUNT = {
    k: np.array([m for m in range(65536) if m.bit_count()==k], dtype=np.uint16)
    for k in range(17)
}

PAIRS = {
    1: [(0,1)],
    2: [(0,2)],
    4: [(0,4),(1,1)],
    8: [(0,8),(1,5),(2,2)],
    16:[(0,16),(1,13),(2,10),(3,7),(4,4),(5,1)],
}

def is_coordinate_subcube(A, B):
    pts = []
    A = int(A); B = int(B)
    for y in range(16):
        if (A >> y) & 1:
            pts.append((0,y))
        if (B >> y) & 1:
            pts.append((1,y))
    if not pts:
        return False
    fixed = 0
    for j in range(5):
        vals = [(x0 if j==0 else ((y>>(j-1))&1)) for x0,y in pts]
        if all(v==vals[0] for v in vals):
            fixed += 1
    return len(pts) == (1 << (5-fixed))

total = 0
near = []
results = []
global_min_positive = float("inf")
global_max_c = -float("inf")
global_max_c_non_subcube = -float("inf")
global_max_c_two_sided = -float("inf")
poincare_fail = 0
parseval_fail = 0

for m, ab_list in PAIRS.items():
    r = m/64.0
    for a,b in ab_list:
        count = 0
        zeros = 0
        negatives = 0
        min_positive = float("inf")
        min_D = float("inf")
        max_c = -float("inf")
        for Am in BYCOUNT[a]:
            uvec = WALSH[int(Am)].astype(np.int32)
            Bs = BYCOUNT[b]
            V = WALSH[Bs.astype(np.int64)].astype(np.int32)

            q0 = (3*uvec[None,:] + V)**2
            q1 = 3*(uvec[None,:] - V)**2

            if not np.all(q0.sum(axis=1,dtype=np.int64) + q1.sum(axis=1,dtype=np.int64) == 4096):
                parseval_fail += 1

            It0n = q1.sum(axis=1,dtype=np.int64)
            In = (q0*LEVEL[None,:] + q1*(LEVEL[None,:]+1)).sum(axis=1,dtype=np.int64)

            # Exact Poincare currency numerator:
            # W = [In - 4 m(64-m)] / 16384.
            Wn = In - 4*m*(64-m)
            poincare_fail += int(np.count_nonzero(Wn < 0))

            slog = LOGMID[q0].__mul__(q0).sum(axis=1) + LOGMID[q1].__mul__(q1).sum(axis=1)
            Hspec = 12.0 - slog/4096.0
            D = C0*(In/4096.0) + LAM*(It0n/4096.0) - GAMMA[m] - Hspec
            W = Wn/16384.0

            count += len(Bs)
            total += len(Bs)
            min_D = min(min_D, float(D.min()))

            suspicious = np.where(D <= CERT_EPS)[0]
            for idx in suspicious.tolist():
                Aint = int(Am); Bint = int(Bs[idx])
                if not is_coordinate_subcube(Aint,Bint):
                    raise AssertionError(
                        f"non-subcube inside certification envelope m={m} a={a} b={b} "
                        f"A={Aint} B={Bint} D={D[idx]:.17g}"
                    )
                near.append((m,a,b,Aint,Bint,float(D[idx]),int(Wn[idx])))
                zeros += 1

            negatives += int(np.count_nonzero(D < -CERT_EPS))
            pos = D[D > CERT_EPS]
            if len(pos):
                mp = float(pos.min())
                min_positive = min(min_positive, mp)
                global_min_positive = min(global_min_positive, mp)

            ok = Wn > 0
            if np.any(ok):
                cv = -D[ok]/W[ok]
                mc = float(cv.max())
                max_c = max(max_c, mc)
                global_max_c = max(global_max_c, mc)

                # Exclude exact subcube/equality cases using the safely separated D envelope.
                ok_non = ok & (D > CERT_EPS)
                if np.any(ok_non):
                    cv_non = -D[ok_non]/W[ok_non]
                    global_max_c_non_subcube = max(global_max_c_non_subcube, float(cv_non.max()))
                    if a > 0 and b > 0:  # both physical slices nonconstant in all listed pairs
                        global_max_c_two_sided = max(global_max_c_two_sided, float(cv_non.max()))

        results.append((m,a,b,count,zeros,negatives,min_D,min_positive,max_c))

assert parseval_fail == 0
assert poincare_fail == 0
assert total == 10857979
assert len(near) == 153
assert all(is_coordinate_subcube(A,B) for _,_,_,A,B,_,_ in near)
assert global_min_positive > 0.0568
assert global_min_positive > 1000000*CERT_EPS
assert not any(row[5] for row in results)


def direct_definition_check(A, B):
    """Independent 32-point biased Walsh definition, used on a non-subcube minimizer."""
    ps = [0.25,0.5,0.5,0.5,0.5]
    mus = [1-2*p for p in ps]
    sqv = [math.sqrt(4*p*(1-p)) for p in ps]
    coeff = np.zeros(32, dtype=np.float64)
    pout = 0.0
    for x in range(32):
        x0 = x & 1
        y = x >> 1
        true = ((int(B if x0 else A) >> y) & 1) != 0
        f = -1.0 if true else 1.0
        prob = 1.0
        phi = []
        for i,p in enumerate(ps):
            bit = (x >> i) & 1
            Xi = -1.0 if bit else 1.0
            prob *= p if bit else (1-p)
            phi.append((Xi-mus[i])/sqv[i])
        if true:
            pout += prob
        for s in range(32):
            z = 1.0
            for i in range(5):
                if (s >> i) & 1:
                    z *= phi[i]
            coeff[s] += prob*f*z
    w = coeff*coeff
    H = -sum(q*math.log2(q) for q in w if q > 0)
    I = sum(s.bit_count()*w[s] for s in range(32))
    It0 = sum(w[s] for s in range(32) if s & 1)
    return pout,H,I,It0

# Independent definition-level cross-check at the smallest genuinely two-sided
# positive-defect signature: A={0,1}, B={0,2}, i.e. masks 3 and 5.
pout_x,H_x,I_x,It0_x = direct_definition_check(3,5)
D_x = C0*I_x + LAM*It0_x - GAMMA[8] - H_x
assert abs(pout_x-0.125) < 1e-15
assert abs(H_x-2.6225562489182668) < 2e-14
assert abs(I_x-0.84375) < 2e-15
assert abs(It0_x-0.09375) < 2e-15
assert abs(D_x-0.2526207033278234) < 2e-14

print("PASS asymmetric-quarter-bias dyadic-output FEI slice")
print(f"total_gates={total}")
print(f"rational_log_series_max_width={max(float(hi-lo) for lo,hi in LOG_BOUNDS[1:]):.3e}")
print(f"max_log_midpoint_error={float(max_log_mid_err):.3e}")
print(f"derived_float_error_bound={derived_float_error_bound:.3e}")
print(f"certification_envelope={CERT_EPS:.1e}")
print(f"exact_coordinate_subcube_equalities={len(near)}")
print(f"minimum_non_equality_D={global_min_positive:.15g}")
print(f"maximum_base_margin_c_over_positive_currency={global_max_c:.3e}")
print(f"maximum_base_margin_c_non_subcube={global_max_c_non_subcube:.12g}")
print(f"maximum_base_margin_c_genuinely_two_sided={global_max_c_two_sided:.12g}")
print("independent_two_sided_witness=A_mask_3,B_mask_5")
print(f"independent_witness_pout={pout_x:.15g}")
print(f"independent_witness_H={H_x:.15g}")
print(f"independent_witness_I={I_x:.15g}")
print(f"independent_witness_It0={It0_x:.15g}")
print(f"independent_witness_D={D_x:.15g}")
print("all_exact_Poincare_currency_numerators_nonnegative=True")
print("all_non_subcube_base_defects_positive=True")
print("therefore_all_live_lift_defects_nonnegative=True")
print()
print("m a b gates equalities negative_beyond_envelope min_D min_positive_D max_c")
for row in results:
    m,a,b,count,zeros,neg,minD,minpos,maxc=row
    mp="NA" if not math.isfinite(minpos) else f"{minpos:.15g}"
    mc="NA" if not math.isfinite(maxc) else f"{maxc:.15g}"
    print(m,a,b,count,zeros,neg,f"{minD:.15g}",mp,mc)
