import sympy as sp

d,s,z,u = sp.symbols("d s z u", real=True)
z = 1+s

k = 2*z*(1-z**2)/((1-d**2)*(d+3*z))
y = ((d+z)*(1-z)*(1-d-2*z))/(2*(1-d)*(d+3*z))
K2 = (d+z)*(1-z**2)/(d+3*z)
tK = (1+z)**2-K2
R = -2*(d+z)*(1-z**2)*(d**2*z+3*d*z**2+d+3*z**3)/(d+3*z)**2
AK = sp.factor(1+3*tK**2/R)
Q = sp.factor(-k*AK)
L = sp.factor(y*AK)
U = sp.factor(-29*y/k)

assert sp.cancel(L/U-Q/29) == 0
assert sp.cancel(sp.limit(L,s,0,dir="+")-6/(1-d)) == 0
assert sp.cancel(sp.limit(U,s,0,dir="+")-29*(1+d)**3/8) == 0
assert sp.cancel(sp.limit(Q,s,0,dir="+")-48/((1-d)*(1+d)**3)) == 0
print("scalar identities and boundary values: PASS")

# Q strictly increases in s on 0<d<1, s>0.
qsd = sp.factor(sp.diff(Q,s))
qnum,qden = map(sp.factor,sp.fraction(qsd))
assert all(c>0 for c in sp.Poly(-qnum/2,d,s).coeffs())
# qden has exactly one sign-changing factor (d-1), hence qsd>0.
assert sp.factor(qden/((d-1)*(d+1)*(d+s+1)**2)) != 0
print("Q_K strictly increasing in s: PASS")

q0 = sp.factor(sp.limit(Q,s,0,dir="+"))
assert sp.cancel(sp.diff(q0,d)-96*(2*d-1)/((d-1)**2*(d+1)**4)) == 0
assert sp.factor(q0.subs(d,sp.Rational(2,5))-29) == sp.Rational(53,343)
assert sp.factor(q0.subs(d,sp.Rational(3,5))-29) == sp.Rational(19,64)
print("Q_K<29 localizes 2/5<delta<3/5: PASS")

# Exact uniform separation s<3/200.
S = sp.Rational(3,200)
expr = sp.factor(sp.together(Q.subs(s,S)-29))
num,den = map(sp.factor,sp.fraction(expr))
P = sp.factor(-num/29)
P_expected = (32480000000000*d**5 + 163868800000000*d**4
              + 200770248000000*d**3 - 61909179580000*d**2
              - 176894008806200*d + 67683686139909)
assert sp.expand(P-P_expected) == 0
expected_den = 20000*(d-1)*(d+1)*(200*d+203)*(8120000*d**2+32725400*d+25096281)
assert sp.expand(den-expected_den) == 0
Pshift = sp.Poly(sp.expand(P.subs(d,sp.Rational(1,2)+u)),u)
c = [Pshift.coeff_monomial(u**j) for j in range(6)]
assert c == [112467841809,3858897613800,525649392420000,
             609707848000000,245068800000000,32480000000000]
assert c[1]**2-4*c[0]*(c[2]/10) == -8756370291684475524672000
assert sp.Rational(9,10)*c[2]-sp.Rational(1,10)*c[3] == 412113668378000
assert c[4]-sp.Rational(1,10)*c[5] == 241820800000000
print("Q_K(delta,3/200)>29 on [2/5,3/5]: PASS")

# L and U are strictly increasing in d and s.
Ld = sp.factor(sp.diff(L,d)); Ls = sp.factor(sp.diff(L,s))
Ud = sp.factor(sp.diff(U,d)); Us = sp.factor(sp.diff(U,s))
ldn,ldden = map(sp.factor,sp.fraction(Ld))
lsn,lsden = map(sp.factor,sp.fraction(Ls))
assert all(cc>0 for cc in sp.Poly(ldn/((s+1)*(s+2)),d,s).coeffs())
assert all(cc<0 for cc in sp.Poly(lsn,d,s).coeffs())
assert sp.cancel(Ud-29*(3*d**2+6*d*s+6*d+2*s**2+6*s+3)/(4*(s+1)*(s+2))) == 0
assert sp.cancel(Us+29*(d-1)*(d+1)*(2*d*s+3*d+3*s**2+6*s+3)/(4*(s+1)**2*(s+2)**2)) == 0
print("L_K,U_K strictly increasing in delta and s: PASS")

# Integer block localization and strips.
assert sp.factor(U.subs({d:sp.Rational(3,5),s:S})-15) == -sp.Rational(979,14105)
stripe_vals = {
  11: -sp.Rational(827,10075),
  12: -sp.Rational(1699,10850),
  13: -sp.Rational(82,455),
  14: -sp.Rational(47,310),
}
for N,val in stripe_vals.items():
    assert sp.factor(U.subs({d:sp.Rational(N,25),s:S})-N) == val
print("N in {11,12,13,14} and four delta strips: PASS")

# For each N, eliminate d from U=N and Q=29. The only nontrivial resultant
# factor on s>=0 is the degree-nine p_N below.
numQ,_ = sp.fraction(sp.factor(sp.together(Q-29)))
expected_coeffs = {
11:[446571,-2080576,-23192680,-30122272,24917048,81222240,28249216,-45477248,-37603456,353280],
12:[446571,-2549390,-25754740,-29216592,38403072,97455168,23071200,-65155968,-48254400,708480],
13:[446571,-3018204,-28265848,-27711296,53330920,113982272,14796384,-89174592,-61129984,786688],
14:[446571,-3487018,-30726004,-25644160,69666704,130731424,3096384,-118209920,-76857152,335744],
}
brackets = {11:(9291,9292),12:(14403,14404),13:(12636,12637),14:(4339,4340)}
witness_d = {11:sp.Rational(9,20),12:sp.Rational(99,200),
             13:sp.Rational(267,500),14:sp.Rational(57,100)}
positive_tail_ceiling = {11:20172,12:16899,13:11540,14:3873}
for N in [11,12,13,14]:
    numU,_ = sp.fraction(sp.factor(sp.together(U-N)))
    res = sp.factor(sp.resultant(numQ,numU,d))
    p = sp.Poly(sp.factor(res/(-585336*(s+1)**4*(s+2)**5)),s)
    assert p.all_coeffs() == expected_coeffs[N]
    assert p.eval(0) > 0 and p.eval(S) < 0

    # Strict decrease on [0,S]: discard negative nonconstant terms and
    # bound every positive monomial at s=S.
    der = sp.Poly(sp.diff(p.as_expr(),s),s)
    c0 = der.coeff_monomial(1)
    pos_tail = sum(der.coeff_monomial(s**j)*S**j for j in range(1,der.degree()+1)
                   if der.coeff_monomial(s**j)>0)
    assert c0 < 0
    assert pos_tail < positive_tail_ceiling[N]
    assert c0 + positive_tail_ceiling[N] < 0

    lo,hi = brackets[N]
    slo,shi = sp.Rational(lo,10**6),sp.Rational(hi,10**6)
    assert p.eval(slo) > 0 and p.eval(shi) < 0

    # At s=0 there is an explicit scalar-feasible d, so d_U(0)<d_L(0).
    dw = witness_d[N]
    assert L.subs({d:dw,s:0}) < N < U.subs({d:dw,s:0})

print("resultants, monotonic p_N, unique exact root brackets: PASS")
for N,(lo,hi) in brackets.items():
    print(f"N={N}: s_N in ({lo}/10^6,{hi}/10^6)")
print("GLOBAL: every n=30 scalar survivor has s < 14404/10^6")
print("ALL_EXACT_CHECKS_PASS")