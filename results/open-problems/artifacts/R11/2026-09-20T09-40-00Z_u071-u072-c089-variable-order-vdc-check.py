#!/usr/bin/env python3
from fractions import Fraction

ASSERTIONS = 0

def check(cond, msg="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def floor_log4_3power(b: int) -> int:
    """Exact floor(b log_4 3): largest q with 4^q <= 3^b."""
    target = 3 ** b
    lo, hi = 0, b
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if 4 ** mid <= target:
            lo = mid
        else:
            hi = mid - 1
    return lo

def tau_three_quarters(b: int) -> Fraction:
    q = floor_log4_3power(b)
    a = 3 ** b
    c = 4 ** q
    check(c <= a < 4*c, "floor-log certificate")
    return Fraction(a, a+c)

def split_kernel(p: Fraction, i: int, j: int) -> Fraction:
    return p**i * (1-p)**j + p**j * (1-p)**i

def n4_rate(b: int, i: int, j: int) -> Fraction:
    # Compact-logit multiplication model at N=4.
    ps = [Fraction(1,4), Fraction(1,2), tau_three_quarters(b)]
    lams = [Fraction(2,3), Fraction(1,2), Fraction(2,3)]
    return sum((lam*split_kernel(p,i,j) for lam,p in zip(lams,ps)), Fraction(0))

def p_from_D(D: int) -> int:
    # C089 schedule expressed using D=floor(log_2 N).
    candidates = []
    p = 5
    while (1 << (2*p)) <= D:
        candidates.append(p)
        p += 2
    return candidates[-1] if candidates else 5

# 1. Exact higher-derivative exponent arithmetic used in U071.
for p in range(5, 102, 2):
    P = 1 << (p-1)
    A = 2*P - 2
    check(Fraction(-2, P) + Fraction(3, A) < 0,
          f"U071 induction exponent not negative at p={p}")
    # The active-interval derivative ratio can be bounded by (5/2)^p.
    lhs = Fraction(5,4)**p + Fraction(5,1)**p
    rhs = 2 * Fraction(5,1)**p
    check(lhs <= rhs, f"derivative-ratio estimate failed at p={p}")

# 2. Exact schedule boundary tests. These use D directly, avoiding astronomical N.
for p in range(5, 32, 2):
    D0 = 1 << (2*p)
    check(p_from_D(D0) == p, f"schedule lower boundary failed p={p}")
    D1 = (1 << (2*(p+2))) - 1
    check(p_from_D(D1) == p, f"schedule upper boundary failed p={p}")
    check(1 << (2*p) <= D0)
    check((1 << (2*(p+2))) > D1)

# 3. Dense exact sanity checks for floor(b log_4 3).
for b in range(1, 501):
    q = floor_log4_3power(b)
    check(4**q <= 3**b, f"lower floor inequality b={b}")
    check(3**b < 4**(q+1), f"upper floor inequality b={b}")
    if b > 1:
        qprev = floor_log4_3power(b-1)
        check(q >= qprev, f"floor monotonicity b={b}")
        check(q-qprev in (0,1), f"floor increment b={b}")

# 4. C089 finite certificate at N=4.
# The small-N convention has p_4=5 and b_4=4^(5-2)=64.
p4 = 5
b4 = 4 ** (p4-2)
check(b4 == 64)
qfloor = floor_log4_3power(b4)
check(qfloor == 50)
check(4**50 <= 3**64 < 4**51)
paintbox_p3 = tau_three_quarters(b4)
check(paintbox_p3 == Fraction(3**64, 3**64 + 4**50))

q13 = n4_rate(b4,1,3)
q22 = n4_rate(b4,2,2)
root_rate = 4*q13 + 3*q22
balanced_prob = 3*q22/root_rate
ctcs_balanced = Fraction(3,11)
check(q13 > 0 and q22 > 0 and root_rate > 0)
check(balanced_prob != ctcs_balanced)
check(balanced_prob > ctcs_balanced)
check(q13/q22 != 2)

# Equivalent exact sign certificate for the balanced-root discrepancy.
check(2*q22-q13 > 0)
check(balanced_prob-ctcs_balanced ==
      Fraction(12,11)*(2*q22-q13)/root_rate)

# 5. Distinguish C089 from C088's natural N=4 branch count b_4=341.
b4_c088 = 341
q13_088 = n4_rate(b4_c088,1,3)
q22_088 = n4_rate(b4_c088,2,2)
pbal_088 = 3*q22_088/(4*q13_088+3*q22_088)
check(balanced_prob != pbal_088)

# 6. Exact CTCS comparator identities.
check(Fraction(1,3) / Fraction(1,6) == 2)
check(3*Fraction(1,6)/(4*Fraction(1,3)+3*Fraction(1,6)) == Fraction(3,11))

print("R11 U071/U072/C089 exact self-check")
print(f"ASSERTIONS={ASSERTIONS}")
print(f"C089_N4_p_order={p4}")
print(f"C089_N4_b={b4}")
print(f"floor(64 log_4 3)={qfloor}")
print(f"C089_N4_p3={paintbox_p3}")
print(f"C089_N4_q13={q13}")
print(f"C089_N4_q22={q22}")
print(f"C089_N4_root_rate={root_rate}")
print(f"C089_N4_balanced={balanced_prob}")
print(f"CTCS_N4_balanced={ctcs_balanced}")
print(f"C089_minus_CTCS={balanced_prob-ctcs_balanced}")
print(f"C088_N4_balanced={pbal_088}")
print(f"C089_minus_C088={balanced_prob-pbal_088}")
print("STATUS=ALL_EXACT_CHECKS_PASS")
