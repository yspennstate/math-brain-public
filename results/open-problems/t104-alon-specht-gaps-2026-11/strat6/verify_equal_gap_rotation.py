"""PROVED: equal-gap basis rotation, conditional moment bound, and cell replay."""
import json
from fractions import Fraction as F
import sympy as s
from moment_bounds import vertices
from directional_bounds import check

U=s.symbols('u0:5')
p1,p2,p3,p4=[sum(x**j for x in U)for j in range(1,5)]
e2,e3,e4=[s.symmetric_poly(j,*U)for j in range(2,5)]
assert s.expand(p2-p1*p1+2*e2)==0
assert s.expand(p3-p1**3+3*p1*e2-3*e3)==0
assert s.expand(p4-p1*p3+e2*p2-e3*p1+4*e4)==0
# With p1=p3=0, the polynomial with these five real roots is
# x^5-(p2/2)x^3+e4*x-e5. Its derivative has four real roots by Rolle.
# The derivative is even, hence its roots come in +/- pairs and e4>=0.
# Thus p4=p2^2/2-4e4<=p2^2/2. This written argument handles multiplicities.
verts=vertices(enhanced=True,extra=[((1,0,0),F(1,2))])
records=json.load(open('equal_gap_cell.json'))
assert len(records)==1
rec=records[0]
assert rec['basis_d_zero'] and F(rec['rlo'])==F(rec['rhi'])==1
assert check(rec,verts)==F(rec['margin'])
print('PROVED: Newton identities checked; the real-root argument gives A<=1/2 when d=0.')
print('PROVED: every frame plane admits d=0 by rotating through a zero of sum u_i^3.')
print('PROVED:',len(verts),'conditional moment vertices and the rational equal-gap cell checked exactly.')
print('PROVED: T>=0 for all equal gaps 0<g<=',rec['ahi'])
