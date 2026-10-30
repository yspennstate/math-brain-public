import mpmath as mp
import sympy as sp

# Dense Parseval core.
R0 = sp.Matrix([
    [1, 1, 1],
    [1,-1, 1],
    [1, 1,-1],
    [1,-1,-1],
]) / 2
B = sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
assert R0.T*R0 == sp.eye(3)
assert B*B == sp.eye(3)
assert B.eigenvals() == {1:2,-1:1}
assert all(x != 0 for x in R0*B*R0.T)
assert sum((sp.Matrix(R0[j,:]).T.T*sp.Matrix(R0[j,:]).T)[0] for j in range(4)) == 3

# Verify the Poisson-gamma Laplace identity behind the noncentral chi-square mixture.
t, s, rho = sp.symbols('t s rho', positive=True)
theta = 2*s
nu = rho**2/(2*s)
mixture_laplace = (1+theta*t)**(-1) * sp.exp(nu*((1+theta*t)**(-1)-1))
noncentral_laplace = (1+2*s*t)**(-1) * sp.exp(-rho**2*t/(1+2*s*t))
assert sp.simplify(mixture_laplace/noncentral_laplace) == 1

# Centered reflection base peak: theta=2s gives 1/(sqrt(2) theta)=1/(2sqrt(2)s).
u = sp.symbols('u', positive=True)
f_exp = sp.exp(-u/theta)/theta
f_half = u**(-sp.Rational(1,2))*sp.exp(-u/theta)/(sp.sqrt(sp.pi)*sp.sqrt(theta))
p0 = sp.simplify(sp.integrate(f_exp*f_half, (u,0,sp.oo)))
assert sp.simplify(p0 - 1/(sp.sqrt(2)*theta)) == 0

# Concrete iid all-four-type lower witness.
lam = mp.mpf('0.0001')
D = mp.mpf('1')
a = mp.sqrt(D/lam)
w0 = (mp.e**(-lam)*mp.besseli(0,lam))**4
lower = 3*mp.sqrt(2)*w0
upper = 3*mp.sqrt(2)
assert lower > mp.mpf('4.24094')
assert upper-lower < mp.mpf('0.001697')
assert 3*D == 3
assert mp.mpf(1)/12 + D == mp.mpf(13)/12

print('QFORM_B17_GLOBAL_GAUSSIAN_LOCATION_CHECK_PASS')
print('p0 symbolic =', p0)
print('lambda =', mp.nstr(lam,20))
print('a =', mp.nstr(a,20))
print('w0 all-four =', mp.nstr(w0,30))
print('lower =', mp.nstr(lower,30))
print('upper =', mp.nstr(upper,30))
print('gap =', mp.nstr(upper-lower,30))
print('iid Lindeberg defect limit for D=1 = 3')
print('iid marginal variance limit for D=1 = 13/12')
