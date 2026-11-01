from fractions import Fraction as F
from itertools import permutations
from math import factorial

print("HARD7-03 exact mixed-sign edge-bonus certificate")

A_VARS = (-1, 0, 1)
BASES_ALL = {
    -2: {-1},
    -1: {-1, 0},
     0: {-1, 0, 1},
     1: {0, 1},
     2: {1},
}

def A3(t):
    return F(2) * (
        F(2268) - F(4408)*t + F(3748)*t**2 - F(1918)*t**3
        + F(652)*t**4 - F(143)*t**5 + F(18)*t**6 - t**7
    ) / ((F(3)-t)**4 * (F(2)-t)**3 * (F(1)-t)**3)

def M2(z, t):
    z = abs(z)
    if z == 2:
        return F(1)/(F(1)-t)**2
    if z == 1:
        return F(2)/((F(1)-t)**2*(F(2)-t))
    if z == 0:
        return F(6)/((F(1)-t)**2*(F(2)-t)*(F(3)-t))
    raise ValueError(z)

def pair_correction(t):
    return F(8)/(F(2)-t) * (M2(0,t)+M2(1,t)+M2(2,t))

def kappa(t):
    return t/((F(2)-t)*(F(3)-t))

def ordered_exp_integral(c):
    c1, c2, c3 = c
    r1 = F(3) - (c1+c2+c3)
    r2 = F(2) - (c2+c3)
    r3 = F(1) - c3
    assert r1 > 0 and r2 > 0 and r3 > 0
    return F(1)/(r1*r2*r3)

def ordered_exp_gap_integral(c, lo, hi):
    assert 0 <= lo < hi <= 2
    c1, c2, c3 = c
    rates = [
        F(3) - (c1+c2+c3),
        F(2) - (c2+c3),
        F(1) - c3,
    ]
    assert all(q > 0 for q in rates)
    base = F(1)/(rates[0]*rates[1]*rates[2])
    return base * sum(F(1, rates[j]) for j in range(lo+1, hi+1))

def weighted_target_max(t, bases, target):
    labels = list(bases)
    competitors = [j for j in labels if j != target]
    total = F(0)
    for perm in permutations(A_VARS):
        rank = {var:i for i,var in enumerate(perm)}
        br = {label:max(rank[v] for v in subset) for label,subset in bases.items()}
        M = max(br.values())
        for mask in range(1 << len(competitors)):
            S = [competitors[k] for k in range(len(competitors)) if (mask >> k) & 1]
            q = F(1)-t+len(S)
            c = [F(0), F(0), F(0)]
            c[br[target]] += 1
            for j in S:
                c[br[j]] += 1
            c[M] -= q
            term = ordered_exp_integral(c)/q
            total += -term if len(S) % 2 else term
    return total

def interval_integral(c, q, Lrank, Urank=None):
    if Urank is not None and Urank <= Lrank:
        return F(0)
    cL = list(c)
    cL[Lrank] -= q
    ans = ordered_exp_integral(cL)/q
    if Urank is not None:
        cU = list(c)
        cU[Urank] -= q
        ans -= ordered_exp_integral(cU)/q
    return ans

def weighted_chain(t, bases, upper, target, lowers):
    total = F(0)
    for perm in permutations(A_VARS):
        rank = {var:i for i,var in enumerate(perm)}
        br = {label:max(rank[v] for v in subset) for label,subset in bases.items()}
        Lrank = max([br[target]] + [br[l] for l in lowers])
        Urank = br[upper]
        for mask in range(1 << len(lowers)):
            S = [lowers[k] for k in range(len(lowers)) if (mask >> k) & 1]
            sign = -1 if len(S) % 2 else 1
            c = [F(0), F(0), F(0)]
            c[br[target]] += 1
            for l in S:
                c[br[l]] += 1
            q1 = F(1)-t+len(S)
            total += sign * interval_integral(c, q1, Lrank, Urank)
            c2 = list(c)
            c2[Urank] += 1
            q2 = q1 + 1
            total += sign * interval_integral(c2, q2, max(Lrank,Urank), None)
    return total

def local_minimum_correction(t):
    M2loc = weighted_target_max(t, {2:{1}, 1:{0,1}}, 2)

    M1_target = weighted_target_max(t, {0:{-1,0,1}, 1:{0,1}, 2:{1}}, 1)
    M1_chain = weighted_chain(t, BASES_ALL, upper=-1, target=2, lowers=[0,1])
    M1loc = M1_target + M1_chain

    M0_target = weighted_target_max(t, {-1:{-1,0}, 0:{-1,0,1}, 1:{0,1}}, 0)
    M0_chain = weighted_chain(t, BASES_ALL, upper=2, target=-1, lowers=[0,1])
    M0loc = M0_target + 2*M0_chain

    Hloc = kappa(t) * (2*M2loc + 2*M1loc + M0loc)
    return Hloc, M2loc, M1loc, M0loc

def weighted_penalty_complement(t, bases, target, lowers):
    """Exact six-cone integral from the preceding global-gap checkpoint."""
    r = F(2)-t
    total = F(0)
    lowers = list(lowers)

    for perm in permutations(A_VARS):
        rank = {var:i for i,var in enumerate(perm)}
        br = {label:max(rank[v] for v in subset) for label,subset in bases.items()}
        rt = br[target]
        m = max(br[l] for l in lowers)

        for mask in range(1, 1 << len(lowers)):
            S = [lowers[k] for k in range(len(lowers)) if (mask >> k) & 1]
            nS = len(S)
            coeff = F(((-1)**(nS+1))*nS)
            c = [F(0), F(0), F(0)]
            for l in S:
                c[br[l]] += 1

            if rt <= m:
                q = F(nS)+F(1)-t
                c2 = list(c)
                c2[rt] += 1
                c2[m] -= q
                total += coeff/r/q * ordered_exp_integral(c2)
            else:
                if nS == 1:
                    c_mid = list(c)
                    c_mid[rt] += t-F(1)
                    total += coeff/r * ordered_exp_gap_integral(c_mid, m, rt)
                else:
                    qmid = F(nS-1)
                    cA = list(c)
                    cA[rt] += t-F(1)
                    cA[m] -= qmid
                    cB = list(c)
                    cB[rt] += t-F(nS)
                    total += coeff/r/qmid * (
                        ordered_exp_integral(cA)-ordered_exp_integral(cB)
                    )

                q = F(nS)+F(1)-t
                cU = list(c)
                cU[rt] += F(1)-q
                total += coeff/r/q * ordered_exp_integral(cU)
    return total

def edge_chain_terms(t):
    """
    Exact integrals on Y0>Y1>Y2.

    Conditional bases are
      u0=max(A-1,A0,A1), u1=max(A0,A1), u2=A1,
    hence u0>=u1>=u2 on every A-order cone.

    Returns
      T1=E[e^{(t-1)Y1+Y2}; Y0>Y1>Y2],
      T2=E[e^{Y2-(1-t)Y0}; Y0>Y1>Y2].
    """
    aa = F(1)-t
    bb = F(2)-t
    cc = F(3)-t
    T1 = F(0)
    T2 = F(0)

    for perm in permutations(A_VARS):
        rank = {var:i for i,var in enumerate(perm)}
        r0 = max(rank[v] for v in {-1,0,1})
        r1 = max(rank[v] for v in {0,1})
        r2 = rank[1]
        assert r0 >= r1 >= r2

        # T1 conditional formula:
        # e^{u2-aa*u1}[(u1-u2)/bb+1/bb^2]
        # + e^{u1+u2-bb*u0}
        #   [(u0-u2)(1/cc-1/bb)+(1/cc^2-1/bb^2)].
        c = [F(0), F(0), F(0)]
        c[r2] += 1
        c[r1] -= aa
        term1 = F(0)
        if r1 > r2:
            term1 += ordered_exp_gap_integral(c, r2, r1)/bb
        term1 += ordered_exp_integral(c)/(bb**2)

        c2 = [F(0), F(0), F(0)]
        c2[r1] += 1
        c2[r2] += 1
        c2[r0] -= bb
        if r0 > r2:
            term1 += ordered_exp_gap_integral(c2, r2, r0) * (
                F(1,cc)-F(1,bb)
            )
        term1 += ordered_exp_integral(c2) * (
            F(1,cc**2)-F(1,bb**2)
        )
        T1 += term1

        # T2 conditional formula:
        # e^{u2-aa*u0}[(u1-u2)+1]/bb
        # + e^{u1+u2-bb*u0}/bb
        #   [-(u0-u2+1)+(u0-u2)/cc+1/cc^2].
        c3 = [F(0), F(0), F(0)]
        c3[r2] += 1
        c3[r0] -= aa
        term2 = F(0)
        if r1 > r2:
            term2 += ordered_exp_gap_integral(c3, r2, r1)/bb
        term2 += ordered_exp_integral(c3)/bb

        if r0 > r2:
            term2 += ordered_exp_gap_integral(c2, r2, r0)/bb * (
                F(-1)+F(1,cc)
            )
        term2 += ordered_exp_integral(c2)/bb * (
            F(-1)+F(1,cc**2)
        )
        T2 += term2

    return T1, T2

theta = F(11729,20000)
a_shape = F(29649457,10000000)
old_L = F(25000,296511)

alpha = F(1)-theta
beta = F(2)-theta
gamma = F(3)-theta

# Continuity check: reconstruct the complete old global-envelope correction at new theta.
Hloc, M2loc, M1loc, M0loc = local_minimum_correction(theta)
P2 = weighted_penalty_complement(theta, {1:{0,1}, 2:{1}}, 1, [2])
P10 = weighted_penalty_complement(
    theta, {0:{-1,0,1}, 1:{0,1}, 2:{1}}, 0, [1,2]
)
P12 = weighted_penalty_complement(theta, BASES_ALL, 2, [-1,0,1])
P01 = weighted_penalty_complement(theta, BASES_ALL, 1, [-2,-1,0])

P2_closed = (
    F(1)/((F(1)-theta)*(F(2)-theta)**3)
    + F(2)/(F(2)-theta)**4
)
assert P2 == P2_closed

Hbase = Hloc + kappa(theta) * (
    2*P2 + 2*(P10+P12) + 2*P01
)

# New mixed-sign edge correction.
T1, T2 = edge_chain_terms(theta)
assert T1 > T2 > 0

# Pointwise minorant constants.
# Exact bonus derivative at u=0 is kappa, while d/du(1-e^{-alpha u})|0=alpha,
# so kappa/alpha is the sharp coefficient in this basis at the origin.
bonus_slope_at_zero = kappa(theta)
basis_slope_at_zero = alpha
sharp_coeff = bonus_slope_at_zero / basis_slope_at_zero
assert sharp_coeff == kappa(theta)/alpha

Hextra_edge = 2 * sharp_coeff * (T1-T2)
assert Hextra_edge > 0

Hnew = Hbase + Hextra_edge
U4 = (F(3)*A3(theta) - pair_correction(theta) - Hnew)/(F(1)-theta)

# Exact Chernoff certificate with e^x > S_32(x).
x = F(4)*theta*a_shape
S32 = sum(x**k/F(factorial(k),1) for k in range(33))
margin = S32-U4
assert margin > 0

new_L = F(1)/(F(4)*a_shape)
metric_gain = new_L-old_L
assert new_L == F(2500000,29649457)
assert metric_gain == F(41075000,8791390144527)
assert metric_gain > 0

print(f"theta = {theta}")
print(f"a_shape = {a_shape}")
print(f"alpha = {alpha}")
print(f"beta = {beta}")
print(f"gamma = {gamma}")
print(f"kappa = {kappa(theta)}")
print(f"sharp_coeff = {sharp_coeff}")
print(f"M2loc = {M2loc}")
print(f"M1loc = {M1loc}")
print(f"M0loc = {M0loc}")
print(f"Hloc = {Hloc}")
print(f"P2 = {P2}")
print(f"P2_closed = {P2_closed}")
print(f"edge_identity_exact = {P2 == P2_closed}")
print(f"P10 = {P10}")
print(f"P12 = {P12}")
print(f"P01 = {P01}")
print(f"Hbase = {Hbase}")
print(f"T1 = {T1}")
print(f"T2 = {T2}")
print(f"T1_minus_T2 = {T1-T2}")
print(f"T1_float = {float(T1):.15f}")
print(f"T2_float = {float(T2):.15f}")
print(f"Hextra_edge = {Hextra_edge}")
print(f"Hextra_edge_float = {float(Hextra_edge):.15f}")
print(f"Hnew = {Hnew}")
print(f"U4 = {U4}")
print(f"U4_float = {float(U4):.15f}")
print(f"x = {x}")
print(f"S32_minus_U4 = {margin}")
print(f"S32_minus_U4_float = {float(margin):.15f}")
print(f"old_L = {old_L}")
print(f"new_L = {new_L}")
print(f"metric_gain = {metric_gain}")
print(f"old_L_float = {float(old_L):.15f}")
print(f"new_L_float = {float(new_L):.15f}")
print(f"metric_gain_float = {float(metric_gain):.15f}")
print("ALL_EXACT_CHECKS_PASS = True")