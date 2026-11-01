from sympy import Matrix, Rational, symbols, sqrt, simplify, factor

a,b,c,qe,qf,qg = symbols("a b c qe qf qg", positive=True)
M = Matrix([[qe,-a,-b],[-a,qf,-c],[-b,-c,qg]])
det_expected = qe*qf*qg - qe*c**2 - qf*b**2 - qg*a**2 - 2*a*b*c
assert simplify(M.det()-det_expected) == 0
print("determinant_identity=PASS")
print("detM=", factor(M.det()))

s = symbols("s", positive=True)
bound_poly = (qg+2)*a**2 + 2*s*a - s**2*qg
candidate = qg*s/(qg+2)
assert simplify(bound_poly.subs(a,candidate)) == 0
print("positive_root=qg*sqrt(qe*qf)/(qg+2):PASS")

assert simplify((qg*s/(qg+2)).subs({qg:1,s:1}) - Rational(1,3)) == 0
print("unit_universal_cap=1/3:PASS")

Ze,Ae,Zf,Af,Zg,Ag = symbols("Ze Ae Zf Af Zg Ag", positive=True)
qe_expr = Ze/Ae
qf_expr = Zf/Af
qg_expr = Zg/Ag
variance_scale = sqrt(Ze*Ae*Zf*Af)
lhs_factor = simplify(sqrt(qe_expr*qf_expr)*variance_scale)
assert simplify(lhs_factor-Ze*Zf) == 0
count_factor = simplify(qg_expr/(qg_expr+2))
assert simplify(count_factor-Zg/(Zg+2*Ag)) == 0
print("count_form=-Delta <= Zg/(Zg+2Z^g)*Ze*Zf:PASS")

d = 1/sqrt(3)
C = Matrix([[1,d**2,d],[d**2,1,d],[d,d,1]])
eigs_C = C.eigenvals()
eigs_2IC = (2*Matrix.eye(3)-C).eigenvals()
assert set(eigs_C.keys()) == {Rational(1,3), Rational(2,3), Rational(2,1)}
assert set(eigs_2IC.keys()) == {Rational(0,1), Rational(4,3), Rational(5,3)}
print("sharp_witness_rho_ef=1/3:PASS")
print("eig(C)=", sorted(eigs_C.keys(), key=float))
print("eig(2I-C)=", sorted(eigs_2IC.keys(), key=float))
print("ALL_CHECKS_PASS")
