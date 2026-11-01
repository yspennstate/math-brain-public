#!/usr/bin/env python3
"""Targeted self-phase/coset-gradient checks for FEI interface C.

This is not an exhaustive Boolean sweep and does not prove FEI.  It checks:
  * exact RM(1,4) phase-increment second moments,
  * the exact index-two coset averaging identity numerically for finite resolvent kernels,
  * the derived J/N bound on an exact admissible sign-changing Boolean witness,
  * character and constant boundary cases.

Only Python's standard library is used.
"""
from fractions import Fraction
import math

def affine_masks(n):
    N = 1 << n
    out = set()
    for a in range(1 << n):
        for c in (0, 1):
            m = 0
            for x in range(N):
                bit = ((a & x).bit_count() & 1) ^ c
                m |= bit << x
            out.add(m)
    return sorted(out)

def phase(mask, N):
    return tuple(-1 if (mask >> x) & 1 else 1 for x in range(N))

def extend(M, b):
    return sorted(set(M) | {m ^ b for m in M})

def influences(mask, n):
    N = 1 << n
    f = phase(mask, N)
    ans = []
    for i in range(n):
        ans.append(Fraction(sum(f[x] != f[x ^ (1 << i)] for x in range(N)), N))
    return ans

def folded_J(mask, n):
    return sum(min(a, 1-a) for a in influences(mask, n))

def du_dv(mask, m, Q, N):
    f = phase(mask, N)
    s = tuple(-1 if (m >> x) & 1 else 1 for x in range(N))
    Q = set(Q)
    du = Fraction(sum((f[x]-1)*s[x] for x in range(N) if x not in Q), N)
    dv = Fraction(sum((f[x]-1)*s[x] for x in range(N) if x in Q), N)
    return du, dv

def F_T(x, T):
    return 0.0 if x == 0.0 else x * math.log1p(T/x)

def K(mask, m, Q, N, T):
    f = phase(mask, N)
    s = tuple(-1 if (m >> x) & 1 else 1 for x in range(N))
    Q = set(Q)
    u = sum(f[x]*s[x] for x in range(N) if x not in Q) / N
    v = sum(f[x]*s[x] for x in range(N) if x in Q) / N
    return F_T((u+v)**2, T) - F_T((u-v)**2, T)

def avgK(mask, M, Q, N, T):
    return sum(K(mask, m, Q, N, T) for m in M) / len(M)

def mask_of(points):
    return sum(1 << x for x in points)

n = 4
N = 1 << n
M = affine_masks(n)
assert len(M) == 2*N

Q = {0,3,4,7,9,10,12,15}
cases = {
    "sign_changing": mask_of({0,1,3,5,10,12,14,15}),
    "one_point": mask_of({0}),
    "character_x0": mask_of({x for x in range(N) if x & 1}),
    "constant_plus": 0,
}

for name, b in cases.items():
    Mp = extend(M, b)
    J = folded_J(b, n)
    moment = sum((du*du + dv*dv) for m in M for du,dv in [du_dv(b,m,Q,N)]) / len(M)
    target = Fraction(4 * b.bit_count(), N*N)
    assert moment == target
    if b in M:
        assert Mp == M
    print(f"CASE {name} J={J} |F|={b.bit_count()} delta2={moment}")
    for T in (1/8, 1/4, 1/2, 2):
        Af = avgK(b, M, Q, N, T)
        A0 = avgK(0, M, Q, N, T)
        Ap = avgK(b, Mp, Q, N, T)
        gamma = Af - Ap
        rhs_identity = 0.5*(Af-A0)
        assert abs(gamma-rhs_identity) < 2e-14
        if b in M:
            assert abs(gamma) < 2e-14
        # For the non-character witnesses used below, this is the direct
        # minimizing-gauge J/N bound. Characters are boundary-tested via gamma=0.
        if name in ("sign_changing", "one_point"):
            bound = 8*T*float(J)/N
            assert gamma*gamma <= bound + 1e-14
            print(f"  T={T:g} gamma={gamma:.17g} sq_bound={bound:.17g} ratio={gamma*gamma/bound:.12g}")
        else:
            print(f"  T={T:g} gamma={gamma:.17g} (boundary zero)")

print("PASS")
