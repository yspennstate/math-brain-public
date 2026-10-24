from sympy import symbols, sqrt, Rational, factor, simplify

D, r = symbols('D r', positive=True)
q = D - 1
L = 1 + D * (D-r) / (D-1)

# Upper-branch equality algebra for beta_D(r)=L_D(r).
radical_squared_identity = factor((2*L-r)**2 - (r**2 - 4*q))
expected_factor = 4 * (r-D) * (-D**3 + 2*D**2*r - 3*D**2 - D*r + 4*D - 1) / (D-1)**2
assert simplify(radical_squared_identity - expected_factor) == 0

r_star = factor((D**3 + 3*D**2 - 4*D + 1) / (D*(2*D-1)))
r_bs = factor((D**2 + D - 1) / (2*D-1))
rho_star = factor(r_star / D)
rho_bs = factor(r_bs / D)
assert factor(rho_star-rho_bs) == (D-1)/D**2
assert factor(rho_star-Rational(1,2)) == (7*D**2-8*D+2)/(2*D**2*(2*D-1))

# At r_star, the square-root sign is valid for every integer D>=5:
# P=(D-5)D^2+4D-1>0.  Also the discriminant is exactly a square.
P = D**3 - 5*D**2 + 4*D - 1
assert factor((r_star**2 - 4*(D-1)) - P**2/(D**2*(2*D-1)**2)) == 0
assert factor((2*L-r).subs(r,r_star) - P/(D*(2*D-1))) == 0

# Low-degree branch roots: L_D(r)=sqrt(D-1) occurs before the NB branch point.
r3 = (11-2*sqrt(2))/3
r4 = (19-3*sqrt(3))/4
L3 = simplify(L.subs({D:3,r:r3}))
L4 = simplify(L.subs({D:4,r:r4}))
assert simplify(L3-sqrt(2)) == 0
assert simplify(L4-sqrt(3)) == 0
# r3<2sqrt2 iff 121<128; r4<2sqrt3 iff 361<363.
assert 121 < 128
assert 361 < 363

# D>=5 upper branch starts on the correct side.  At D=5 it is already strict,
# and for t=sqrt(D-1)>=2 the exact factor is
# (t-1)(t^3-2t^2+t-1)/t^2 > 0.
t = symbols('t', positive=True)
D_t = t**2 + 1
edge_gap = simplify((1 + D*(D-2*sqrt(D-1))/(D-1) - sqrt(D-1)).subs(D,D_t))
assert factor(edge_gap) == (t-1)*(t**3-2*t**2+t-1)/t**2

# Exact tree calibration of the stronger Cheeger-form criterion:
# phi_E(T_D)=D-2, beta_D(2sqrt(D-1))=sqrt(D-1), and sqrt(q)<q for q>=2.
for d in range(3, 101):
    assert sqrt(d-1) < d-1

# Frozen noncentral genus-three semidirect example used in the report.
# Quotient: standard genus-3 surface Cayley graph, D=12, r_Q<=4sqrt(3).
d = 12
rq = 4*sqrt(3)
phi_lb = simplify(d*(d-rq)/(d-1))
pc_ub = simplify(1/(1+phi_lb))
beta = simplify((rq+sqrt(rq**2-4*(d-1)))/2)
pu_lb = simplify(1/beta)
gap = simplify(pu_lb-pc_ub)
assert phi_lb == Rational(144,11)-Rational(48,11)*sqrt(3)
assert beta == 1+2*sqrt(3)
assert pu_lb == -Rational(1,11)+Rational(2,11)*sqrt(3)
assert pc_ub == Rational(1705,17113)+Rational(528,17113)*sqrt(3)
assert gap == -Rational(35868,188243)+Rational(28418,188243)*sqrt(3)
# gap > 7/100 iff 2,841,800 sqrt(3) > 4,904,501.
margin = 2841800**2 * 3 - 4904501**2
assert margin == 173351660999 and margin > 0

# Finite falsification scan of the D>=5 threshold ordering, exact algebraic comparisons.
for d in range(5, 501):
    rs = r_star.subs(D,d)
    edge = 2*sqrt(d-1)
    Lfun = lambda x: 1 + Rational(d,d-1)*(d-x)
    # exact signs through SymPy algebraic-number comparison
    assert rs > edge
    assert Lfun(edge) > sqrt(d-1)
    # r_star is below D and the sign used after squaring is positive
    assert rs < d
    assert P.subs(D,d) > 0

print('PROB10-09 SPECTRAL-CHEEGER COVER EXACT CHECK')
print('upper_branch_factor=', radical_squared_identity)
print('r_star=', r_star)
print('rho_star=', rho_star)
print('rho_star_minus_classical_BS_Mohar=', factor(rho_star-rho_bs))
print('rho_star_minus_one_half=', factor(rho_star-Rational(1,2)))
print('D3_threshold_r=', r3)
print('D4_threshold_r=', r4)
print('genus3_phi_lower=', phi_lb)
print('genus3_pc_upper=', pc_ub)
print('genus3_beta=', beta)
print('genus3_pu_lower=', pu_lb)
print('genus3_gap_lower=', gap)
print('genus3_gap_gt_7_over_100_square_margin=', margin)
print('finite_D_scan=5..500 PASS')
print('ALL_EXACT_CHECKS_PASS')
