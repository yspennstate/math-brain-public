#!/usr/bin/env python3
"""Independent exact audit of B12's shared-coordinate covariance witness.

Dyadic quantities are represented by Fraction.  Spectral entropies are stored
as exact rational coefficients of ln(2) and ln(3); the only sign comparison is
reduced to an integer-power inequality.
"""
from fractions import Fraction as Q
from itertools import product


def dot(x, s):
    return sum(a*b for a, b in zip(x, s)) & 1


def fwht(values):
    n = (len(values)).bit_length() - 1
    cube = list(product((0, 1), repeat=n))
    return {
        s: Q(sum(values[j] * (-1 if dot(x, s) else 1)
                 for j, x in enumerate(cube)), 2**n)
        for s in cube
    }


def restrict(values, coord, bit):
    n = (len(values)).bit_length() - 1
    cube = list(product((0, 1), repeat=n))
    return [values[j] for j, x in enumerate(cube) if x[coord] == bit]


def energy(values):
    return sum(c*c for c in fwht(values).values())


def variance(values):
    m = sum(values, Q(0)) / Q(len(values))
    return sum((Q(v)*Q(v) for v in values), Q(0)) / Q(len(values)) - m*m


def influence(values):
    return sum(sum(s) * c*c for s, c in fwht(values).items())


def raw_entropy_log_coeffs(values):
    """Return (c2,c3) with E_raw = c2 ln2 + c3 ln3.

    This routine is intentionally strict: the audited witness has squared
    Walsh masses whose reduced numerators and denominators factor over 2,3.
    """
    c2 = Q(0)
    c3 = Q(0)
    for c in fwht(values).values():
        p = c*c
        if not p:
            continue
        num, den = p.numerator, p.denominator
        e2 = e3 = 0
        while num % 2 == 0:
            num //= 2; e2 += 1
        while num % 3 == 0:
            num //= 3; e3 += 1
        while den % 2 == 0:
            den //= 2; e2 -= 1
        while den % 3 == 0:
            den //= 3; e3 -= 1
        assert num == den == 1, (p, num, den)
        c2 += -p * e2
        c3 += -p * e3
    return c2, c3


def avg(x, y):
    return (x+y)/Q(2)


gp = [ 1,-1,-1, 1,-1,-1,-1, 1,-1,-1, 1,-1,-1,-1,-1, 1]
gm = [ 1,-1,-1,-1, 1,-1,-1, 1,-1,-1, 1,-1,-1,-1, 1,-1]
h  = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,-1, 1]

a = [Q(x+y, 2) for x, y in zip(gp, gm)]
b = [Q(x-y, 2) for x, y in zip(gp, gm)]
F = [x + z*y for x, y, z in zip(a, b, h)]
assert set(F) <= {-1, 1}

disagree = {i for i, (x, y) in enumerate(zip(gp, gm)) if x != y}
assert disagree == {3, 4, 14, 15}
assert {h[i] for i in disagree} == {-1, 1}

q = energy(b); Z = raw_entropy_log_coeffs(b)
V = variance(h); J = influence(h)
assert (q, Z, V, J) == (Q(1,4), (Q(5,4),Q(0)), Q(15,64), Q(1,2))

children = []
for bit in (0, 1):
    bb = restrict(b, 1, bit)
    hh = restrict(h, 1, bit)
    children.append((energy(bb), raw_entropy_log_coeffs(bb), variance(hh), influence(hh)))

assert children[0] == (Q(1,8), (Q(3,4),Q(0)), Q(0), Q(0))
assert children[1] == (Q(3,8), (Q(9,4),Q(-9,16)), Q(7,16), Q(3,4))

(q0,(z20,z30),V0,J0),(q1,(z21,z31),V1,J1) = children
drop_qJ = q*J - avg(q0*J0, q1*J1)
drop_VZ = (V*Z[0]-avg(V0*z20,V1*z21),
           V*Z[1]-avg(V0*z30,V1*z31))
assert drop_qJ == Q(-1,64)
assert drop_VZ == (Q(-102,512), Q(63,512))
assert 3**63 < 2**102

HF = raw_entropy_log_coeffs(F)
IF = influence(F)
assert HF == (Q(3), Q(0))
assert IF == Q(2)

# Check the simultaneous-update algebra independently on the witness.
dq = (q0-q1)/2
dJ = (J0-J1)/2
dv = (V0-V1)/2
dz2 = (z20-z21)/2
dz3 = (z30-z31)/2
inf_i = J-avg(J0,J1)
alpha2 = V-avg(V0,V1)
Dz = (Z[0]-avg(z20,z21), Z[1]-avg(z30,z31))
assert drop_qJ == q*inf_i - dq*dJ
assert drop_VZ[0] == alpha2*Z[0] + avg(V0,V1)*Dz[0] - dv*dz2
assert drop_VZ[1] == alpha2*Z[1] + avg(V0,V1)*Dz[1] - dv*dz3

# Exact all-k bent-spectator formulas.  H(s_k)=2k and I(s_k)=k.
for k in range(9):
    lifted_drop = (Q(-(102+24*k),512), Q(63,512))
    assert 3**63 < 2**(102+24*k)
    assert Q(2*k+3, k+2) < 2
    assert lifted_drop[0] == drop_VZ[0] - Q(24*k,512)

print("SHARED_COVARIANCE_CERTIFICATE_PASS")
print("root", q, Z, V, J)
print("children", children)
print("drop_qJ", drop_qJ)
print("drop_VZ_ln2_ln3", drop_VZ)
print("integer_sign", "3^63 < 2^102", 3**63 < 2**102)
print("output_H_bits_I", HF[0], IF)
print("lifted_k_checked", "0..8")
print("scope", "exact witness plus analytic nonnegative-two-term no-go")
