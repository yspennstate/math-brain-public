import sympy as sp

m, delta, z, t = sp.symbols("m delta z t", nonzero=True)

a = m*(1+delta)
b = m*(1-delta)
c = a-b
p = m*(delta+z)
ab = a*b

k = sp.factor(2*z*(1-z**2)/((1-delta**2)*(delta+3*z)))
x = sp.factor((delta+z)*(1+z)*(1+delta+2*z)/(2*(1+delta)*(delta+3*z)))
y = sp.factor((delta+z)*(1-z)*(1-delta-2*z)/(2*(1-delta)*(delta+3*z)))

def check(name, expr):
    val = sp.factor(sp.cancel(expr))
    assert val == 0, (name, val)
    print(f"{name}: PASS")

check("normalization", x+y+k-1)
check("mean", a*x-b*y-p)

M2 = sp.expand(x*a**2 + y*b**2)
M3 = sp.expand(x*a**3 - y*b**3)
M4 = sp.expand(x*a**4 + y*b**4)
M5 = sp.expand(x*a**5 - y*b**5)

mu2 = sp.factor(M2-p**2)
mu3 = sp.factor(M3-3*p*M2+2*p**3)
mu4 = sp.factor(M4-4*p*M3+6*p**2*M2-3*p**4)
mu5 = sp.factor(M5-5*p*M4+10*p**2*M3-10*p**3*M2+4*p**5)

kappa4 = sp.factor(mu4-3*mu2**2)
kappa5 = sp.factor(mu5-10*mu3*mu2)

Q = sp.factor((delta+z)*(1-z**2)/(delta+3*z))
R = sp.factor(-2*(delta+z)*(1-z**2)*
              (delta**2*z+3*delta*z**2+delta+3*z**3)/(delta+3*z)**2)

check("second_cumulant_Q", mu2-m**2*Q)
check("cubic_null", mu3)
check("fourth_cumulant_R", kappa4-m**4*R)
check("fifth_support_recurrence",
      kappa5-(c-3*p)*(kappa4+2*mu2**2))

# Excluded denominator branch delta+3z=0: p=c/3.
p_bad = c/3
q_bad = sp.factor(c*p_bad + ab*(1-k) - p_bad**2)
ell3_bad = sp.factor((c-2*p_bad)*q_bad + ab*k*p_bad)
target_bad = sp.factor(2*m**3*delta*(9-delta**2)/27)
check("denominator_branch_nonzero_formula", ell3_bad-target_bad)

# C=0 implies z in {0,+/-1}; positive x,y rules out +/-1.
# At z=0 the fourth cumulant is strictly negative.
check("C0_quartic_value", R.subs(z,0)+2)

# Balanced specialization and singular balanced blow-up.
check("balanced_k", k.subs(delta,0)-2*(1-z**2)/3)
check("balanced_R", R.subs(delta,0)-sp.Rational(2,3)*z**2*(z**2-1))

lim_k = sp.simplify(sp.limit(k.subs(z,t*delta), delta, 0))
lim_R = sp.simplify(sp.limit(R.subs(z,t*delta), delta, 0))
check("balanced_blowup_k", lim_k-2*t/(1+3*t))
check("balanced_blowup_R", lim_R+2*(t+1)/(1+3*t)**2)

print("ALL_EXACT_SYMBOLIC_CHECKS_PASS")
