from fractions import Fraction as F
from itertools import permutations
from math import factorial

# HARD7-03 exact structural zero-gap edge triple-slack certificate.
# Self-check for the new edge-boundary stratum Y_0 > Y_2 > Y_1,
# disjoint from the previously corrected mixed-sign edge stratum.

U = (F(1), F(0), F(0))
V = (F(0), F(1), F(0))
W = (F(0), F(0), F(1))
ORDER = (
    U,
    tuple(U[i] + V[i] for i in range(3)),
    tuple(U[i] + V[i] + W[i] for i in range(3)),
)

def vadd(*vs):
    return tuple(sum(v[i] for v in vs) for i in range(3))

def vscale(c, v):
    return tuple(c*x for x in v)

def gap_cone_integral(g):
    # g are coefficients of the independent order-cone gaps
    # x_low=u, x_mid=u+v, x_high=u+v+w.
    rates = (F(3)-g[0], F(2)-g[1], F(1)-g[2])
    assert all(r > 0 for r in rates), (g, rates)
    return F(1)/(rates[0]*rates[1]*rates[2])

def high_minus_rank_gap_integral(g, rank):
    # Integral of (x_high-x_rank) exp(<g,gaps>) against the iid Exp(1)
    # density on one strict order cone.
    rates = (F(3)-g[0], F(2)-g[1], F(1)-g[2])
    assert all(r > 0 for r in rates), (g, rates)
    base = F(1)/(rates[0]*rates[1]*rates[2])
    if rank == 2:
        return F(0)
    return base*sum(F(1, rates[j]) for j in range(rank+1, 3))

def edge_boundary_transforms(theta):
    """
    Exact T_r for r=0,a,b:
       T_r = E[e^{theta Y2-r(Y0-Y2)} ; Y0>Y2>Y1],
    where
       s0=max(A_-1,A_0,A_1), s1=max(A_0,A_1), s2=A_1,
       Yj=sj+Exp(1),
    and s0>=s1>=s2 deterministically.

    Conditional on first-layer shifts, split the Y2 integral at s0.
    The resulting formulas contain only exponential monomials and
    at most one Delta=s0-s1 factor, then integrate over six order cones.
    """
    a = F(1)-theta
    b = F(2)-theta
    c = F(3)-theta
    T0 = Ta = Tb = F(0)

    for perm in permutations((-1, 0, 1)):  # low -> high A-label order
        rank = {lab: i for i, lab in enumerate(perm)}
        avec = {perm[r]: ORDER[r] for r in range(3)}

        s0 = ORDER[2]  # max(A_-1,A_0,A_1)
        s1 = avec[0] if rank[0] > rank[1] else avec[1]  # max(A_0,A_1)
        s2 = avec[1]  # A_1
        r1 = max(rank[0], rank[1])

        e_s2_minus_a_s1 = vadd(s2, vscale(-a, s1))
        e_s2_minus_a_s0 = vadd(s2, vscale(-a, s0))
        e_s2_plus_s1_minus_b_s0 = vadd(s2, s1, vscale(-b, s0))

        # r=0:
        # e^{s2}[(e^{-a s1}-e^{-a s0})/(ab)
        #         + e^{s1-b s0}/(bc)].
        T0 += (
            (gap_cone_integral(e_s2_minus_a_s1)
             - gap_cone_integral(e_s2_minus_a_s0))/(a*b)
            + gap_cone_integral(e_s2_plus_s1_minus_b_s0)/(b*c)
        )

        # r=a:
        # e^{s2}[ Delta e^{-a s0}/b
        #         - a e^{-a s0}/b^2
        #         + e^{s1-b s0}/c ].
        Delta_e0 = high_minus_rank_gap_integral(e_s2_minus_a_s0, r1)
        Ta += (
            Delta_e0/b
            - a*gap_cone_integral(e_s2_minus_a_s0)/(b*b)
            + gap_cone_integral(e_s2_plus_s1_minus_b_s0)/c
        )

        # r=b:
        # e^{s2}[ e^{-a s0}/b
        #   - e^{s1-b s0}(1+Delta+1/c)/c ].
        Delta_ec = high_minus_rank_gap_integral(
            e_s2_plus_s1_minus_b_s0, r1
        )
        Tb += (
            gap_cone_integral(e_s2_minus_a_s0)/b
            - (F(1)+F(1,c))*gap_cone_integral(
                e_s2_plus_s1_minus_b_s0
              )/c
            - Delta_ec/c
        )

    return T0, Ta, Tb

if __name__ == "__main__":
    theta = F(57343, 100000)
    a = F(1)-theta
    b = F(2)-theta
    c = F(3)-theta
    q = a
    kappa = theta/(b*c)

    # Carry-in exact four-step all-pair envelope from the preceding immutable run.
    U_prev = F(
        44218621253097337675520630615938362481617650843715385324269439414717371037400000000000000000000,
        54442695413156570473578553858609910677406260157304013873650482583987300880543061947950013587,
    )
    A_prev = F(36511391, 12500000)
    L_prev = F(3125000, 36511391)
    assert L_prev == F(1)/(F(4)*A_prev)

    T0, Ta, Tb = edge_boundary_transforms(theta)
    assert T0 > Ta > Tb > 0

    # Exact boundary bonus from
    # Phi_theta(u,0)-kappa
    # = theta/(ab)(1-e^{-au}) - kappa(1-e^{-bu}).
    C_edge0 = theta/(a*b)*(T0-Ta) - kappa*(T0-Tb)
    assert C_edge0 > 0

    # Two reflected edge strata. Triple slack H enters U4 as -H/(1-theta).
    delta_H = F(2)*C_edge0
    U_refined = U_prev - delta_H/q
    assert U_refined > 0
    assert U_refined < U_prev

    # New rational shape certificate, with an exact positive Taylor margin.
    A_new = F(584101, 200000)  # 2.920505
    assert A_new < A_prev
    x = F(4)*theta*A_new
    S32 = sum(x**k/F(factorial(k)) for k in range(33))
    margin = S32-U_refined
    assert margin > 0  # S32(x)<exp(x), so U_refined<exp(4 theta A_new).

    L_new = F(1)/(F(4)*A_new)
    assert L_new == F(50000, 584101)
    assert L_new > L_prev
    metric_gain = L_new-L_prev

    print("HARD7-03 exact structural zero-gap edge triple-slack certificate")
    print(f"theta = {theta}")
    print(f"T0 = {T0}")
    print(f"Ta = {Ta}")
    print(f"Tb = {Tb}")
    print(f"C_edge0 = {C_edge0}")
    print(f"delta_H_two_edges = {delta_H}")
    print(f"U_prev = {U_prev}")
    print(f"U_refined = {U_refined}")
    print(f"A_prev = {A_prev}")
    print(f"A_new = {A_new}")
    print(f"x = {x}")
    print(f"S32_minus_U_refined = {margin}")
    print(f"L_prev = {L_prev}")
    print(f"L_new = {L_new}")
    print(f"metric_gain = {metric_gain}")
    print(f"T0_float = {float(T0):.15f}")
    print(f"Ta_float = {float(Ta):.15f}")
    print(f"Tb_float = {float(Tb):.15f}")
    print(f"C_edge0_float = {float(C_edge0):.15f}")
    print(f"delta_U_float = {float(delta_H/q):.15f}")
    print(f"U_refined_float = {float(U_refined):.15f}")
    print(f"S32_minus_U_refined_float = {float(margin):.15e}")
    print(f"L_prev_float = {float(L_prev):.15f}")
    print(f"L_new_float = {float(L_new):.15f}")
    print(f"metric_gain_float = {float(metric_gain):.15e}")
    print("ALL_EXACT_CHECKS_PASS = True")
