from sympy import Matrix, Rational, sqrt, diag, simplify, N, E

# Exact spectral basis and Parseval frame.
u = Matrix([1,-1,0])/sqrt(2)
w = Matrix([1,1,2])/sqrt(6)
v = Matrix([-1,-1,1])/sqrt(3)
Lam = diag(1,1,-1)
rows = [v/2]*4 + [u/sqrt(2)]*2 + [w/sqrt(2)]*2
G = sum((r*r.T for r in rows), Matrix.zeros(3))
assert simplify(G-Matrix.eye(3)) == Matrix.zeros(3)
assert max([simplify((r.T*r)[0]) for r in rows]) == Rational(1,2)

P = Matrix.hstack(u,w,v)
Qb = simplify(P.T*Lam*P)
Qexpected = Matrix([
    [1, 0, 0],
    [0, -Rational(1,3), -2*sqrt(2)/3],
    [0, -2*sqrt(2)/3, Rational(1,3)],
])
assert simplify(Qb-Qexpected) == Matrix.zeros(3)

# Pivot r_5=u/sqrt(2) for the completed account03/B16 theorem.
pivot = rows[4]
ell = simplify((pivot.T*pivot)[0])
a = simplify((pivot.T*Lam*pivot)[0])
assert ell == Rational(1,2)
assert a == Rational(1,2)
# Residual leverages in u^perp: four v/2 rows ->1/4, two w/sqrt2 ->1/2,
# and the duplicate u/sqrt2 row ->0.
residual_leverages = [Rational(1,4)]*4 + [0] + [Rational(1,2)]*2
assert max(residual_leverages) == Rational(1,2)
partner_constant = 4*sqrt(6*E)

# Robust fiber bounds used in the proof.  For 0<delta<=1/100 and
# |z1|,|z2|<delta/64, the thin t-overlap width lies in [15d/16,17d/16]
# and contains [-d/2,-d/4].  The u/w overlaps have widths in
# [31/32,33/32] under |z5|,|z7|<1/(64sqrt2).
delta_max = Rational(1,100)
t_width_lo = Rational(15,16)
t_width_hi = Rational(17,16)
trans_width_lo = Rational(31,32)
trans_width_hi = Rational(33,32)
mass_factor_hi = simplify(trans_width_hi**2 * t_width_hi)
assert mass_factor_hi == Rational(18513,16384)

# On t in [-delta/2,-delta/4], r in [6|t|,1/8], the q=0 root
# s=-3t^2/r stays inside the transverse support.  The following is the
# worst elementary upper bound on |beta| from the report.
beta_abs_hi = simplify(sqrt(3)/2*(Rational(1,8)+delta_max/4) + sqrt(2)*delta_max)
assert N(beta_abs_hi) < N(Rational(31,64))
alpha_abs_hi = Rational(1,16) + delta_max/8
assert alpha_abs_hi < Rational(31,64)

# The robust normalized trace lower-bound coefficient.
robust_coeff = simplify((sqrt(3)/8) / mass_factor_hi)
assert robust_coeff == 2048*sqrt(3)/18513

print('PASS')
print('Gram=', G)
print('Q_in_uwv_basis=', Qb)
print('pivot_ell=', ell, 'pivot_a=', a)
print('max_residual_leverage=', max(residual_leverages))
print('mass_factor_hi=', mass_factor_hi, float(mass_factor_hi))
print('robust_log_coefficient=', robust_coeff, float(N(robust_coeff,16)))
print('partner_full_density_bound=', partner_constant, float(N(partner_constant,16)))
