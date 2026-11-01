from sympy import symbols, sqrt, simplify, limit, Rational

# Exact algebra for the scalar critical-feedback extremizer.
# We parameterize s = sqrt(2/(p-1)) and assume 0 <= beta < s.
s, beta, p = symbols('s beta p', positive=True)
q = 2/s**2                 # q = p-1
alpha = s - beta
delta = 1 - beta**2/s**2   # 1 - beta^2(p-1)/2 after q=2/s^2
R = 1/alpha

# Scalar Ito upper-bound quadratic:
# delta R^2 <= (p-1) beta R + (p-1)/2.
# At the proposed sharp constant R=1/alpha, equality must hold.
root_residual = simplify(delta*R**2 - q*beta*R - q/2)
assert root_residual == 0

# Critical feedback beta+alpha=s makes the p-moment Lyapunov exponent zero.
lyap = simplify((q+1)/2 * ((beta+alpha)**2*q - 2))
assert lyap == 0

# Bellman upper constant squared, rewritten using q=2/s^2, is (p/2) times R^2.
# Original C_B^2 = p(p-1) / (2 (sqrt(2)-beta sqrt(p-1))^2).
# Since sqrt(p-1)=sqrt(2)/s, this becomes p/(2(s-beta)^2).
Cb2_rewritten = p/(2*(s-beta)**2)
assert simplify(Cb2_rewritten / R**2 - p/2) == 0

# Frozen beta=1 rationalization. Put t=sqrt(p-1), so s=sqrt(2)/t.
t = symbols('t', positive=True)
R_frozen_t = simplify(1/(sqrt(2)/t - 1))
R_frozen_rationalized_t = simplify(t*(sqrt(2)+t)/(2-t**2))
assert simplify(R_frozen_t - R_frozen_rationalized_t) == 0

# Representative exact subcritical point p=5/2, beta=1.
p0 = Rational(5,2)
t0 = sqrt(p0-1)
R0 = simplify(t0/(sqrt(2)-t0))
R0_alt = simplify(((p0-1)+sqrt(2*(p0-1)))/(3-p0))
assert simplify(R0-R0_alt) == 0

# Frozen near-critical asymptotic: (3-p) C_sc(p) -> 4.
pvar = symbols('pvar', positive=True)
Csc = 1/(sqrt(2/(pvar-1))-1)
limval = limit((3-pvar)*Csc, pvar, 3, dir='-')
assert limval == 4

print('root_residual =', root_residual)
print('critical_feedback_lyapunov =', lyap)
print('Bellman_upper_squared / scalar_sharp_squared = p/2')
print('frozen_p_5/2_Csc =', R0)
print('lim_(p->3-) (3-p) Csc(p) =', limval)
# C27 peer-audit constant arithmetic for C27-MACROSCOPIC-FRESH-PREFIX-03.
from fractions import Fraction
assert Fraction(8,128) == Fraction(1,16)
assert Fraction(1,8) + Fraction(1,1024) < Fraction(1,4)
assert 1 - Fraction(1,8) - Fraction(1,1024) > Fraction(3,4)
print('C27: 8/128 = 1/16 and 1-1/8-1/1024 > 3/4')
print('ALL_EXACT_CHECKS_PASS')
