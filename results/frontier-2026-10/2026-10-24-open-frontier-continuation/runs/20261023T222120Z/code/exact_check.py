"""Exact algebra checks only; this is not a finite-width simulation."""
import json
import sympy as s
t=s.symbols('t', real=True)
K=s.Matrix([[2,1],[1,2]])
r=s.Matrix([2*s.exp(-3*t)-s.exp(-t),2*s.exp(-3*t)+s.exp(-t)])
J=s.Matrix([-s.Rational(1,3)+s.exp(-t)-s.Rational(2,3)*s.exp(-3*t),s.Rational(5,3)-s.exp(-t)-s.Rational(2,3)*s.exp(-3*t)])
assert s.simplify(r.diff(t)+K*r)==s.zeros(2,1)
assert r.subs(t,0)==s.Matrix([1,3])
assert s.simplify(J.diff(t)-r)==s.zeros(2,1)
assert J.subs(t,0)==s.zeros(2,1)
z=(s.sqrt(3)-1)/2
cross=s.log(1+s.sqrt(3))
at=lambda e:s.simplify(e.subs(s.exp(-3*t),z**3).subs(s.exp(-t),z))
assert at(J[0])==0
assert at(r[0])==s.sqrt(3)-2
assert at(r[1])==2*s.sqrt(3)-3
assert at(J[1])==3-s.sqrt(3)
assert float(J[0].subs(t,2))<-.19
print(json.dumps({'kind':'exact symbolic identities with numerical evaluations','sympy_version':s.__version__,'checks_passed':8,'candidate_crossing_time':str(cross),'candidate_crossing_time_numeric':float(cross),'candidate_J1_at_2':float(J[0].subs(t,2)),'candidate_r1_at_crossing':str(at(r[0])),'candidate_r2_at_crossing':str(at(r[1])),'candidate_J2_at_crossing':str(at(J[1])),'scope':'candidate constant phase only; no simulated or proved full hybrid convergence'},indent=2))
