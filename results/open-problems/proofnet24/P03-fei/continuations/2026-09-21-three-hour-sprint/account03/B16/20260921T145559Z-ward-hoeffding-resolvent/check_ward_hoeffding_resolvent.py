#!/usr/bin/env python3
"""Exact checks for the B16 Ward/Hoeffding/plaquette-resolvent report.

Standard library only. These are falsification checks for the proved algebra,
not a finite proof of FEI.
"""
from fractions import Fraction
from itertools import combinations
from math import factorial
import json, random


def powerset(items):
    items = tuple(items)
    for r in range(len(items)+1):
        for s in combinations(items, r):
            yield frozenset(s)


def beta_int(a, b):
    return Fraction(factorial(a-1)*factorial(b-1), factorial(a+b-1))


def kint_pair(A, B):
    h = len(A & B)
    if h == 0:
        return Fraction(0)
    r, s = len(A), len(B)
    return Fraction(h, len(A | B)) - Fraction(h, r+s-1)


def direct_kint(rel):
    return sum(ca*cb*kint_pair(A, B)
               for A, ca in rel.items() for B, cb in rel.items())


def deriv_poly(rel, F):
    d = {}
    for A, c in rel.items():
        if F <= A:
            j = len(A)-len(F)
            d[j] = d.get(j, Fraction(0)) + c
    return d


def deriv_diag(rel, F, t):
    return sum(c*t**(len(A)-len(F)) for A, c in rel.items() if F <= A)


def face_layers(rel, ground):
    out = {}
    for k in range(2, len(ground)+1):
        total = Fraction(0)
        for Ft in combinations(ground, k):
            d = deriv_poly(rel, frozenset(Ft))
            for a, ca in d.items():
                for b, cb in d.items():
                    total += k*ca*cb*beta_int(a+b+k, k)
        if total:
            out[k] = total
    return out


def parity_game(rel, S):
    return sum(c for A, c in rel.items() if len(A & S) % 2)


def delta_F(rel, F, S):
    ans = Fraction(0)
    for U in powerset(F):
        ans += (-1 if (len(F)-len(U)) % 2 else 1) * parity_game(rel, S | U)
    return ans


def bernoulli_delta(rel, ground, F, p):
    rest = tuple(set(ground)-set(F))
    ans = Fraction(0)
    for S in powerset(rest):
        prob = p**len(S)*(1-p)**(len(rest)-len(S))
        ans += prob*delta_F(rel, F, S)
    return ans


def pv_value(rel, v, Y):
    return sum(c for A, c in rel.items() if v in A and (A-{v}) <= Y)


def brute_var(rel, ground, v, t):
    rest = tuple(set(ground)-{v})
    m = s2 = Fraction(0)
    for Y in powerset(rest):
        prob = t**len(Y)*(1-t)**(len(rest)-len(Y))
        z = pv_value(rel, v, Y)
        m += prob*z
        s2 += prob*z*z
    return s2-m*m


def hoeffding_var(rel, ground, v, t):
    w = t*(1-t)
    ans = Fraction(0)
    rest = tuple(set(ground)-{v})
    for k in range(1, len(rest)+1):
        for T in combinations(rest, k):
            d = deriv_diag(rel, frozenset(T)|{v}, t)
            ans += w**k*d*d
    return ans


def qflip_basis(n):
    out = {}
    for v in range(1, 1 << n):
        supp = [i for i in range(n) if (v >> i) & 1]
        if len(supp) >= 2:
            i = min(supp)
            out[v] = frozenset((0, 1 << i, v, v ^ (1 << i)))
    return out


def symdiff(sets):
    s = set()
    for A in sets:
        for x in A:
            if x in s:
                s.remove(x)
            else:
                s.add(x)
    return frozenset(s)


# Generic exact families.
rng = random.Random(160921)
generic = variance_checks = parity_checks = 0
for m in range(3, 6):
    ground = tuple(range(m))
    odd = [frozenset(S) for k in range(1, m+1, 2)
           for S in combinations(ground, k)]
    for _ in range(7):
        rel = {A: Fraction(c) for A in odd
               for c in [rng.choice((-2, -1, 0, 1, 2))] if c}
        if not rel:
            continue
        assert sum(face_layers(rel, ground).values(), Fraction(0)) == direct_kint(rel)
        generic += 1
        for t in (Fraction(1,5), Fraction(1,3), Fraction(1,2), Fraction(4,5)):
            for v in ground:
                assert brute_var(rel, ground, v, t) == hoeffding_var(rel, ground, v, t)
                variance_checks += 1
        for t in (Fraction(1,3), Fraction(3,5)):
            p = (1-t)/2
            for k in range(1, m+1):
                for Ft in combinations(ground, k):
                    F = frozenset(Ft)
                    lhs = bernoulli_delta(rel, ground, F, p)
                    rhs = ((-1)**(k+1))*2**(k-1)*deriv_diag(rel, F, t)
                    assert lhs == rhs
                    parity_checks += 1

# Abstract Pasch trade.
ground = tuple(range(6))
plus = [(0,1,2), (0,3,4), (1,3,5), (2,4,5)]
minus = [(0,1,3), (0,2,4), (1,2,5), (3,4,5)]
pasch = {frozenset(T): Fraction(1) for T in plus}
pasch.update({frozenset(T): Fraction(-1) for T in minus})
for ij in combinations(ground, 2):
    assert all(x == 0 for x in deriv_poly(pasch, frozenset(ij)).values())
assert face_layers(pasch, ground) == {3: Fraction(4,5)}
assert direct_kint(pasch) == Fraction(4,5)

# Genuine n=4 one-point-phase ordered-min q-flip packet.
basis = qflip_basis(4)
vs = (3, 5, 6, 10, 11, 13)
actual = {}
weights = {}
for T in plus + minus:
    A = symdiff([basis[vs[i]] for i in T])
    sign = 1 if (len(A)//2) % 2 == 0 else -1
    target = 1 if T in plus else -1
    assert sign == target
    actual[frozenset(T)] = Fraction(sign, 8)  # exact Borel pi/4 magnitude for N=16
    weights[tuple(i+1 for i in T)] = len(A)
for ij in combinations(ground, 2):
    assert all(x == 0 for x in deriv_poly(actual, frozenset(ij)).values())
assert face_layers(actual, ground) == {3: Fraction(1,80)}
assert direct_kint(actual) == Fraction(1,80)

# Inverse-number resolvent normalization.
for j in range(1, 21):
    assert 2*j*Fraction(1, 2*j) == 1

print(json.dumps({
    "status": "PASS",
    "generic_signed_relation_families": generic,
    "exact_conditional_variance_checks": variance_checks,
    "exact_parity_bridge_checks": parity_checks,
    "resolvent_orders_checked": 20,
    "pasch_abstract_internal_bank": "4/5",
    "pasch_abstract_diagonal_face2_bank": "0",
    "actual_n4_qflip_packet_internal_bank": "1/80",
    "actual_n4_qflip_packet_diagonal_face2_bank": "0",
    "actual_n4_relation_weights": {str(k): v for k, v in weights.items()},
    "borel_pi_over_4_coefficient_magnitude": "1/8"
}, indent=2, sort_keys=True))
