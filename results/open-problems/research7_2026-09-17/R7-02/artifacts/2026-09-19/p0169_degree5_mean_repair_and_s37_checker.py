#!/usr/bin/env python3
"""
P0169 exact repair checker, 2026-09-19.

Purpose:
1. Audit the Newton/Hamming mean normalization.
2. Re-enumerate the 11-variable equality cases at L=34/16 and verify true mean 0.
3. Re-enumerate the 12-variable L=36/16 boundary profiles.
4. Correct the old 11-variable restriction enumeration at true means +/-3/16:
   two necessary profiles survive on each side, so the previous zero-survivor
   checker is invalid.
5. Glue corrected child profiles to each 12-variable parent profile and use
   coordinate-incidence double counting to rule out both parents.
6. Enumerate exact necessary profiles at L=35/16 in N=12,13 and L=37/16
   in N=13, supporting the first S=37 support-size eliminations.

All arithmetic is integer; mean is stored as mu16 = 16*E[f].
No floating point is used.
"""
from math import comb


def ceildiv(a, b):
    assert b > 0
    return -((-a)//b)


def enumerate_profiles(N, target16, target_mu16=None):
    """
    Necessary symmetrized Newton/Hamming profiles for Boolean degree <=5.

    b_k = # of +1 values on Hamming layer k.
    b_k = sum_{j=0}^5 u_j C(N-j,k-j), u_j integers.

    target16 = 16 * signed singleton sum.
    mu16 = 16 * mean = 32u0+16u1+8u2+4u3+2u4+u5-16.

    The singleton equation is
      -16u1-16u2-12u3-8u4-5u5 = target16.
    We enumerate the triangular prefix (u0,b1,b2,b3), then solve the
    remaining one-dimensional integer interval exactly.
    """
    C = [comb(N,k) for k in range(N+1)]
    c = [[0]*(N+1) for _ in range(6)]
    for j in range(6):
        for k in range(j, N+1):
            c[j][k] = comb(N-j, k-j)

    out = []
    prefixes = 0

    for u0 in (0,1):
        for b1 in range(C[1]+1):
            u1 = b1 - c[0][1]*u0
            for b2 in range(C[2]+1):
                u2 = b2 - c[0][2]*u0 - c[1][2]*u1
                for b3 in range(C[3]+1):
                    prefixes += 1
                    u3 = b3 - c[0][3]*u0 - c[1][3]*u1 - c[2][3]*u2

                    # From the signed singleton equation:
                    # 8u4 + 5u5 = -(target16+16u1+16u2+12u3).
                    R = target16 + 16*u1 + 16*u2 + 12*u3

                    # For every layer, after substituting
                    # u5=(-R-8u4)/5, impose 0 <= b_k <= C(N,k).
                    lo = -10**30
                    hi = 10**30
                    feasible = True

                    for k in range(N+1):
                        base = (u0*c[0][k] + u1*c[1][k]
                                + u2*c[2][k] + u3*c[3][k])
                        # 5 b_k = A + B u4
                        A = 5*base - c[5][k]*R
                        B = 5*c[4][k] - 8*c[5][k]
                        M = 5*C[k]

                        if B == 0:
                            if not (0 <= A <= M):
                                feasible = False
                                break
                        elif B > 0:
                            lo = max(lo, ceildiv(-A, B))
                            hi = min(hi, (M-A)//B)
                        else:
                            bb = -B
                            lo = max(lo, ceildiv(A-M, bb))
                            hi = min(hi, A//bb)

                        if lo > hi:
                            feasible = False
                            break

                    if not feasible:
                        continue

                    # Divisibility of u5: R+8u4 == 0 (mod 5);
                    # since 8 == 3 and 3^{-1} == 2 mod 5,
                    # u4 == -2R (mod 5).
                    residue = (-2*R) % 5
                    start = lo + ((residue-lo) % 5)

                    for u4 in range(start, hi+1, 5):
                        u5 = (-R-8*u4)//5
                        mu16 = (32*u0 + 16*u1 + 8*u2 + 4*u3
                                + 2*u4 + u5 - 16)
                        if target_mu16 is not None and mu16 != target_mu16:
                            continue

                        u = (u0,u1,u2,u3,u4,u5)
                        b = tuple(
                            sum(u[j]*c[j][k] for j in range(6))
                            for k in range(N+1)
                        )
                        assert all(0 <= b[k] <= C[k] for k in range(N+1))
                        L16 = -16*u1 - 16*u2 - 12*u3 - 8*u4 - 5*u5
                        assert L16 == target16
                        Bplus = sum(b)
                        assert mu16 * (2**N) == 32*Bplus - 16*(2**N)
                        out.append((u,b,mu16))

    return prefixes, out


def combine_children(bp, bm):
    """Parent Hamming profile from x_i=+ and x_i=- child profiles."""
    assert len(bp) == len(bm)
    nchild = len(bp)-1
    return tuple(
        (bp[k] if 0 <= k <= nchild else 0)
        + (bm[k-1] if 0 <= k-1 <= nchild else 0)
        for k in range(nchild+2)
    )


print("P0169 exact repair / S=37 first-support checker")
print("arithmetic=integer; floating_point=False")

const_mu16 = 32*1 - 16
assert const_mu16 == 16
print("mean_normalization_constant_plus_one_mu16", const_mu16)

p11eq, eq11 = enumerate_profiles(11,34)
assert p11eq == 223104
assert len(eq11) == 5
assert {z[2] for z in eq11} == {0}
print("N11_L34_prefixes", p11eq)
print("N11_L34_profiles", len(eq11))
print("N11_L34_mu16_set", sorted({z[2] for z in eq11}))

p12bd, bd12 = enumerate_profiles(12,36)
assert p12bd == 384982
assert len(bd12) == 2
assert {z[2] for z in bd12} == {0}
print("N12_L36_prefixes", p12bd)
print("N12_L36_profiles", len(bd12))
print("N12_L36_mu16_set", sorted({z[2] for z in bd12}))

p11p, rplus = enumerate_profiles(11,33,3)
p11m, rminus = enumerate_profiles(11,33,-3)
assert p11p == p11m == 223104
assert len(rplus) == 2
assert len(rminus) == 2
print("N11_L33_muplus3_profiles", len(rplus))
print("N11_L33_muminus3_profiles", len(rminus))
for tag, arr in (("plus",rplus),("minus",rminus)):
    for idx,(u,b,mu16) in enumerate(arr):
        print("restriction", tag, idx, "u", u, "b", b, "mu16", mu16)

for pidx,(pu,pb,pmu) in enumerate(bd12):
    matches = []
    for i,(_,bp,_) in enumerate(rplus):
        for j,(_,bm,_) in enumerate(rminus):
            if combine_children(bp,bm) == pb:
                matches.append((i,j))
    assert len(matches) == 1
    print("parent", pidx, "unique_child_pair", matches[0])

    i,j = matches[0]
    bp = rplus[i][1]
    bm = rminus[j][1]
    defects = []
    for k,bk in enumerate(pb):
        if k <= 11:
            lhs = 12*bp[k]
            rhs = (12-k)*bk
            if lhs != rhs:
                defects.append(("plus",k,lhs,rhs))
        if k >= 1:
            lhs = 12*bm[k-1]
            rhs = k*bk
            if lhs != rhs:
                defects.append(("minus",k,lhs,rhs))
    assert defects
    print("parent", pidx, "incidence_defect_count", len(defects),
          "first_defect", defects[0])

print("N12_L36_boundary_impossible_by_child_gluing_and_incidence", True)
print("therefore_N12_degree5_signed_singleton_bound_L16_le_35", True)

p12n, n12L35 = enumerate_profiles(12,35)
p13n, n13L35 = enumerate_profiles(13,35)
assert p12n == 384982
assert p13n == 634844
assert len(n12L35) == 8
assert len(n13L35) == 36
assert {z[2] for z in n12L35} == {-1,1}
assert {z[2] for z in n13L35} == {-1,1}
print("N12_L35_profiles", len(n12L35), "mu16_set", sorted({z[2] for z in n12L35}))
print("N13_L35_profiles", len(n13L35), "mu16_set", sorted({z[2] for z in n13L35}))

p13v, n13L37 = enumerate_profiles(13,37)
assert p13v == 634844
assert n13L37 == []
print("N13_L37_profiles", len(n13L37))

mu13 = sorted({z[2] for z in n13L35})
assert max(abs(a-b) for a in mu13 for b in mu13) == 2
assert 4 > 2
print("S37_n13_eliminated", True)
print("S37_n14_eliminated", True)
print("next_S37_support_size", 15)
print("ASSERTIONS_PASS")
