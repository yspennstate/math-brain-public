from fractions import Fraction as F
from itertools import permutations, combinations
from math import factorial
from collections import Counter

# HARD7-03 exact central double-outrunner correction.
# This checker inherits only the previously certified pre-boundary rational U_prev,
# then reconstructs all three preceding structural-boundary corrections and the
# new strict (+,+) central local-minimum correction in exact Fraction arithmetic.

THETA = F(57343, 100000)
A_OLD = F(58398337, 20000000)
L_OLD = F(5000000, 58398337)
A_NEW = F(291978907, 100000000)

Uvec = (F(1), F(0), F(0))
Vvec = (F(0), F(1), F(0))
Wvec = (F(0), F(0), F(1))
ORDER = (
    Uvec,
    tuple(Uvec[i] + Vvec[i] for i in range(3)),
    tuple(Uvec[i] + Vvec[i] + Wvec[i] for i in range(3)),
)

def vadd(*vs):
    return tuple(sum(v[i] for v in vs) for i in range(3))

def vscale(c, v):
    return tuple(c*x for x in v)

def gap_cone_integral(g):
    rates = (F(3)-g[0], F(2)-g[1], F(1)-g[2])
    assert all(r > 0 for r in rates), (g, rates)
    return F(1)/(rates[0]*rates[1]*rates[2])

def max_shift(avec, rank, labels):
    lab = max(labels, key=lambda x: rank[x])
    return avec[lab]

def high_minus_rank_gap_integral(g, rank):
    rates = (F(3)-g[0], F(2)-g[1], F(1)-g[2])
    assert all(r > 0 for r in rates)
    base = F(1)/(rates[0]*rates[1]*rates[2])
    if rank == 2:
        return F(0)
    return base*sum(F(1, rates[j]) for j in range(rank+1, 3))

def edge_boundary_transforms(theta):
    a = F(1)-theta
    b = F(2)-theta
    c = F(3)-theta
    T0 = Ta = Tb = F(0)
    for perm in permutations((-1, 0, 1)):
        rank = {lab: i for i, lab in enumerate(perm)}
        avec = {perm[r]: ORDER[r] for r in range(3)}
        s0 = ORDER[2]
        s1 = avec[0] if rank[0] > rank[1] else avec[1]
        s2 = avec[1]
        r1 = max(rank[0], rank[1])

        e1 = vadd(s2, vscale(-a, s1))
        e0 = vadd(s2, vscale(-a, s0))
        ec = vadd(s2, s1, vscale(-b, s0))

        T0 += (
            (gap_cone_integral(e1)-gap_cone_integral(e0))/(a*b)
            + gap_cone_integral(ec)/(b*c)
        )
        Ta += (
            high_minus_rank_gap_integral(e0, r1)/b
            - a*gap_cone_integral(e0)/(b*b)
            + gap_cone_integral(ec)/c
        )
        Tb += (
            gap_cone_integral(e0)/b
            - (F(1)+F(1,c))*gap_cone_integral(ec)/c
            - high_minus_rank_gap_integral(ec, r1)/c
        )
    return T0, Ta, Tb

def near_boundary_T0(theta):
    b = F(2)-theta
    c = F(3)-theta
    d = F(4)-theta
    total = F(0)
    for perm in permutations((-1, 0, 1)):
        rank = {lab: i for i, lab in enumerate(perm)}
        avec = {perm[r]: ORDER[r] for r in range(3)}
        sU = max_shift(avec, rank, (-1, 0))
        s0 = ORDER[2]
        s1 = max_shift(avec, rank, (0, 1))
        s2 = avec[1]
        g1 = vadd(sU, s1, vscale(-b, s0))
        g2 = vadd(sU, s2, vscale(-b, s0))
        g3 = vadd(sU, s1, s2, vscale(-c, s0))
        total += (
            (gap_cone_integral(g1)+gap_cone_integral(g2))/(b*c)
            - F(2)*gap_cone_integral(g3)/(c*d)
        )
    return total

def center_boundary_T0(theta):
    total = F(0)
    zero = (F(0), F(0), F(0))
    for perm in permutations((-1, 0, 1)):
        rank = {lab: i for i, lab in enumerate(perm)}
        avec = {perm[r]: ORDER[r] for r in range(3)}
        sU = avec[-1]
        s0 = ORDER[2]
        s1 = max_shift(avec, rank, (0, 1))
        ell1 = max_shift(avec, rank, (-1, 0))
        ell2 = avec[1]
        dens = (
            (F(1), s0, 1),
            (F(1), s1, 1),
            (F(-2), vadd(s0, s1), 2),
        )
        lower = (
            (F(1), zero, 0),
            (F(-1), ell1, 1),
            (F(-1), ell2, 1),
            (F(1), vadd(ell1, ell2), 2),
        )
        val = F(0)
        for cd, sd, n in dens:
            for cl, sl, k in lower:
                lam = F(n+k+1)-theta
                g = vadd(sU, sd, sl, vscale(-lam, s0))
                val += cd*cl*gap_cone_integral(g)/lam
        assert val > 0
        total += val
    return total

def double_outrunner_T(theta):
    """
    T_both = E exp(A_-1 + A_1 -(2-theta) T),
    T=max(Y_-1,Y_0,Y_1).
    Conditional on A, expand the density of this three-way shifted-exponential
    maximum above s0=max(A_-1,A_0,A_1), then integrate over all six A-order cones.
    """
    b = F(2)-theta
    total = F(0)
    cone_values = []
    for perm in permutations((-1, 0, 1)):
        rank = {lab: i for i, lab in enumerate(perm)}
        avec = {perm[r]: ORDER[r] for r in range(3)}
        sm = max_shift(avec, rank, (-1, 0))
        s0 = ORDER[2]
        sp = max_shift(avec, rank, (0, 1))
        shifts = (sm, s0, sp)
        outer_sum = vadd(avec[-1], avec[1])
        val = F(0)
        for r in range(1, 4):
            for inds in combinations(range(3), r):
                coeff = F(((-1)**(r+1))*r, b+r)
                sexp = vadd(*(shifts[i] for i in inds))
                g = vadd(outer_sum, sexp, vscale(-(b+r), s0))
                val += coeff*gap_cone_integral(g)
        assert val > 0
        cone_values.append((perm, val))
        total += val
    return total, cone_values

# B19: exhaustive strict-order sign classifier for all 5! layer-two orderings.
YLABS = (-2, -1, 0, 1, 2)

def Srank(rank, e):
    return max(rank[z] for z in YLABS if abs(z-e) <= 1)

def sign(a, b):
    return "+" if a > b else ("0" if a == b else "-")

def pattern(rank, d):
    sm, s, sp = Srank(rank, d-1), Srank(rank, d), Srank(rank, d+1)
    return sign(sm, s), sign(sp, s)

counts = {d: Counter() for d in (0, 1, 2)}
for perm in permutations(YLABS):
    rank = {lab: i for i, lab in enumerate(perm)}  # low -> high
    for d in (0, 1, 2):
        counts[d][pattern(rank, d)] += 1

    # Right edge local-min positive/zero chamber.
    assert (pattern(rank, 2) == ("+", "0")) == (
        rank[0] > rank[2] > rank[1]
    )

    # Right near-edge local-min positive/zero chamber.
    M = max(rank[1], rank[2])
    assert (pattern(rank, 1) == ("+", "0")) == (
        rank[-1] > M > rank[0]
    )

    # Central positive/zero structural chamber.
    M0 = max(rank[0], rank[1])
    L0 = max(rank[-1], rank[2])
    assert (pattern(rank, 0) == ("+", "0")) == (
        rank[-2] > M0 > L0
    )

    # Reflected central zero/positive structural chamber.
    Mr = max(rank[-1], rank[0])
    Lr = max(rank[-2], rank[1])
    assert (pattern(rank, 0) == ("0", "+")) == (
        rank[2] > Mr > Lr
    )

    # The unique strict (+,+) local-minimum chamber.
    Tinner = max(rank[-1], rank[0], rank[1])
    assert (pattern(rank, 0) == ("+", "+")) == (
        rank[-2] > Tinner and rank[2] > Tinner
    )

assert counts[1][("+", "+")] == 0
assert counts[2][("+", "+")] == 0
assert counts[0][("+", "+")] == 12

theta = THETA
q = F(1)-theta
a = q
b = F(2)-theta
c = F(3)-theta
kappa = theta/(b*c)

# Certified carry-in before structural boundary corrections (immutable earlier run).
U_prev = F(
    44218621253097337675520630615938362481617650843715385324269439414717371037400000000000000000000,
    54442695413156570473578553858609910677406260157304013873650482583987300880543061947950013587,
)

# Reconstruct all previously certified structural boundary corrections.
T0e, Tae, Tbe = edge_boundary_transforms(theta)
C_edge = theta/(a*b)*(T0e-Tae) - kappa*(T0e-Tbe)
assert C_edge > 0
U_edge = U_prev - F(2)*C_edge/q

T0n = near_boundary_T0(theta)
T0c = center_boundary_T0(theta)
C_near = theta*T0n*(F(1, b*b)-F(1, c*c))
C_center = theta*T0c*(F(1, b*b)-F(1, c*c))
assert C_near > 0 and C_center > 0
U_carry = U_edge - F(2)*(C_near+C_center)/q

# New B5/B24 strict (+,+) central correction.
# If E~Exp(1), E[exp(-(t-E)_+)] = exp(-t)(1+t).
# Hence for two iid residuals the exact expected fresh-layer kernel is
# theta * int exp(-(2-theta)t)(1-e^-t)(1+t)^2 dt.
# Subtract kappa = theta(1/b-1/c).
D = F(2)*theta * (
    (F(1, b*b)-F(1, c*c))
    + (F(1, b*b*b)-F(1, c*c*c))
)
assert D > 0

T_both, both_cones = double_outrunner_T(theta)
C_both = D*T_both
assert C_both > 0

# It occurs only at d=0, so subtract one copy.
U_new = U_carry - C_both/q
assert U_new > 0 and U_new < U_carry

# Exact rational Chernoff certificate at the inherited theta.
assert A_NEW < A_OLD
x = F(4)*theta*A_NEW
S32 = sum(x**k/F(factorial(k)) for k in range(33))
margin = S32-U_new
assert margin > 0  # S32(x)<exp(x), so U_new<exp(4 theta A_NEW).

L_new = F(1)/(F(4)*A_NEW)
assert L_new == F(25000000, 291978907)
assert L_OLD == F(1)/(F(4)*A_OLD)
gain = L_new-L_OLD
assert gain > 0

print("HARD7-03 exact central double-outrunner local-minimum completion")
print(f"theta = {theta}")
print(f"sign_counts_d0 = {dict(sorted(counts[0].items()))}")
print(f"sign_counts_d1 = {dict(sorted(counts[1].items()))}")
print(f"sign_counts_d2 = {dict(sorted(counts[2].items()))}")
print(f"T_both = {T_both}")
print(f"D = {D}")
print(f"C_both = {C_both}")
print(f"U_carry = {U_carry}")
print(f"U_new = {U_new}")
print(f"A_old = {A_OLD}")
print(f"A_new = {A_NEW}")
print(f"x = {x}")
print(f"S32_minus_U_new = {margin}")
print(f"L_old = {L_OLD}")
print(f"L_new = {L_new}")
print(f"metric_gain = {gain}")
print(f"T_both_float = {float(T_both):.15f}")
print(f"D_float = {float(D):.15f}")
print(f"C_both_float = {float(C_both):.15f}")
print(f"delta_U_float = {float(C_both/q):.15f}")
print(f"U_carry_float = {float(U_carry):.15f}")
print(f"U_new_float = {float(U_new):.15f}")
print(f"S32_minus_U_new_float = {float(margin):.15e}")
print(f"L_old_float = {float(L_OLD):.15f}")
print(f"L_new_float = {float(L_new):.15f}")
print(f"metric_gain_float = {float(gain):.15e}")
print("ALL_EXACT_CHECKS_PASS = True")