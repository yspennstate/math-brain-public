import sympy as sp
import math
import json

a,r,s,k,lam=sp.symbols('a r s k lam', nonzero=True)
B=sp.Matrix([
    [a,a*r,a*s],
    [a*r,a*r**2,a*r*s+k],
    [a*s,a*r*s+k,a*s**2],
])
Binv=sp.simplify(B.inv())
M=sp.Matrix([[1,1,1],[1,1,-1],[1,-1,1]])
mins=[sp.det(M.extract([i,j],[i,j])) for i,j in [(0,1),(0,2),(1,2)]]
h=6.266
C=4*h**0.75
out={
    'det_family': str(sp.factor(B.det())),
    'inverse_family': str(Binv),
    'inverse_check': str(sp.simplify(B*Binv)),
    'example_principal_2x2_minors': [str(x) for x in mins],
    'example_charpoly': str(sp.factor(M.charpoly(lam).as_expr())),
    'example_eigenvalues': {str(kk): int(vv) for kk,vv in M.eigenvals().items()},
    'coarea_constant_if_H3_lt_6.266': C,
    'spectral_special_family_constant_using_abs_a_k_ge_1_over_3': C*math.sqrt(3),
    'example_M_constant_a1_kminus2': C/math.sqrt(2),
}
print(json.dumps(out, indent=2))
