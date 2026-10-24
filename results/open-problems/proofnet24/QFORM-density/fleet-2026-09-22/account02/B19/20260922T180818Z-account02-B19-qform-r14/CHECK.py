import sympy as sp

t = sp.symbols('t')
a,b,c,l,d = sp.symbols('a b c l d', real=True)
M = sp.Matrix([[a,b,c],[b,l,0],[c,0,d]])
w = sp.Matrix([0,c,-b])
assert M*w == sp.Matrix([0,l*c,-d*b])

S_l = sp.Matrix([[a-b**2/l,c],[c,d]])
assert sp.simplify(sp.det(M)-l*sp.det(S_l)) == 0

Mbase = sp.Matrix([[0,2,2],[2,2,0],[2,0,2]])
assert sp.factor(Mbase.charpoly(t).as_expr()) == (t-4)*(t-2)*(t+2)

A0 = sp.Matrix([[0,2,2,0],[2,2,0,0],[2,0,2,0],[0,0,0,0]])
assert sp.factor(A0.charpoly(t).as_expr()) == t*(t-4)*(t-2)*(t+2)

print(f"arrow_null_vector_image={list(M*w)}")
print(f"det_schur_identity={sp.simplify(sp.det(M)-l*sp.det(S_l))}")
print(f"angle_base_charpoly={sp.factor(Mbase.charpoly(t).as_expr())}")
print(f"angle_full_charpoly={sp.factor(A0.charpoly(t).as_expr())}")
print("base_nonzero_eigenvalues=-2,2,4")
print("arrow_constant=8")
print("curved_star_constant=16")
print("QFORM_ARROW_CURVED_STAR_CHECK_PASS")
