import sympy as sp

a, s, delta, d, m = sp.symbols('a s delta d m', positive=True)
F = (2-s)*a**2 + 2*a*(2*delta-3+s) - s

print('dF_ds=', sp.factor(sp.diff(F, s)))
print('F_at_s1=', sp.factor(F.subs(s, 1)))
print('density_sub=', sp.factor(F.subs({s: 1, delta: d+1})))

root = sp.sqrt(4*d**2 + 1) - 2*d
print('general_root_residual=', sp.simplify(root**2 + 4*d*root - 1))

root6 = sp.sqrt(145) - 12
print('d6_root=', root6)
print('d6_root_residual=', sp.simplify(root6**2 + 24*root6 - 1))
print('d6_decimal=', sp.N(root6, 18))

rootm = sp.sqrt(4*m**2/9 + 1) - 2*m/3
print('mindegree_root_residual=', sp.simplify(rootm**2 + 4*(m/3)*rootm - 1))
print('STATUS=PASS')
