#!/usr/bin/env python3
"""
Exact algebraic self-check for D0009 third successor run.

Checks:
1. two-point fixed-mean layer extreme identities;
2. integer-occupancy length/mean identities;
3. the exact n=3 rational worked example;
4. a three-atom layer law and its barycentric reconstruction;
5. explicit constant-sum formulas for both components of that example.

All arithmetic is symbolic or rational. This is a self-check of the finite/algebraic
core, not an independent audit and not a source-general sampler.
"""
import sympy as sp

a,b,m,n,k = sp.symbols("a b m n k", positive=True)
alpha = (b-m)/(b-a)
beta = (m-a)/(b-a)

assert sp.simplify(alpha + beta - 1) == 0
assert sp.simplify(alpha*a + beta*b - m) == 0

m_occ = ((n-k)*a + k*b)/n
assert sp.simplify((n-k)*a + k*b - n*m_occ) == 0
assert sp.simplify((1-k/n)*a + (k/n)*b - m_occ) == 0

print("SYMBOLIC alpha+beta=1 PASS")
print("SYMBOLIC extreme mean alpha*a+beta*b=m PASS")
print("SYMBOLIC integer occupancy total length=n*m PASS")

# Exact n=3 worked extreme:
# m=2/3, a=1/2, b=1 gives beta=1/3 and k=1.
Q = sp.Rational
n0 = 3
a0, b0, m0 = Q(1,2), Q(1,1), Q(2,3)
alpha0 = sp.simplify((b0-m0)/(b0-a0))
beta0 = sp.simplify((m0-a0)/(b0-a0))
assert alpha0 == Q(2,3)
assert beta0 == Q(1,3)
assert n0*beta0 == 1

v = sp.symbols("v", real=True)
y1 = Q(1,4) + v/2
y2 = y1
y3 = Q(1,2) - v
assert sp.simplify(y1+y2+y3) == 1
assert [sp.simplify(y1.subs(v,t)) for t in (-Q(1,2),Q(1,2))] == [0,Q(1,2)]
assert [sp.simplify(y3.subs(v,t)) for t in (-Q(1,2),Q(1,2))] == [1,0]
print("EXAMPLE pair component alpha=2/3 beta=1/3 k=1 PASS")
print("EXAMPLE pair component constant sum=1 and exact uniform ranges PASS")

# Three-atom layer law H:
# weights 1/3 at 1/2, 1/2 at 2/3, 1/6 at 1.
hl, hm, hu = Q(1,3), Q(1,2), Q(1,6)
assert hl+hm+hu == 1
assert sp.simplify(hl*a0 + hm*m0 + hu*b0) == m0
C_lo = sp.simplify(hl*(m0-a0))
C_hi = sp.simplify(hu*(b0-m0))
assert C_lo == C_hi == Q(1,18)
Pi_mass = sp.simplify((b0-a0)/C_lo * hl*hu)
assert Pi_mass == Q(1,2)
assert sp.simplify(Pi_mass*alpha0) == hl
assert sp.simplify(Pi_mass*beta0) == hu
print("EXAMPLE layer law mass=1 mean=2/3 deficit=surplus=1/18 PASS")
print("EXAMPLE barycentric reconstruction atom_mass=1/2 pair_mass=1/2 PASS")

# Uniform atom U[0,2/3] has an explicit 3-complete-mix line sampler.
w = sp.symbols("w", real=True)
z1, z2, z3 = w, w+Q(1,3), Q(2,3)-2*w
assert sp.simplify(z1+z2+z3) == 1
assert [z1.subs(w,t) for t in (0,Q(1,3))] == [0,Q(1,3)]
assert [z2.subs(w,t) for t in (0,Q(1,3))] == [Q(1,3),Q(2,3)]
assert [z3.subs(w,t) for t in (0,Q(1,3))] == [Q(2,3),0]
print("EXAMPLE atom component constant sum=1 and pooled U[0,2/3] ranges PASS")

# Mixture weights reproduce the target layer law exactly.
assert hm == Pi_mass == Q(1,2)
print("EXAMPLE component mixing weights 1/2 + 1/2 PASS")
print("ALL EXACT CHECKS PASSED")
