import sympy as sp
import math

A0 = sp.Rational(57, 8)
B0 = sp.Rational(3, 4)
D = sp.simplify((sp.sqrt(A0) + sp.sqrt(B0))**2)
cstar = sp.simplify(D / 20)
alpha = sp.simplify(sp.sqrt(A0) / (sp.sqrt(A0) + sp.sqrt(B0)))

assert sp.simplify(D - (sp.Rational(63, 8) + sp.sqrt(342)/4)) == 0
assert sp.simplify(cstar - (sp.Rational(63, 160) + sp.sqrt(342)/80)) == 0
assert sp.simplify(alpha - (sp.Rational(19,17) - sp.sqrt(38)/17)) == 0

p, r = 25, 4
rows = []
for j in range(4):
    assert p*p - 38*r*r == 17
    assert (p - 2*r) % 17 == 0
    k = (19*r - p)//17
    q = r-k
    assert 2 <= k <= r-1
    cr = sp.simplify(sp.Rational(r,20)*(A0/k + B0/q))
    delta = sp.simplify(k-alpha*r)
    exact_delta = sp.simplify(-1/(p+r*sp.sqrt(38)))
    assert sp.simplify(delta-exact_delta) == 0
    exact_gap = sp.simplify(D/(20*k*q*(p+r*sp.sqrt(38))**2))
    assert sp.simplify(cr-cstar-exact_gap) == 0
    rows.append((j,r,k,q,p,sp.N(cr,25),sp.N(exact_gap,25)))
    p, r = 37*p+228*r, 6*p+37*r

K = 2*math.sqrt(2)*math.asin(4/5) + math.sqrt(5)*(math.pi/2-math.asin(4/5))
assert K < 3*math.sqrt(2)

print('QFORM_B17_PELL_PERIODIC_CHECK_PASS')
print('alpha =', sp.N(alpha,30))
print('D =', sp.N(D,30))
print('c_star =', sp.N(cstar,30))
for row in rows:
    print(row)
print('partner K = %.15f' % K)
print('partner gap = %.15f' % (3*math.sqrt(2)-K))
