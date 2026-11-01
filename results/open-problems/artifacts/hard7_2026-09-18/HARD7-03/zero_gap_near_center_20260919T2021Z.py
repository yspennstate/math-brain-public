from fractions import Fraction as F
from itertools import permutations
from math import factorial

# HARD7-03 exact near-edge structural zero-gap triple-slack certificate.
# New event at d=1:
#   U=Y_{-1} > M=max(Y_1,Y_2) > Y_0,
# which forces S_0=U>S_1=S_2=M and hence (u,v)=(U-M,0).
# The reflected d=-1 event is added separately.

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
    # On one strict order cone:
    # x_low=z1, x_mid=z1+z2, x_high=z1+z2+z3,
    # iid Exp(1) density is exp(-3 z1-2 z2-z3).
    rates = (F(3)-g[0], F(2)-g[1], F(1)-g[2])
    assert all(r > 0 for r in rates), (g, rates)
    return F(1)/(rates[0]*rates[1]*rates[2])

def max_shift(avec, rank, labels):
    lab = max(labels, key=lambda x: rank[x])
    return avec[lab]

def near_boundary_T0(theta):
    """
    T0 = E[e^{theta M}; U>M>Y0],
    U=Y_{-1}, M=max(Y1,Y2).

    Given A, let
      sU=max(A_-1,A0), s0=max(A_-1,A0,A1),
      s1=max(A0,A1), s2=A1.
    Then s0 dominates all four shifts. On U>M>Y0 we have m=M>s0,
    so all shifted exponentials are in their pure tail region.

    For m>=s0:
      f_M(m)=e^{s1-m}+e^{s2-m}-2e^{s1+s2-2m},
      P(Y0<m)=1-e^{s0-m},
      P(U>m)=e^{sU-m}.
    Direct integration yields
      T0|A =
       [e^{sU+s1-b s0}+e^{sU+s2-b s0}]/(b c)
       - 2 e^{sU+s1+s2-c s0}/(c d),
    b=2-theta, c=3-theta, d=4-theta.
    """
    b = F(2)-theta
    c = F(3)-theta
    d = F(4)-theta
    total = F(0)
    cone_values = []

    for perm in permutations((-1, 0, 1)):  # low -> high A-label order
        rank = {lab: i for i, lab in enumerate(perm)}
        avec = {perm[r]: ORDER[r] for r in range(3)}

        sU = max_shift(avec, rank, (-1, 0))
        s0 = ORDER[2]
        s1 = max_shift(avec, rank, (0, 1))
        s2 = avec[1]

        g1 = vadd(sU, s1, vscale(-b, s0))
        g2 = vadd(sU, s2, vscale(-b, s0))
        g3 = vadd(sU, s1, s2, vscale(-c, s0))

        val = (
            (gap_cone_integral(g1) + gap_cone_integral(g2))/(b*c)
            - F(2)*gap_cone_integral(g3)/(c*d)
        )
        assert val > 0
        cone_values.append((perm, val))
        total += val

    return total, cone_values

def center_boundary_T0(theta):
    """
    One orientation of the center zero-gap event:
       U=Y_{-2} > M=max(Y0,Y1) > L=max(Y_{-1},Y2).
    Then S_{-1}=U>S0=S1=M.

    Given A, M>=s0=max(A_-1,A0,A1), which dominates all other
    deterministic shifts. Expand the density of M against the CDF of L.
    """
    total = F(0)
    cone_values = []

    for perm in permutations((-1, 0, 1)):  # low -> high
        rank = {lab: i for i, lab in enumerate(perm)}
        avec = {perm[r]: ORDER[r] for r in range(3)}

        sU = avec[-1]                       # shift of Y_{-2}
        s0 = ORDER[2]                       # shift of Y0
        s1 = max_shift(avec, rank, (0, 1)) # shift of Y1
        ell1 = max_shift(avec, rank, (-1, 0)) # shift of Y_{-1}
        ell2 = avec[1]                      # shift of Y2

        # f_M terms: coefficient, shift monomial, exponential decay n.
        dens = (
            (F(1), s0, 1),
            (F(1), s1, 1),
            (F(-2), vadd(s0, s1), 2),
        )
        # P(L<m)=(1-e^{ell1-m})(1-e^{ell2-m}).
        zero = (F(0), F(0), F(0))
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
        cone_values.append((perm, val))
        total += val

    return total, cone_values

def high_minus_rank_gap_integral(g, rank):
    # Needed only to reconstruct the preceding immutable edge correction exactly.
    rates = (F(3)-g[0], F(2)-g[1], F(1)-g[2])
    assert all(r > 0 for r in rates), (g, rates)
    base = F(1)/(rates[0]*rates[1]*rates[2])
    if rank == 2:
        return F(0)
    return base*sum(F(1, rates[j]) for j in range(rank+1, 3))

def edge_boundary_transforms(theta):
    # Exact carry-in from the preceding immutable run.
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

if __name__ == "__main__":
    theta = F(57343, 100000)
    a = F(1)-theta
    b = F(2)-theta
    c = F(3)-theta
    q = a
    kappa = theta/(b*c)

    # Pre-edge-boundary exact four-step all-pair envelope.
    U_prev = F(
        44218621253097337675520630615938362481617650843715385324269439414717371037400000000000000000000,
        54442695413156570473578553858609910677406260157304013873650482583987300880543061947950013587,
    )

    # Reconstruct preceding edge-boundary correction exactly.
    T0e, Tae, Tbe = edge_boundary_transforms(theta)
    C_edge0 = theta/(a*b)*(T0e-Tae) - kappa*(T0e-Tbe)
    assert C_edge0 > 0
    U_carry = U_prev - F(2)*C_edge0/q

    # New near-edge boundary branch.
    T0n, near_cones = near_boundary_T0(theta)
    assert T0n > 0

    # B11 identity: T_r=T0/(1+r) on every pure-tail zero-gap event.
    Tan = T0n/b          # 1+a=b
    Tbn = T0n/c          # 1+b=c
    C_near_direct = theta/(a*b)*(T0n-Tan) - kappa*(T0n-Tbn)
    C_near = theta*T0n*(F(1, b*b)-F(1, c*c))
    assert C_near_direct == C_near
    assert C_near > 0

    # New center boundary branch, one orientation; reflection is disjoint.
    T0c, center_cones = center_boundary_T0(theta)
    assert T0c > 0
    Tac = T0c/b
    Tbc = T0c/c
    C_center_direct = theta/(a*b)*(T0c-Tac) - kappa*(T0c-Tbc)
    C_center = theta*T0c*(F(1, b*b)-F(1, c*c))
    assert C_center_direct == C_center
    assert C_center > 0

    # Two reflected near-edge endpoints and two disjoint center orientations.
    delta_H_near = F(2)*C_near
    delta_H_center = F(2)*C_center
    delta_H = delta_H_near + delta_H_center
    U_refined = U_carry - delta_H/q
    assert U_refined > 0
    assert U_refined < U_carry

    # Carry-in metric from 19:21Z.
    A_carry = F(584101, 200000)
    L_carry = F(50000, 584101)
    assert L_carry == F(1)/(F(4)*A_carry)

    # New rational shape certificate at the same theta.
    A_new = F(58398337, 20000000)  # 2.91991685
    assert A_new < A_carry
    x = F(4)*theta*A_new
    S32 = sum(x**k/F(factorial(k)) for k in range(33))
    margin = S32-U_refined
    assert margin > 0  # S32(x)<exp(x), hence U_refined<exp(4 theta A_new).

    L_new = F(1)/(F(4)*A_new)
    assert L_new == F(5000000, 58398337)
    assert L_new > L_carry
    metric_gain = L_new-L_carry

    print("HARD7-03 exact near-edge + center structural zero-gap triple-slack certificate")
    print(f"theta = {theta}")
    for perm, val in near_cones:
        print(f"T0_near_cone_{perm} = {val}")
    for perm, val in center_cones:
        print(f"T0_center_cone_{perm} = {val}")
    print(f"T0_near = {T0n}")
    print(f"Ta_near = {Tan}")
    print(f"Tb_near = {Tbn}")
    print(f"C_near0 = {C_near}")
    print(f"T0_center = {T0c}")
    print(f"Ta_center = {Tac}")
    print(f"Tb_center = {Tbc}")
    print(f"C_center0 = {C_center}")
    print(f"delta_H_two_near_edges = {delta_H_near}")
    print(f"delta_H_two_center_orientations = {delta_H_center}")
    print(f"delta_H_total = {delta_H}")
    print(f"U_carry = {U_carry}")
    print(f"U_refined = {U_refined}")
    print(f"A_carry = {A_carry}")
    print(f"A_new = {A_new}")
    print(f"x = {x}")
    print(f"S32_minus_U_refined = {margin}")
    print(f"L_carry = {L_carry}")
    print(f"L_new = {L_new}")
    print(f"metric_gain = {metric_gain}")
    print(f"T0_near_float = {float(T0n):.15f}")
    print(f"C_near0_float = {float(C_near):.15f}")
    print(f"T0_center_float = {float(T0c):.15f}")
    print(f"C_center0_float = {float(C_center):.15f}")
    print(f"delta_U_float = {float(delta_H/q):.15f}")
    print(f"U_carry_float = {float(U_carry):.15f}")
    print(f"U_refined_float = {float(U_refined):.15f}")
    print(f"S32_minus_U_refined_float = {float(margin):.15e}")
    print(f"L_carry_float = {float(L_carry):.15f}")
    print(f"L_new_float = {float(L_new):.15f}")
    print(f"metric_gain_float = {float(metric_gain):.15e}")
    print("ALL_EXACT_CHECKS_PASS = True")
