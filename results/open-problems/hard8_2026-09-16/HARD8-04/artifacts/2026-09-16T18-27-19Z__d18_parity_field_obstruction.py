#!/usr/bin/env python3
"""
Exact self-check for HARD8-04's d=18 signed-equivariant T(523) obstruction.

Scope:
- exact arithmetic only;
- validates the finite arithmetic and GF(2) support-orbit linear algebra used
  in the written proof;
- does NOT claim nonexistence of arbitrary T(523) or H(2092).

The preceding pinned signed-equivariance sieve established that, among d=18
signed-permutation equivariance classes surviving its necessary row/orbit-sum
gates, the unique class up to conjugacy has canonical support action
  e0 -> e0, e1 -> e3, e2 -> e2, e3 -> e1
and normalized row vector (19,9,0,9).
"""

P = 523
N = P - 1

# ---------- arithmetic / primitive-root checks ----------

prime_factors_N = (2, 3, 29)
assert N == 2 * 3 * 3 * 29
assert pow(2, N, P) == 1
# To prove ord_P(2)=522, check 2^(522/q) != 1 for every prime q|522.
order_witnesses = {q: pow(2, N // q, P) for q in prime_factors_N}
assert all(v != 1 for v in order_witnesses.values())
assert order_witnesses == {2: 522, 3: 462, 29: 121}

# h generates the unique subgroup of order 18 in F_523^*.
h = pow(2, N // 18, P)
assert h == 429
assert pow(h, 18, P) == 1
assert pow(h, 9, P) != 1
assert pow(h, 6, P) != 1

# The involution z -> z^{-1} is Frobenius^(261), since 2^261 == -1 mod 523.
assert pow(2, 261, P) == P - 1
assert 261 % 29 == 0
assert 261 % 58 == 29

# ---------- support-bit action / parity truth table ----------

# Support labels:
# e0=(0,0), e1=(0,1), e2=(1,0), e3=(1,1)
bits = {
    0: (0, 0),
    1: (0, 1),
    2: (1, 0),
    3: (1, 1),
}
# Canonical d=18 surviving signed action has support permutation
# 0->0, 1->3, 2->2, 3->1.
support_R = {0: 0, 1: 3, 2: 2, 3: 1}
for i in range(4):
    u, v = bits[i]
    up, vp = bits[support_R[i]]
    assert vp == v
    assert up == (u ^ v)

# Equality indicator over F2:
# 1_{(u,v)=(u',v')} = (1+u+u')(1+v+v').
for i in range(4):
    for j in range(4):
        u, v = bits[i]
        up, vp = bits[j]
        rhs = (1 ^ u ^ up) & (1 ^ v ^ vp)
        lhs = int(i == j)
        assert lhs == rhs

# ---------- h-orbits and GF(2)[z]/Phi_523 exact linear algebra ----------

# 29 nonzero h-orbits, each of size 18.
seen = set()
orbits = []
for x in range(1, P):
    if x in seen:
        continue
    orb = []
    y = x
    while y not in orb:
        orb.append(y)
        seen.add(y)
        y = (h * y) % P
    assert y == x
    assert len(orb) == 18
    orbits.append(tuple(orb))
assert len(orbits) == 29
assert len(seen) == 522
assert set().union(*(set(o) for o in orbits)) == set(range(1, P))

# Since ord_523(2)=522, Phi_523(z)=1+z+...+z^522 is irreducible over F2.
# Work in its quotient. For polynomials of degree <=522,
# z^522 = 1+z+...+z^521.
LOW_522 = (1 << 522) - 1

def reduce_phi_deg_le_522(poly_bits: int) -> int:
    assert poly_bits.bit_length() <= 523
    if (poly_bits >> 522) & 1:
        poly_bits ^= 1 << 522
        poly_bits ^= LOW_522
    assert poly_bits.bit_length() <= 522
    return poly_bits

# Each h-invariant v with v(0)=0 is a binary choice on 29 h-orbits.
# Map each orbit indicator into the quotient field representation.
columns = []
for orb in orbits:
    poly = 0
    for e in orb:
        poly ^= 1 << e
    columns.append(reduce_phi_deg_le_522(poly))

def gf2_rank(vectors):
    basis = {}
    for v in vectors:
        x = v
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                break
    return len(basis), basis

rank, _ = gf2_rank(columns)
assert rank == 29

# The XOR of all orbit indicators is z+...+z^522,
# which equals 1 modulo Phi_523.
all_nonzero_poly = 0
for col in columns:
    all_nonzero_poly ^= col
assert all_nonzero_poly == 1

# Therefore the linear equation V(zeta)=1 among h-invariant v with v(0)=0
# has the UNIQUE orbit-choice solution "all 29 orbits selected".
assert rank == len(columns)

# ---------- final row-sum contradiction ----------

# From the preceding exact signed-equivariance sieve:
q0_component = 0
q0_sign = 1
required_row_vector = (19, 9, 0, 9)
assert sum(r*r for r in required_row_vector) == 523
assert q0_component == 0 and q0_sign == 1

# The field/parity argument forces v(x)=1 for every x != 0.
# Since v=1 exactly on support components e1/e3, component e0 occurs only at x=0.
# Its row sum must therefore be +1, contradicting the required +19.
forced_component0_row_sum = q0_sign
assert forced_component0_row_sum == 1
assert required_row_vector[0] == 19
assert forced_component0_row_sum != required_row_vector[0]

print("P", P)
print("ORD_523_2_WITNESSES", order_witnesses)
print("H_ORDER18_GENERATOR", h)
print("STAR_FROBENIUS_EXPONENT", 261)
print("STAR_ON_F29_REMAINDER", 261 % 29)
print("STAR_ON_F58_REMAINDER", 261 % 58)
print("NONZERO_H_ORBITS", len(orbits))
print("H_ORBIT_SIZES", sorted(set(map(len, orbits))))
print("GF2_ORBIT_INDICATOR_RANK", rank)
print("GF2_ALL_NONZERO_ORBITS_EVALUATE_TO_ONE", int(all_nonzero_poly == 1))
print("UNIQUE_H_INVARIANT_V_WITH_V0_ZERO_AND_VZETA_ONE", "all_nonzero_positions")
print("REQUIRED_ROW_VECTOR", required_row_vector)
print("FORCED_COMPONENT0_ROW_SUM", forced_component0_row_sum)
print("CONTRADICTION", f"{forced_component0_row_sum}!={required_row_vector[0]}")
print("SCOPE", "rules out the d=18 canonical signed-equivariant T(523) family; combine with pinned conjugacy sieve for the full d=18 signed-equivariant tier")
print("ALL_EXACT_D18_PARITY_FIELD_CHECKS_PASSED")
