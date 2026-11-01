from fractions import Fraction
from decimal import Decimal, getcontext
from itertools import product

getcontext().prec = 180

# Frozen source endpoints entering this P13 run.
LOW = Fraction(99083249, 125000000)  # 0.792665992
P02_BEFORE = Fraction(8262759427622826251, 10**19)

# R17-C045 exact covering/cone data, reused but not re-proved here.
XN = YN = 513434
D = 1600000
A = Fraction(4*XN*YN, D*D)
LAM = Fraction(
    10114875937111444750637950885399422919832438289108176982868202874026753,
    29591135160849999997918500618240000000000000000000000000000000000000000
)

def neglog_bounds(x, n):
    # -log x = 2 * sum_{j>=0} u^(2j+1)/(2j+1), u=(1-x)/(1+x), for 0<x<1.
    u = (1-x)/(1+x)
    s = Fraction(0)
    p = u
    for j in range(n):
        s += p / (2*j+1)
        p *= u*u
    lo = 2*s
    # Positive-tail bound.
    hi = lo + 2*p / ((2*n+1)*(1-u*u))
    return lo, hi

def dec(q):
    return Decimal(q.numerator) / Decimal(q.denominator)

# Rigorous endpoint enclosure.
a_lo, a_hi = neglog_bounds(A, 500)
l_lo, l_hi = neglog_bounds(LAM, 700)
alpha_lo = a_lo / l_hi
alpha_hi = a_hi / l_lo
SCALE = 10**30
ceil_num = (alpha_hi.numerator*SCALE)//alpha_hi.denominator + 1
P13_AFTER = Fraction(ceil_num, SCALE)
assert alpha_lo <= alpha_hi < P13_AFTER < P02_BEFORE
assert P13_AFTER - LOW < P02_BEFORE - LOW

print("SOURCE_LOWER_EXACT", LOW)
print("P02_UPPER_BEFORE_EXACT", P02_BEFORE)
print("P13_UPPER_AFTER_EXACT", P13_AFTER)
print("CONTINUOUS_ALPHA_LO", dec(alpha_lo))
print("CONTINUOUS_ALPHA_HI", dec(alpha_hi))
print("WIDTH_BEFORE", dec(P02_BEFORE-LOW))
print("WIDTH_AFTER", dec(P13_AFTER-LOW))
print("STRICT_WIDTH_DECREASE", dec(P02_BEFORE-P13_AFTER))
print("EXACT_ENDPOINT_REFINEMENT_PASS")

def carries(x, g, v, left):
    cprev = left
    out = []
    for xi, gi in zip(x, g):
        c = 0 if gi else max(cprev, int(xi == v))
        out.append(c)
        cprev = c
    return tuple(out)

def delta_formula(x, g, v):
    # delta_i = product_{j<=i} (1-g_j) 1{x_j != v}
    p = 1
    out = []
    for xi, gi in zip(x, g):
        p *= (1-gi) * int(xi != v)
        out.append(p)
    return tuple(out)

# Exhaustively verify the exact dependence-preserving boundary recursion.
for k in range(1, 9):
    survival_pairs = 0
    total_xv = 0
    for x in product((0,1), repeat=k):
        for v in (0,1):
            total_xv += 1
            # Worst case over g is attained by g=0^k; count exact raw-letter survival.
            gz = (0,)*k
            d0 = carries(x, gz, v, 0)
            d1 = carries(x, gz, v, 1)
            if d1[-1] - d0[-1] == 1:
                survival_pairs += 1
        for g in product((0,1), repeat=k):
            for v in (0,1):
                c0 = carries(x,g,v,0)
                c1 = carries(x,g,v,1)
                delta = tuple(b-a for a,b in zip(c0,c1))
                assert delta == delta_formula(x,g,v)
                # Once killed, the boundary discrepancy never reappears.
                seen_zero = False
                for d in delta:
                    if seen_zero:
                        assert d == 0
                    if d == 0:
                        seen_zero = True
                # Gradient-output discrepancy is a single kill marker.
                prev = 1
                nonzero = 0
                for d in delta:
                    dg = d-prev
                    assert dg in (-1,0)
                    nonzero += (dg != 0)
                    prev = d
                assert nonzero <= 1
    # Exactly x=0^k,v=1 and x=1^k,v=0 survive.
    assert survival_pairs == 2
    prob = Fraction(survival_pairs, total_xv)
    assert prob == Fraction(1, 2**k)
    print("BOUNDARY_SURVIVAL_EXACT", k, prob)

print("CARRY_EXTINCTION_IDENTITY_EXHAUSTIVE_K_LE_8_PASS")

# Finite-horizon union-bound compiler. The theorem itself is proved in the report.
for T,K in [(1,8),(4,12),(8,16),(16,24)]:
    err = Fraction(T, 2**K)
    assert err <= 1
    print("FINITE_HORIZON_BOUND", "T", T, "K", K, "ERR", err, "DEC", dec(err))
print("FINITE_HORIZON_ERROR_ARITHMETIC_PASS")
print("ALL_EXACT_CHECKS_PASS")
