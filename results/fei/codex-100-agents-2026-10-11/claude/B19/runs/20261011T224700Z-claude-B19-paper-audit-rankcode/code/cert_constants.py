# Exact/interval certificates for the numerical constants of main.tex Theorem A/B and the selector corollaries.
import json, sys
from fractions import Fraction as Fr
from math import factorial
out = {}
# --- rational enclosure of e: sum_{k<=N} 1/k! <= e <= that + 2/(N+1)!
N = 40
e_lo = sum(Fr(1, factorial(k)) for k in range(N+1)); e_hi = e_lo + Fr(2, factorial(N+1))
# --- rational enclosure of pi by Machin: pi = 16 atan(1/5) - 4 atan(1/239); alternating series brackets
def atan_bracket(x, K):
    s = Fr(0); partial = []
    for k in range(K+2):
        s += Fr((-1)**k) * x**(2*k+1) / (2*k+1); partial.append(s)
    a, b = partial[-2], partial[-1]
    return (min(a, b), max(a, b))
a5 = atan_bracket(Fr(1,5), 40); a239 = atan_bracket(Fr(1,239), 12)
pi_lo = 16*a5[0] - 4*a239[1]; pi_hi = 16*a5[1] - 4*a239[0]
assert pi_lo < pi_hi and e_lo < e_hi
out['e_interval_width'] = float(e_hi - e_lo); out['pi_interval_width'] = float(pi_hi - pi_lo)
# C_reg = log2((4+e) e^2 pi^2).  C_reg < 8.937  <=>  ((4+e)e^2 pi^2)^1000 < 2^8937
X_hi = (4 + e_hi) * e_hi**2 * pi_hi**2; X_lo = (4 + e_lo) * e_lo**2 * pi_lo**2
upper_ok = X_hi.numerator**1000 < (2**8937) * X_hi.denominator**1000
lower_ok = X_lo.numerator**1000 > (2**8936) * X_lo.denominator**1000
out['C_reg_lt_8.937_exact_rational'] = upper_ok
out['C_reg_gt_8.936_exact_rational'] = lower_ok
# tighter decimal location: 8.9364 < C_reg < 8.9366 via 10^4 powers
up2 = X_hi.numerator**10000 < (2**89366) * X_hi.denominator**10000
lo2 = X_lo.numerator**10000 > (2**89364) * X_lo.denominator**10000
out['C_reg_in_(8.9364,8.9366)_exact_rational'] = bool(up2 and lo2)
# --- interval arithmetic (mpmath iv, outward rounding) for all closure constants
import mpmath
from mpmath import iv
iv.dps = 50
E = iv.mpf([str(e_lo.numerator/ e_lo.denominator) if False else 0, 0])
def ivfr(lo, hi):
    return iv.mpf([mpmath.mpf(lo.numerator)/lo.denominator, mpmath.mpf(hi.numerator)/hi.denominator])
mpmath.mp.dps = 60
E = ivfr(e_lo, e_hi); PI = ivfr(pi_lo, pi_hi)
LN2 = iv.log(iv.mpf(2))
# Euler gamma enclosure (Euler-Maclaurin, remainder of alternating definite sign for f(x)=1/x):
#   H_n - ln n - 1/(2n) + 1/(12n^2) - 1/(120n^4) < gamma < H_n - ln n - 1/(2n) + 1/(12n^2)
# plus the elementary bracket H_n - ln n - 1/(2n) < gamma < H_n - ln n - 1/(2(n+1)) as a second, weaker method.
n = 2000
Hn = iv.mpf(0)
for k in range(1, n+1): Hn += iv.mpf(1)/k
lnn = iv.log(iv.mpf(n))
base = Hn - lnn - iv.mpf(1)/(2*n)
g_lo = (base + iv.mpf(1)/(12*n**2) - iv.mpf(1)/(120*n**4)).a; g_hi = (base + iv.mpf(1)/(12*n**2)).b
el_lo = base.a; el_hi = (Hn - lnn - iv.mpf(1)/(2*(n+1))).b
assert el_lo <= g_lo and g_hi <= el_hi
out['gamma_mpmath_reference_inside'] = bool(g_lo < mpmath.euler < g_hi)
G = iv.mpf([g_lo, g_hi])
log2 = lambda z: iv.log(z)/LN2
Clev = log2(4 + E); Creg = Clev + 2*log2(E*PI)
Lp = 1 + LN2; Lmix = 2 + G
a = iv.mpf(6)/5
C_ord = Clev + (1 + iv.log(a/(a-1)) + a*Lmix)/LN2          # m-independent part of (ordinaryexact)
C_mul = Clev + (1 + iv.log(iv.mpf(7)) + a*Lmix)/LN2       # m-independent part of (cm)
CT = 80 + 460/LN2
def s(x): return [mpmath.nstr(x.a, 15), mpmath.nstr(x.b, 15)]
out['gamma_interval'] = s(G)
out['C_lev'] = s(Clev); out['C_reg'] = s(Creg)
out['C_reg_lt_8.937_iv'] = bool(Creg.b < mpmath.mpf('8.937'))
out['C_reg_gt_4_iv'] = bool(Creg.a > 4)
out['2Lp_plus_ln(pi^2/4)_over_ln2_equals_2log2(e*pi)'] = s((2*Lp + iv.log(PI**2/4))/LN2 - 2*log2(E*PI))
out['C_ord(a=6/5)'] = s(C_ord); out['C_ord_in_[11.2375133696,11.2375133697]'] = bool(C_ord.a > mpmath.mpf('11.2375133696') and C_ord.b < mpmath.mpf('11.2375133697'))
out['C_ord_width'] = mpmath.nstr(C_ord.delta, 3)
out['C_ord_lt_11.238'] = bool(C_ord.b < mpmath.mpf('11.238'))
out['C_multi(a=6/5)'] = s(C_mul); out['C_multi_lt_11.460'] = bool(C_mul.b < mpmath.mpf('11.460'))
out['log_m_coeff_ord_(1+2a)=17/5'] = str(1 + 2*Fr(6,5)); out['log_m_coeff_center_2a+2=22/5'] = str(2*Fr(6,5) + 2)
out['Creg_plus_4_lt_12.937'] = bool((Creg + 4).b < mpmath.mpf('12.937'))
out['4Creg'] = s(4*Creg)
out['C_T=80+460/ln2'] = s(CT)
out['rho=4/(4+e): log2(rho/(1-rho)) + log2 e - 2 (must be 0)'] = s(log2((4/(4+E))/(1-4/(4+E))) + log2(E) - 2)
out['2+log2(1/rho) - log2(4+e) (must be 0)'] = s(2 + log2((4+E)/4) - log2(4+E))
json.dump(out, open(sys.argv[1], 'w'), indent=1)
print(json.dumps(out, indent=1))
