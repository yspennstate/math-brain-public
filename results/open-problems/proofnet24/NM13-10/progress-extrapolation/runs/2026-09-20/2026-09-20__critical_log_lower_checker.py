#!/usr/bin/env python3
import sympy as sp
from mpmath import mp

g, t, ts, s2 = sp.symbols("g t ts s2", positive=True)
sigma2 = (1+g)**2
q = sp.expand(sigma2 - 1)
d = 1 + sigma2/2
kappa = sp.simplify(2*d/sigma2)
a = sp.simplify(1-kappa/3)
ad = sp.simplify(a*d)

assert sp.simplify(a - 2*q/(3*sigma2)) == 0
assert sp.simplify(q-ad - 2*q**2/(3*sigma2)) == 0

sigma, dd = sp.symbols("sigma dd", positive=True)
x = dd*ts
E = (x+dd*t)**2/(2*sigma**2*t)
kap = 2*dd/sigma**2
assert sp.simplify(E-kap*x - dd**2*(t-ts)**2/(2*sigma**2*t)) == 0

L = sp.log(1/g)/(2*g)
assert sp.simplify(q*L + (g+2)*sp.log(g)/2) == 0
assert sp.limit(ad/(2*g), g, 0, dir="+") == 1
assert sp.limit(q**2*L, g, 0, dir="+") == 0
assert sp.limit(q*sp.sqrt(L), g, 0, dir="+") == 0

print("SYMBOLIC_IDENTITIES_PASS")
print("a =", sp.factor(a))
print("q-ad =", sp.factor(q-ad))
print("Gaussian exponent defect =", sp.factor(E-kap*x))
print("lim ad/(2g) =", sp.limit(ad/(2*g), g, 0, dir="+"))
print("lim q^2 L =", sp.limit(q**2*L, g, 0, dir="+"))
print("lim q sqrt(L) =", sp.limit(q*sp.sqrt(L), g, 0, dir="+"))

mp.dps = 50
def proxy(gv, alpha):
    sigma2v=(1+gv)**2
    qv=sigma2v-1
    dv=1+sigma2v/2
    kappav=2*dv/sigma2v
    av=1-kappav/3
    Lv=mp.log(1/gv)/(2*gv)
    xv=dv*(Lv-2*mp.sqrt(Lv))
    inp=gv*((mp.e**(3*qv*Lv)-1)/(3*qv))**(mp.mpf(1)/3)
    out=mp.e**(av*xv)/(Lv**alpha)
    return Lv, kappav, out/inp

for alpha in [mp.mpf("0.5"), mp.mpf("0.6"), mp.mpf(2)/3, mp.mpf("0.75")]:
    vals=[]
    for gv in [mp.mpf("1e-3"), mp.mpf("1e-4"), mp.mpf("1e-5")]:
        Lv, kv, rv=proxy(gv, alpha)
        vals.append((gv, rv))
    print("alpha", mp.nstr(alpha,12), "proxy ratios",
          [(mp.nstr(gv,4), mp.nstr(rv,14)) for gv,rv in vals])
print("CHECK_PASS")
