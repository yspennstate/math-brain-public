# T357, agent A 20 Oct 11:3x. Proof check: D(beta) > 0 for every beta > 0 via the normal scale mixture of the logistic
# (Stefanski 1991: logistic = N(0, (2K)^2), K Kolmogorov). sig'(x) = int N(x; 0, sigma^2) dF(sigma), sigma = 2K.
# With a = beta^2/sigma^2 and c = 1 + a, Gaussian integrals against phi(u):
#   E[exp(-a u^2/2)] = c^-1/2, E[u^2 exp(-a u^2/2)] = c^-3/2, E[|u| exp(-a u^2/2)] = 2 phi0 c^-1.
# D > 0  <=>  2 phi0 s0 E[u^2 s] > E[s] E[|u| s]  <=>  E_P[X^3] > E_P[X] E_P[X^2], X = c^-1/2 in (0,1), P prop. to dF(sigma)/sigma,
# which is Chebyshev's sum inequality (X and X^2 both increasing in X), strict unless X is constant.
import mpmath as mp
mp.mp.dps = 25
phi0 = 1/mp.sqrt(2*mp.pi)
def kdens(x):  # Kolmogorov density
    if x < mp.mpf('0.3'):  # small-x form: P(K<=x) = sqrt(2pi)/x sum exp(-(2k-1)^2 pi^2/(8x^2))
        F = lambda y: mp.sqrt(2*mp.pi)/y*mp.nsum(lambda k: mp.exp(-(2*k-1)**2*mp.pi**2/(8*y*y)), [1, mp.inf])
        return mp.diff(F, x)
    return 8*x*mp.nsum(lambda k: (-1)**(k-1)*k*k*mp.exp(-2*k*k*x*x), [1, mp.inf])
def s1(x): e = mp.exp(-abs(x)); return e/(1+e)**2
# sanity: mixture reproduces sig'(x)
for x in [0, 0.5, 2, 5]:
    mix = mp.quad(lambda k: kdens(k)*mp.exp(-x*x/(8*k*k))/(2*k*mp.sqrt(2*mp.pi)), [0, 0.3, 1, 3, mp.inf])
    print('sig\'(%g): direct %s  mixture %s' % (x, mp.nstr(s1(x), 15), mp.nstr(mix, 15)))
phi = lambda u: mp.exp(-u*u/2)*phi0
for b in [0.5, 2, 10]:
    b = mp.mpf(b)
    d = lambda f: 2*mp.quad(lambda u: f(u)*phi(u), [0, 1/b, 1, 4, mp.inf])
    direct = [d(lambda u: s1(b*u)), d(lambda u: u*u*s1(b*u)), d(lambda u: u*s1(b*u))]
    w = lambda k: kdens(k)/(2*k*mp.sqrt(2*mp.pi))
    m = lambda g: mp.quad(lambda k: w(k)*g(1 + b*b/(4*k*k)), [0, 0.3, 1, 3, mp.inf])
    s0 = m(lambda c: 1)
    mix = [m(lambda c: c**-0.5), m(lambda c: c**-1.5), 2*phi0*m(lambda c: 1/c)]
    EX, EX2, EX3 = [m(lambda c, p=p: c**(-p/2))/s0 for p in (1, 2, 3)]
    print('beta %s: s0 %s | E s %s/%s | E u2 s %s/%s | E|u| s %s/%s | E X^3 - E X E X^2 = %s' % (
        mp.nstr(b, 3), mp.nstr(s0, 12), mp.nstr(direct[0], 12), mp.nstr(mix[0], 12), mp.nstr(direct[1], 12), mp.nstr(mix[1], 12),
        mp.nstr(direct[2], 12), mp.nstr(mix[2], 12), mp.nstr(EX3 - EX*EX2, 8)))
