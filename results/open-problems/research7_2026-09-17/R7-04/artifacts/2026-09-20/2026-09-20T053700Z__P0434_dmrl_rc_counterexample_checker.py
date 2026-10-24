import sympy as sp

# P0434 / P01-A exact symbolic self-check for the DMRL-collapse theorem,
# the high-load failure of P01-B's strengthened RC inequality, and the
# contact-adaptive residual-credit correction.

rho = sp.symbols('rho', positive=True)
Q = sp.symbols('Q', positive=True)
s = 1-rho
sqrt_s = sp.sqrt(s)
c = sp.factor(2/(1+sqrt_s))
L = -sp.log(1-rho)/rho

# On a whole-line Gittins valley with a_V=s_V=1-rho,
# Omega_V must equal (c(rho)-1) Q.
Omega = sp.factor(Q*(s + s/s - 2*sqrt_s)/(1-s))
assert sp.simplify(Omega-(c-1)*Q) == 0
print('WHOLE_VALLEY_WAITING_CREDIT_IDENTITY_PASS')

# The strengthened RC inequality with Xi=0 differs from equality by
# -(L/2-1)m.  Here m is normalized to one.
rc_lhs_minus_rhs = sp.simplify((c-1)*Q - ((c-1)*Q + (L/2-1)))
assert sp.simplify(rc_lhs_minus_rhs - (1-L/2)) == 0
print('RC_GAP_IDENTITY_PASS', rc_lhs_minus_rhs)

# Mean-one Erlang-2 witness: survival S=e^{-2x}(1+2x),
# integrated tail N=e^{-2x}(1+x), hence strictly decreasing MRL.
x = sp.symbols('x', nonnegative=True)
S = sp.exp(-2*x)*(1+2*x)
N = sp.exp(-2*x)*(1+x)
mrl = sp.factor(N/S)
assert sp.simplify(mrl-(x+1)/(2*x+1)) == 0
assert sp.simplify(sp.diff(mrl,x) + 1/(2*x+1)**2) == 0
print('ERLANG2_STRICT_DMRL_PASS', mrl)

# At rho=9/10, lambda=rho because E[X]=1 and E[X^2]=3/2.
r = sp.Rational(9,10)
Lr = sp.factor(-sp.log(1-r)/r)
Qr = sp.factor(r*sp.Rational(3,2)/(2*(1-r)))
assert Qr == sp.Rational(27,4)
rc_deficit = sp.factor(Lr/2-1)
assert float(rc_deficit) > 0
print('ERLANG2_Q', Qr)
print('ERLANG2_L', Lr)
print('ERLANG2_RC_DEFICIT', rc_deficit)

# For DMRL/FCFS, S_slack=Q+(L-1)m, Xi=0, and the whole D1+D3
# reserve is free when there are no internal contacts.  The corrected
# contact-adaptive condition has margin T_G/2=(Q+m)/2.
S_slack = sp.factor(Qr + Lr - 1)
carc_margin = sp.factor(S_slack/2 - (Lr/2-1))
assert sp.simplify(carc_margin-sp.Rational(31,8)) == 0
print('ERLANG2_CONTACT_ADAPTIVE_MARGIN', carc_margin)

# Unique nonzero high-load threshold for RC failure is defined by L(rho)=2.
# We only archive a numerical locator; the theorem uses the exact equation.
root = sp.nsolve(-sp.log(1-rho)-2*rho, sp.Rational(4,5))
print('RC_FAILURE_THRESHOLD_LOCATOR', sp.N(root, 30))
print('ALL_SYMBOLIC_CHECKS_PASS')
