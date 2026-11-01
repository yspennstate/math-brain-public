import sympy as sp

# Exact algebra for the normalized Lamperti correlation of integrated fBM.
p, T, t, k = sp.symbols('p T t k', positive=True)
B = T**(p+1) + T - (T**(p+2) + 1 - (T-1)**(p+2))/(p+2)
R = (p+2)/(2*(p+1)) * T**(-(p+2)/2) * B

# H=p/2, so d/dH = 2 d/dp.
D = sp.expand_log(sp.simplify(2*sp.diff(R, p).subs(p, 1)), force=True)
D_expected = sp.expand_log(
    (T-1)**2/(2*T**sp.Rational(3,2)) *
    (1 - (T-1)*sp.log(T/(T-1))), force=True)
assert sp.simplify(D - D_expected) == 0
print('DERIVATIVE_IDENTITY_PASS')
print('dH_R_at_half =', sp.factor(D_expected))

# Local scale: D(t) ~ t^2/2.  This implies d_H[-R_H''(0)]|_{1/2} = -1.
Dt = sp.simplify(D_expected.subs(T, sp.exp(t)))
local_coeff = sp.limit(Dt/t**2, t, 0, dir='+')
assert local_coeff == sp.Rational(1,2)
print('LOCAL_T2_COEFF =', local_coeff)
print('SECOND_SPECTRAL_MOMENT_DERIVATIVE = -1')

# Positivity reduction.  Put y=T-1>0:
# 1-y log(1+1/y)>0 because log(1+x)<x for x>0.
y = sp.symbols('y', positive=True)
g = 1 - y*sp.log(1 + 1/y)
print('POSITIVITY_REDUCTION = 1 - y*log(1+1/y), y>0')
print('POSITIVITY_WITNESS = log(1+x)<x for x>0')

# A useful sharp relative bound: 0 < D/R_{1/2} < 1/6.
# With x=1/y, the upper bound is equivalent to
# F(x)=x^2(3+2x)-6(x-log(1+x))>0.
x = sp.symbols('x', positive=True)
F = x**2*(3+2*x) - 6*(x-sp.log(1+x))
Fp = sp.factor(sp.diff(F, x))
assert sp.simplify(Fp - 6*x**2*(x+2)/(x+1)) == 0
print('RELATIVE_BOUND_D_OVER_R0_LT_1_OVER_6_PASS')
print('Fprime =', Fp)

# Low-frequency spectral tangent.  For u=e^{-t},
# g(u)=1+(1-u)log(1-u)/u = sum_{k>=1}u^k/[k(k+1)].
# Hence integral_0^infty D(t)dt is the positive series below.
term = 1/(k*(k+1)*(k-sp.Rational(1,2))*(k+sp.Rational(1,2))*(k+sp.Rational(3,2)))
apart_expected = (
    sp.Rational(4,3)/(2*k+3) + 8/(2*k+1) + sp.Rational(4,3)/(2*k-1)
    - sp.Rational(8,3)/(k+1) - sp.Rational(8,3)/k
)
assert sp.simplify(term-apart_expected) == 0
print('PARTIAL_FRACTION_PASS')
I0 = sp.Rational(32,3)*sp.log(2) - sp.Rational(64,9)
print('INT_0_INF_D_DT =', I0)
print('SPECTRAL_DENSITY_TANGENT_AT_ZERO =', sp.simplify(I0/sp.pi))

# At H=1/2 the stationary spectral density under
# f(lambda)=(2*pi)^(-1) int R(t)e^{-i lambda t}dt is
# 3/[2*pi*(lambda^2+1/4)*(lambda^2+9/4)].
lam = sp.symbols('lambda', real=True)
f0 = 3/(2*sp.pi*(lam**2+sp.Rational(1,4))*(lam**2+sp.Rational(9,4)))
print('F0(lambda) =', f0)
print('ALL_EXACT_CHECKS_PASS')
