# T357, agent A 20 Oct 11:2x. Leading order in 1/alpha: lam_OC/lam_risk > 1 for every beta > 0?
# lam_r is proportional to b - C (r - beta)/beta^2 with b > 0, C > 0 and r_FM, r_OC < 0 (sig'' is odd and negative on u > 0),
# so both lambdas are positive and the ratio exceeds 1 exactly when r_OC < r_FM, i.e. when
#   D(beta) = E[u sig''(bu)]/E[u^2 sig'(bu)] - E[sgn(u) sig''(bu)]/E[|u| sig'(bu)] > 0      (u ~ N(0,1)).
import mpmath as mp, sympy as sp
mp.mp.dps = 30
def s1(x): e = mp.exp(-abs(x)); return e/(1+e)**2
def s2(x):  # sig''(x) = sig'(x)(1 - 2 sig(x))
    sg = 1/(1+mp.exp(-x)); return s1(x)*(1-2*sg)
phi = lambda u: mp.exp(-u*u/2)/mp.sqrt(2*mp.pi)
def E(f, b):  # 2 * int_0^inf f(u) phi(u) du for even integrands
    pts = [0, mp.mpf(1)/b, mp.mpf(5)/b, mp.mpf(20)/b, 1, 3, 10, mp.inf]
    pts = sorted(set(p for p in pts if p == mp.inf or p <= 12)) if b > 0 else [0, mp.inf]
    return 2*mp.quad(lambda u: f(u)*phi(u), pts)
def D(b):
    fm = E(lambda u: u*s2(b*u), b)/E(lambda u: u*u*s1(b*u), b)
    oc = E(lambda u: s2(b*u), b)/E(lambda u: u*s1(b*u), b)
    return fm - oc, fm, oc
out = []
# small-beta series: moments E u^(2k) = (2k-1)!!, E|u|^(2k+1) = 2^k k! sqrt(2/pi)
x, bb = sp.symbols('x beta', positive=True)
sig = 1/(1+sp.exp(-x)); d1 = sp.diff(sig, x); d2 = sp.diff(sig, x, 2)
N = 12
p1 = sp.series(d1, x, 0, N).removeO(); p2 = sp.series(d2, x, 0, N).removeO()
c = sp.sqrt(2/sp.pi)
def Eeven(k): return sp.factorial2(k-1) if k > 0 else 1   # E u^k, k even
def Eabs(k): return 2**((k-1)//2)*sp.factorial((k-1)//2)*c   # E|u|^k, k odd
def mom(poly, extra, absval):
    poly = sp.Poly(sp.expand(poly), x); tot = 0
    for (k,), co in poly.terms():
        p = k + extra
        tot += co*bb**k*(Eabs(p) if p % 2 else (Eeven(p) if not absval else Eeven(p)))
    return tot
fm = mom(p2, 1, False)/mom(p1, 2, False)
oc = mom(p2, 0, True)/mom(p1, 1, True)   # sgn(u) u^k with k odd -> |u|^k ; |u| u^k with k even -> |u|^(k+1)
ser = sp.series(sp.simplify(fm - oc), bb, 0, 9)
out.append('small-beta series of D(beta): ' + str(sp.nsimplify(ser)))
out.append('numeric coefficients: ' + str(sp.N(ser.removeO(), 8)))
out.append('%10s %22s %16s %16s %14s' % ('beta', 'D', 'FM ratio', 'OC ratio', 'D/beta^3 or D/beta'))
for b in [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1, 1.5, 2, 3, 5, 7, 10, 15, 20, 30, 50, 100, 200, 500, 1000]:
    d, f, o = D(mp.mpf(b))
    scale = d/b**3 if b < 1 else d/b
    out.append('%10g %22s %16s %16s %14s' % (b, mp.nstr(d, 12), mp.nstr(f, 10), mp.nstr(o, 10), mp.nstr(scale, 8)))
# large beta: FM ratio ~ (1/b)(-1)/(pi^2/3) * ... ; check b*D -> limit
lim = (-1/(mp.pi**2/3)) - (-mp.mpf(1)/4)/(mp.log(2))   # from int x sig'' = -1, int x^2 sig' = pi^2/3, int_0 sig'' = -1/4, int_0 x sig' = ln 2
out.append('large-beta: D/beta -> %s (closed form -3/pi^2 + 1/(4 ln 2))' % mp.nstr(lim, 12))
for b in [100, 1000]:
    out.append('  beta %d: D/beta = %s' % (b, mp.nstr(D(mp.mpf(b))[0]/b, 12)))
print('\n'.join(out))
