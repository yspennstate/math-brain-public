from sympy import symbols, exp, integrate, simplify, diff, E

s,u = symbols('s u', nonnegative=True)

m1 = 1-exp(-s)
m2 = 2*(1-(s+1)*exp(-s))
assert simplify(diff(m1,s) - (1-m1)) == 0
assert simplify(diff(m2,s) - (2*m1-m2)) == 0
assert simplify(m1.subs(s,0)) == 0
assert simplify(m2.subs(s,0)) == 0
m3_at_1 = simplify(3*integrate(m2,(s,0,1)))
assert simplify(m3_at_1 - (18/E-6)) == 0

q = 1-exp(-s)
q1 = 1-exp(-1)
G3 = simplify(integrate(q**3,(s,0,1)) + q1**3/3)
claimed_G3 = simplify((4*E-E**2-1)/(2*E**2))
assert simplify(G3-claimed_G3) == 0

limcoef = simplify(m3_at_1/(6*G3))
claimed_coef = simplify(2*E*(3-E)/(4*E-E**2-1))
assert simplify(limcoef-claimed_coef) == 0

print('P24 AV-P3 ENDPOINT CONSTANT CHECK')
print('PASS m3 = 18/e - 6')
print('PASS G3 = (4e-e^2-1)/(2e^2)')
print('PASS liminf coefficient m3/(6G3) = 2e(3-e)/(4e-e^2-1)')
print('ALL_EXACT_CHECKS_PASS')
