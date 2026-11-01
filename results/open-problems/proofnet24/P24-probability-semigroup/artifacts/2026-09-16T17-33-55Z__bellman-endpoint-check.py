import sympy as sp

p, eps, q = sp.symbols('p eps q', positive=True)
a = 1 - (1+eps)*(p-1)/2
b = p*(p-1)*(1+1/eps)/4
assert sp.simplify(a - (3-p-(p-1)*eps)/2) == 0
R2 = sp.factor(b/a)
expected = p*(p-1)*(1+1/eps)/(2*(3-p-(p-1)*eps))
assert sp.simplify(R2-expected) == 0

# Verify the optimizer after the substitution p-1=q^2, 0<q<sqrt(2).
R2q = sp.factor(R2.subs(p, q**2+1))
eps_star_q = sp.sqrt(2)/q - 1
numq = sp.together(sp.diff(R2q, eps)).as_numer_denom()[0]
assert sp.simplify(numq.subs(eps, eps_star_q)) == 0
R2_star_q = sp.factor(sp.cancel(R2q.subs(eps, eps_star_q)))
expected_star_q = (q**2+1)*q**2/(2*(sp.sqrt(2)-q)**2)
assert sp.simplify(R2_star_q-expected_star_q) == 0

# Exact rational spot checks in 2<p<3 with admissible rational eps.
checks = [
    (sp.Rational(5,2), sp.Rational(1,10)),
    (sp.Rational(8,3), sp.Rational(1,20)),
    (sp.Rational(11,4), sp.Rational(1,25)),
]
for pp, ee in checks:
    threshold = (3-pp)/(pp-1)
    assert 0 < ee < threshold
    aa = sp.factor(a.subs({p:pp, eps:ee}))
    rr = sp.factor(R2.subs({p:pp, eps:ee}))
    assert aa > 0 and rr > 0
    print(f'p={pp} eps={ee} threshold={threshold} a={aa} C^2={rr}')

# Critical coefficient: no positive eps is admissible at p=3.
assert sp.simplify(a.subs(p, 3)) == -eps

print('C^2(p,eps) =', R2)
print('epsilon_star = sqrt(2/(p-1)) - 1')
print('C_opt^2 = p*(p-1)/(2*(sqrt(2)-sqrt(p-1))^2)')
print('critical_a_p3 =', sp.simplify(a.subs(p,3)))
print('ALL_EXACT_CHECKS_PASS')
