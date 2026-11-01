import math
import random
import sympy as sp
import numpy as np

x,a,b,s,p = sp.symbols("x a b s p", real=True)
phi = 282*x**5 - 265*x**4 + 30*x**3 - 240*x**2 + 193*x

# 1. G3 decomposition.
S2,S3,S4,S5 = sp.symbols("S2 S3 S4 S5", real=True)
D2,D3,D4,D5 = 3-S2,3-S3,3-S4,3-S5
G = sp.expand(30*D2*(3-D3)+240*D2-30*D3+265*D4-282*D5)
sumphi = sp.expand(579-240*S2+30*S3-265*S4+282*S5)
assert sp.expand(G - (sumphi + 30*(3-S2)*S3)) == 0

# 2. Pair-merging factorization.
phia = phi.subs(x,a)
phib = phi.subs(x,b)
phis = phi.subs(x,a+b)
diff = sp.factor(phia+phib-phis)
B_ab = sp.factor(-diff/(10*a*b))
B_target = 141*(a+b)**3 -106*(a+b)**2 + 9*(a+b)-48 + (53-141*(a+b))*a*b
assert sp.expand(B_ab-B_target) == 0

# 3. n=4 Newton reduction.
y = sp.symbols("y0:4", nonnegative=True)
expr4 = sp.expand(sum(phi.subs(x,1-z) for z in y))
y0,y1,y2,y3=y
e2 = sum(y[i]*y[j] for i in range(4) for j in range(i+1,4))
e3 = sum(y[i]*y[j]*y[k] for i in range(4) for j in range(i+1,4) for k in range(j+1,4))
e4 = sp.prod(y)
target4 = 10*(88*e2**2 + (141*e2-220)*e3 + 4*e2 -317*e4)
expr4_sub = sp.expand(expr4.subs(y3,1-y0-y1-y2))
target4_sub = sp.expand(target4.subs(y3,1-y0-y1-y2))
assert sp.expand(expr4_sub-target4_sub) == 0

# 4. Bernstein coefficients for P(x)=phi+100x-60 on [1/3,1].
t=sp.symbols("t", real=True)
P = sp.expand((phi+100*x-60).subs(x,sp.Rational(1,3)+sp.Rational(2,3)*t))
coeffs = sp.symbols("c0:6")
bern = sum(coeffs[k]*sp.binomial(5,k)*t**k*(1-t)**(5-k) for k in range(6))
sol = sp.solve(sp.Poly(sp.expand(bern-P),t).coeffs(), coeffs, dict=True)[0]
expected = [
    sp.Rational(10),
    sp.Rational(10592,405),
    sp.Rational(4018,135),
    sp.Rational(308,15),
    sp.Rational(94,15),
    sp.Rational(40),
]
assert [sp.simplify(sol[c]-e) for c,e in zip(coeffs,expected)] == [0]*6
assert all(e>0 for e in expected)

# 5. Random capped-simplex sanity bank.
def project_capped_sum3(v):
    # Euclidean projection by bisection on lambda: clip(v+lambda,0,1), sum=3.
    lo,hi=-5.0,5.0
    for _ in range(100):
        mid=(lo+hi)/2
        w=np.clip(v+mid,0.0,1.0)
        if w.sum() < 3.0:
            lo=mid
        else:
            hi=mid
    return np.clip(v+(lo+hi)/2,0.0,1.0)

def phi_num(z):
    return 282*z**5-265*z**4+30*z**3-240*z**2+193*z

worst_phi=1e99
worst_G=1e99
rng=np.random.default_rng(16092026)
for n in range(3,31):
    for _ in range(2000):
        d=project_capped_sum3(rng.normal(size=n))
        H=float(np.sum(phi_num(d)))
        s2=float(np.sum(d**2)); s3=float(np.sum(d**3))
        Gv=H+30*(3-s2)*s3
        worst_phi=min(worst_phi,H)
        worst_G=min(worst_G,Gv)
        assert H >= -1e-8
        assert Gv >= -1e-8

print("symbolic identities: PASS")
print("pair-merging factorization: PASS")
print("n=4 Newton reduction: PASS")
print("n=5 Bernstein certificate: PASS")
print(f"random capped-simplex bank: PASS; worst sum_phi={worst_phi:.12g}; worst G3={worst_G:.12g}")
