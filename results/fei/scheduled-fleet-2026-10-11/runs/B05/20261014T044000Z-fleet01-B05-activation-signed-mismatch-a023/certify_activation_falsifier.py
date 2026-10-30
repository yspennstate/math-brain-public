#!/usr/bin/env python3
"""Exact sign certificate for the fair-activation SMR(2,1/4) falsifier."""

from fractions import Fraction
from math import gcd, log2

QMASK = 56242


def lcm(a, b):
    return a // gcd(a, b) * b


def fwht(values):
    a = [Fraction(v) for v in values]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/len(a) for x in a]


def upper_caps(p):
    c = list(p)
    n = len(c).bit_length()-1
    for i in range(n):
        b = 1 << i
        for s in range(1 << n):
            if not s & b:
                c[s] += c[s | b]
    return c


def add_term(out, coeff, base):
    if coeff and base != 1:
        out[base] = out.get(base, Fraction(0)) + coeff
        if out[base] == 0:
            del out[base]


def add_scaled(out, src, scale=Fraction(1)):
    for base, coeff in src.items():
        add_term(out, scale*coeff, base)


def entropy_pair(out, a, b, scale=Fraction(1)):
    if a:
        add_term(out, scale*a, (a+b)/a)
    if b:
        add_term(out, scale*b, (a+b)/b)


def symbolic_stats(f):
    n = len(f).bit_length()-1
    wh = fwht(f)
    p = [x*x for x in wh]
    caps = upper_caps(p)
    u = {}
    for x, y in zip(p, caps):
        if x:
            add_term(u, x, y/x)
    bsum = {}
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if not s & bit:
                entropy_pair(bsum, p[s], p[s | bit])
    influence = sum(x*s.bit_count() for s, x in enumerate(p))
    return u, bsum, influence


def restrict(f, i, bit):
    n = len(f).bit_length()-1
    out = []
    for z in range(1 << (n-1)):
        lo = z & ((1 << i)-1)
        hi = z >> i
        out.append(f[lo | (bit << i) | (hi << (i+1))])
    return tuple(out)


def symbolic_residual(f):
    n = len(f).bit_length()-1
    u, bsum, influence = symbolic_stats(f)
    out = {}
    # G = n U(f) - 1/2 sum_{i,sigma} U(f_i^sigma).
    add_scaled(out, u, Fraction(n))
    for i in range(n):
        for bit in (0, 1):
            ur, _, _ = symbolic_stats(restrict(f, i, bit))
            add_scaled(out, ur, Fraction(-1, 2))
    add_scaled(out, bsum, Fraction(-1))
    add_scaled(out, u, Fraction(5, 4))
    # -2I = (-2I) log_2 2.
    add_term(out, -2*influence, Fraction(2))
    return out, influence


def value(expr):
    return sum(float(c)*log2(float(r)) for r, c in expr.items())


def exact_relation(expr):
    den = 1
    for c in expr.values():
        den = lcm(den, c.denominator)
    pos_num = pos_den = neg_num = neg_den = 1
    terms = 0
    for r, c in expr.items():
        e = c.numerator * (den // c.denominator)
        if not e:
            continue
        terms += 1
        if e > 0:
            pos_num *= pow(r.numerator, e)
            pos_den *= pow(r.denominator, e)
        else:
            e = -e
            neg_num *= pow(r.numerator, e)
            neg_den *= pow(r.denominator, e)
    left = pos_num * neg_den
    right = neg_num * pos_den
    return den, terms, (left > right) - (left < right), left.bit_length(), right.bit_length()


def numeric_full(f):
    n = len(f).bit_length()-1
    u, bsum, influence = symbolic_stats(f)
    U = value(u)
    B = value(bsum)
    G = n*U
    for i in range(n):
        for bit in (0, 1):
            ur, _, _ = symbolic_stats(restrict(f, i, bit))
            G -= value(ur)/2
    M = G-B
    return U, float(influence), B, G, M, M+1.25*U-2*float(influence)


q = tuple(1 if QMASK >> j & 1 else -1 for j in range(16))
F = tuple(1 if x & 1 else q[x >> 1] for x in range(32))
qexpr, qi = symbolic_residual(q)
fexpr, fi = symbolic_residual(F)
qcert = exact_relation(qexpr)
cert = exact_relation(fexpr)
qs = numeric_full(q)
fs = numeric_full(F)

print(f"q_mask={QMASK}")
print(f"q_truth={''.join('+' if x == 1 else '-' for x in q)}")
print(f"activation_truth={''.join('+' if x == 1 else '-' for x in F)}")
print(f"I_q={qi} residual_q={value(qexpr):.15f}")
print(f"I_activation={fi} residual_activation={value(fexpr):.15f}")
print(f"stats_q_U_I_B_G_M_L={qs}")
print(f"stats_activation_U_I_B_G_M_L={fs}")
print(f"exact_child_relation={qcert[2]}")
print(f"common_exponent_denominator={cert[0]}")
print(f"distinct_log_bases={cert[1]}")
print(f"left_bits={cert[3]} right_bits={cert[4]}")
print(f"exact_product_comparison_sign={cert[2]}")
assert qcert[2] == 0
assert cert[2] == 1
assert value(fexpr) > 0.09
print("PASS")
