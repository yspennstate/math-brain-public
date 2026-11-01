#!/usr/bin/env python3
import itertools
import sympy as sp

p = sp.symbols("p")
q = 1-p
PTS = list(itertools.product([0,1], repeat=3))
MASK = 23  # +1 exactly on Hamming weights 0 and 1.

def f(y):
    idx = PTS.index(tuple(y))
    return 1 if ((MASK >> idx) & 1) else -1

def coeff_sq(S):
    num = 0
    for y in PTS:
        prob = sp.prod(p if bit else q for bit in y)
        centered = sp.prod(y[i]-p for i in S)
        num += f(y)*prob*centered
    return sp.factor(sp.cancel(num**2/(p*q)**len(S)))

single = coeff_sq({0})
pair = coeff_sq({0,1})
triple = coeff_sq({0,1,2})
assert sp.factor(single - 16*p**3*q**3) == 0
assert sp.factor(pair - 4*p**2*q**2*(2*p-1)**2) == 0
assert sp.factor(triple - 16*p**3*q**3) == 0
assert sp.factor(single-pair) == -4*p**2*(p-1)**2*(8*p**2-8*p+1)

roots = [sp.Rational(1,2)-sp.sqrt(2)/4, sp.Rational(1,2)+sp.sqrt(2)/4]
for r in roots:
    assert sp.simplify(8*r**2-8*r+1) == 0
    vals = []
    for k in range(1,4):
        for S in itertools.combinations(range(3), k):
            vals.append(sp.simplify(coeff_sq(set(S)).subs(p,r)))
    assert all(v > 0 for v in vals)
    assert all(sp.simplify(v-vals[0]) == 0 for v in vals)

cofactor_counts = {}
for A in itertools.combinations(range(3), 2):
    b = ({0,1,2}-set(A)).pop()
    cofs = set()
    for a in itertools.product([0,1], repeat=2):
        yy = [0,0,0]
        for j,i in enumerate(A): yy[i] = a[j]
        vals = []
        for xb in [0,1]:
            yy[b] = xb
            vals.append(f(yy))
        cofs.add(tuple(vals))
    cofactor_counts[A] = len(cofs)
    assert len(cofs) == 3

print("PASS")
print("mask =", MASK)
print("truth_table_plus_atoms =", [PTS[i] for i in range(8) if (MASK>>i)&1])
print("singleton_sq =", single)
print("pair_sq =", pair)
print("triple_sq =", triple)
print("zero_KL_biases =", roots)
print("cofactor_counts =", cofactor_counts)
print("spectral_law_at_each_root = uniform on the seven nonempty subsets")
print("occurrence_marginals = (4/7,4/7,4/7)")
print("I_projection_parameters = independent Bernoulli(1/2)^3 conditioned nonempty")
