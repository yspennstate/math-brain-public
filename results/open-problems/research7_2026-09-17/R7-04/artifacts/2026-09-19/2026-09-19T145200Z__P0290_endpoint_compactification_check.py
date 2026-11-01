import sympy as sp

a, r, lam = sp.symbols("a r lam", positive=True, real=True)
M = sp.Matrix([[-4,-a,a],[a,-2*a,a],[-a,a,-4]])
Minv = sp.simplify(M.inv())
S1 = sp.simplify((Minv + Minv.T)/2)
Minv2 = sp.simplify(Minv**2)
S2 = sp.simplify((Minv2 + Minv2.T)/2)

assert sp.simplify(M*Minv - sp.eye(3)) == sp.zeros(3)
assert sp.simplify(S1[1:,1:].det() - 1/(8*a)) == 0
assert sp.simplify(S2[1:,1:].det() - (8-a**2)/(512*a**2)) == 0
assert sp.simplify(S2.det() - (a-4)*(a+12)*(a**2-8)/(524288*a**2)) == 0

B = sp.simplify(-S1-sp.eye(3)/5)
mins = [sp.factor(B[:i,:i].det()) for i in (1,2,3)]
expected_mins = [
    -(5*a-8)/160,
    -(5*a-8)*(5*a**2-32*a+80)/(25600*a),
    (5*a-8)*(5*a**2+4*a-10)/(64000*a),
]
assert all(sp.simplify(x-y)==0 for x,y in zip(mins, expected_mins))

dH0 = sp.simplify((sp.diff(M,a)+sp.diff(M,a).T)/12)
assert sp.simplify(dH0[1:,1:].det() + sp.Rational(1,36)) == 0

gen_num = sp.factor(sp.together((S2[1:,1:] - r*(-S1[1:,1:])).det()).as_numer_denom()[0])
expected_gen = -2*a**2*r - a**2 + 64*a*r**2 - 16*a*r - 32*r + 8
assert sp.simplify(gen_num - expected_gen) == 0
D = a**4+80*a**3+96*a**2-256*a+256
assert sp.simplify(sp.discriminant(gen_num,r) - 4*D) == 0

sqdiff = sp.factor((sp.Rational(192,5)-(a+4)**2)**2-D)
expected_sq = -sp.Rational(64,25)*(25*a**3+30*a**2+40*a-96)
assert sp.simplify(sqdiff-expected_sq) == 0
reven = sp.factor(S2[0,0]/(-S1[0,0]))
expected_reven = (a-4)*(a+12)/(32*(a-8))
assert sp.simplify(reven-expected_reven) == 0
revendiff = sp.factor(sp.Rational(3,5)/a-reven)
expected_revendiff = -(5*a**3+40*a**2-336*a+768)/(160*a*(a-8))
assert sp.simplify(revendiff-expected_revendiff) == 0

char = sp.factor((lam*sp.eye(3)-M).det())
mu3 = -2*a + sp.Rational(1,8)*a**3
char_mu = sp.expand(char.subs(lam,mu3))
assert all(char_mu.coeff(a,k) == 0 for k in (1,2,3))
ser = sp.series(char_mu,a,0,6)

print("det(S1_odd) =", sp.factor(S1[1:,1:].det()))
print("det(S2_odd) =", sp.factor(S2[1:,1:].det()))
print("det(S2) =", sp.factor(S2.det()))
print("Sylvester minors of -S1-I/5 =", mins)
print("det(d/da H_a(0)|odd) =", sp.factor(dH0[1:,1:].det()))
print("odd generalized-eigen numerator =", gen_num)
print("odd discriminant =", sp.factor(sp.discriminant(gen_num,r)))
print("3/(5a)-r_even =", revendiff)
print("squared r_max margin =", sqdiff)
print("charpoly(mu3) series =", ser)
print("ALL_SYMBOLIC_CHECKS_PASS")
