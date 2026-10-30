#!/usr/bin/env python3
"""Independent finite audit of B06-A028-LTF-TERMINAL-STOPPING-v1.

The certificate uses exact Fraction arithmetic for every Fourier coefficient,
coefficient factorization, squared-spectrum law, influence identity, and
physical-child spectrum.  Floating point is used only to evaluate the entropy
functional after the exact probability identities have been established.
"""

from fractions import Fraction
from itertools import product
from math import log2


def walsh(values):
    n = (len(values)).bit_length() - 1
    out = []
    for mask in range(1 << n):
        total = 0
        for x, val in enumerate(values):
            sign = -1 if ((mask & x).bit_count() & 1) else 1
            total += val * sign
        out.append(Fraction(total, 1 << n))
    return out


def entropy(coeffs):
    total = 0.0
    for a in coeffs:
        p = float(a * a)
        if p:
            total += p * log2(1.0 / p)
    return total


def influence(coeffs):
    return sum((a * a) * mask.bit_count() for mask, a in enumerate(coeffs))


def modulate(g, h):
    """F(x,z)=g(x_1 h(z),...,x_n h(z)); bits encode -1 when set."""
    n = (len(g)).bit_length() - 1
    m = (len(h)).bit_length() - 1
    vals = []
    all_x = (1 << n) - 1
    for x in range(1 << n):
        for z in range(1 << m):
            x2 = x if h[z] == 1 else (x ^ all_x)
            vals.append(g[x2])
    return vals


def restrict_z(F, n, m, z):
    return [F[(x << m) | z] for x in range(1 << n)]


def point_defect(m, defect=0):
    return [-1 if z == defect else 1 for z in range(1 << m)]


checks = 0
cases = 0

# Exhaust all Boolean g on up to three bits and all Boolean h on up to two bits.
for n in range(1, 4):
    for g_bits in product((-1, 1), repeat=1 << n):
        gh = walsh(g_bits)
        p_odd = sum(a * a for s, a in enumerate(gh) if s.bit_count() & 1)
        for m in range(1, 3):
            for h_bits in product((-1, 1), repeat=1 << m):
                hh = walsh(h_bits)
                F = modulate(g_bits, h_bits)
                Fh = walsh(F)
                # Exact coefficient factorization.  Our table layout places z
                # in the low m mask bits and x in the high n mask bits.
                for sx in range(1 << n):
                    for tz in range(1 << m):
                        got = Fh[(sx << m) | tz]
                        if sx.bit_count() & 1:
                            want = gh[sx] * hh[tz]
                        else:
                            want = gh[sx] if tz == 0 else Fraction(0)
                        assert got == want
                        checks += 1

                assert influence(Fh) == influence(gh) + p_odd * influence(hh)
                checks += 1
                assert abs(entropy(Fh) - (entropy(gh) + float(p_odd) * entropy(hh))) < 2e-12
                checks += 1

                # Every actual physical child after fixing the complete fresh
                # block has exactly the predecessor squared spectrum.
                g_sq = sorted(a * a for a in gh)
                for z in range(1 << m):
                    child = walsh(restrict_z(F, n, m, z))
                    assert sorted(a * a for a in child) == g_sq
                    checks += 1
                cases += 1

# Endpoint omitted in the source proof: q_1 is a signed dictator.
q1 = walsh(point_defect(1))
assert entropy(q1) == 0.0
assert influence(q1) == 1
checks += 2

# Every two-level physical leaf is an input-sign flip of the base.  This
# verifies the nested-variable issue: the newer common modulator also flips
# the older auxiliary variables.
for n in (1, 2):
    for g_bits in product((-1, 1), repeat=1 << n):
        for m1 in (1, 2):
            F1 = modulate(g_bits, point_defect(m1))
            for m2 in (1, 2):
                F2 = modulate(F1, point_defect(m2))
                # Directly restrict physical variables in order z2, then z1.
                # Index layout for F2 is ((x,z1),z2).
                for z2 in range(1 << m2):
                    for z1 in range(1 << m1):
                        leaf = []
                        for x in range(1 << n):
                            idx1 = (x << m1) | z1
                            leaf.append(F2[(idx1 << m2) | z2])
                        assert leaf == list(g_bits) or leaf == list(reversed(g_bits))
                        # Reversal is global input negation in this bit order.
                        checks += 1

print(f"PASS exact checks={checks} exhaustive one_step_cases={cases}")
print("PASS q_1 endpoint: H=0, I=1")
print("PASS two-level physical leaves, including flips of older auxiliary variables")
print("SCOPE finite algebraic audit only; all-dimensional claims are proved symbolically in the review")
