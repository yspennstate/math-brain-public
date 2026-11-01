import sympy as sp

# Superseding executed checker for P0434 / P01-A DMRL-collapse and RC obstruction.
rho = sp.symbols('rho', positive=True)
Q = sp.symbols('Q', positive=True)
s = 1-rho
sqrt_s = sp.sqrt(s)
c = sp.factor(2/(1+sqrt_s))
L = -sp.log(1-rho)/rho

Omega = sp.factor(Q*(s + s/s - 2*sqrt_s)/(1-s))
assert sp.simplify(Omega-(c-1)*Q) == 0
print('WHOLE_VALLEY_WAITING_CREDIT_IDENTITY_PASS')

rc_lhs_minus_rhs = sp.simplify((c-1)*Q - ((c-1)*Q + (L/2-1)))
assert sp.simplify(rc_lhs_minus_rhs - (1-L/2)) == 0
print('RC_GAP_IDENTITY_PASS', rc_lhs_minus_rhs)

x = sp.symbols('x', nonnegative=True)
S = sp.exp(-2*x)*(1+2*x)
N = sp.exp(-2*x)*(1+x)
mrl = sp.factor(N/S)
assert sp.simplify(mrl-(x+1)/(2*x+1)) == 0
assert sp.simplify(sp.diff(mrl,x) + 1/(2*x+1)**2) == 0
print('ERLANG2_STRICT_DMRL_PASS', mrl)

r = sp.Rational(9,10)
Lr = sp.factor(-sp.log(1-r)/r)
Qr = sp.factor(r*sp.Rational(3,2)/(2*(1-r)))
assert Qr == sp.Rational(27,4)
rc_deficit = sp.factor(Lr/2-1)
assert float(rc_deficit) > 0
print('ERLANG2_Q', Qr)
print('ERLANG2_L', Lr)
print('ERLANG2_RC_DEFICIT', rc_deficit)

S_slack = sp.factor(Qr + Lr - 1)
carc_margin = sp.factor(S_slack/2 - (Lr/2-1))
assert sp.simplify(carc_margin-sp.Rational(31,8)) == 0
print('ERLANG2_CONTACT_ADAPTIVE_MARGIN', carc_margin)

root = sp.nsolve(-sp.log(1-rho)-2*rho, sp.Rational(4,5), prec=80)
print('RC_FAILURE_THRESHOLD_LOCATOR', sp.N(sp.re(root), 40))
print('ALL_SYMBOLIC_CHECKS_PASS')
