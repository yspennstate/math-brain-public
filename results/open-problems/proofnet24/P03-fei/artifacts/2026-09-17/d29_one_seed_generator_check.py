#!/usr/bin/env python3
"""Exact modular checks for P03-I0098 d=29 one-seed reduction.

No floating point is used.  This verifies the finite-field/Zauner generator facts
used in the accompanying theorem.  It does not verify existence of a SIC or of
the conjectural Galois-equivariant overlap seed.
"""

p = 29
I = ((1, 0), (0, 1))
Z = ((0, 28), (1, 28))
G = ((1, 24), (5, 25))  # I + 5 Z mod 29


def mm(A, B):
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(2)) % p for j in range(2))
        for i in range(2)
    )


def mpow(A, n):
    R = I
    while n:
        if n & 1:
            R = mm(R, A)
        A = mm(A, A)
        n //= 2
    return R


def det(A):
    return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % p


def order_mat(A, limit=2000):
    R = I
    for n in range(1, limit + 1):
        R = mm(R, A)
        if R == I:
            return n
    raise AssertionError("order exceeds limit")


def order_mod(a):
    x = 1
    for n in range(1, p):
        x = x * a % p
        if x == 1:
            return n
    raise AssertionError("not in F_p^x")


def mv(A, v):
    return (
        (A[0][0] * v[0] + A[0][1] * v[1]) % p,
        (A[1][0] * v[0] + A[1][1] * v[1]) % p,
    )


def neg(A):
    return tuple(tuple((-x) % p for x in row) for row in A)


def symp(u, v):
    return (u[0] * v[1] - u[1] * v[0]) % p


# Full G orbit of e_1.
e1 = (1, 0)
cycle = []
v = e1
for _ in range(840):
    cycle.append(v)
    v = mv(G, v)
v_end = v

# First 280 points are representatives for the 280 Zauner 3-orbits because G^280=Z.
orbits = []
for k in range(280):
    vk = cycle[k]
    orbits.append({vk, mv(Z, vk), mv(mpow(Z, 2), vk)})
union = set().union(*orbits)
pairwise = all(orbits[i].isdisjoint(orbits[j]) for i in range(280) for j in range(i))

# A few vectors suffice for a direct implementation sanity check; the identity
# <Gu,Gv> = det(G)<u,v> is the standard 2x2 determinant identity.
samples_a = [(0, 1), (1, 0), (2, 3), (5, 7)]
samples_b = [(1, 1), (3, 4), (8, 9), (0, 2)]
symp_ok = all(
    symp(mv(G, a), mv(G, b)) == det(G) * symp(a, b) % p
    for a in samples_a
    for b in samples_b
)

checks = {
    "Z_order": order_mat(Z) == 3,
    "G_order": order_mat(G) == 840,
    "det_order": order_mod(det(G)) == 28,
    "commutes": mm(G, Z) == mm(Z, G),
    "G280_Z": mpow(G, 280) == Z,
    "G420_minusI": mpow(G, 420) == neg(I),
    "G140_minusZ2": mpow(G, 140) == neg(mpow(Z, 2)),
    "fullcycle": len(set(cycle)) == 840 and v_end == e1,
    "orbits": len(orbits) == 280 and len(union) == 840 and pairwise,
    "symp": symp_ok,
}

print("Z_order", order_mat(Z))
print("G", G, "det", det(G), "det_order", order_mod(det(G)), "G_order", order_mat(G))
print("G_commutes_Z", checks["commutes"])
print("G^280", mpow(G, 280))
print("G^420", mpow(G, 420))
print("G^140", mpow(G, 140))
print("-Z^2", neg(mpow(Z, 2)))
print("full_nonzero_cycle", len(set(cycle)), checks["fullcycle"])
print("zauner_orbits_count", len(orbits), "unique_union", len(union), "pairwise_disjoint", pairwise)
print("G140coset_minus", checks["G140_minusZ2"])
print("symplectic_multiplier_det", symp_ok)
print("ALL_EXACT_CHECKS_PASS", all(checks.values()))

assert all(checks.values())
