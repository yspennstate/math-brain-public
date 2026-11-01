"""Exact identity checks for X083; finite samples are illustrative only."""
import json
import math
from pathlib import Path
import sympy as sp
import numpy as np

checks = 0
def exact(expr):
    global checks
    assert sp.simplify(expr) == 0, expr
    checks += 1

r, s = sp.symbols('r s', real=True)
a, b, c = 1-r*r, 1-s*s, 1-r*r*s*s
lp, lm = sp.symbols('lp lm', real=True)
R, kr = (lp-lm)/2, -(lp+lm)/2
vplus, vminus = sp.Matrix([1,1+r]), sp.Matrix([1,1-r])
v = (lp*vplus-lm*vminus)/2
exact(v[0]-R)
exact(v[1]-(R-r*kr))
for x in (sp.Rational(1,2)*(lp**2*vplus*vplus.T+lm**2*vminus*vminus.T)-v*v.T-(lp*vplus+lm*vminus)*(lp*vplus+lm*vminus).T/4):
    exact(x)
G = r*r*(vplus*vplus.T/(1+r)+vminus*vminus.T/(1-r))/2
for x in G-r*r*sp.Matrix([[1/a,1],[1,1]]):
    exact(x)

U11, U22 = 2*(2*c-b)/(a*c), 2*(2*c-a)/(b*c)
exact(U11-(2/a+2*s*s/c))
exact(U22-(2/b+2*r*r/c))
exact((U11-2/a)-2*s*s/c)
exact((U22-(2+2*r*r))-(2*(1/b-1)+2*r*r*(1/c-1)))
exact((2/c-2)-2*r*r*s*s/c)

x,y=sp.symbols('x y', real=True)
W=sp.Matrix([[(2-x)/(1-x),2-x-y],[2-x-y,2+x]])
expr=W.det().subs(x,1-sp.exp(-y))
exact(expr-(3*sp.exp(y)+2-sp.exp(-y)-(1+sp.exp(-y)-y)**2))
assert 1+sp.Rational(128,125)**2 < sp.Rational(9,4)
checks += 1
E = lambda q: 4*q/(1-q)+(5*q+q*q/2)/(1-q)**2
exact(E(sp.Rational(1,25))-sp.Rational(443,1152))
exact(sp.Rational(1,2)-sp.Rational(443,1152)-sp.Rational(133,1152))
assert sp.Rational(133,1152) > sp.Rational(1,10)
checks += 1

samples=[]
for rv,sv in [(0.6,0.2),(0.8,0.1),(0.99,0.2),(1-1e-9,0.2)]:
    av,bv,cv=1-rv*rv,1-sv*sv,1-rv*rv*sv*sv
    Rv,Sv,Pv=map(math.atanh,[rv,sv,rv*sv])
    kv=math.log(cv/(av*bv))/2
    U=np.array([[2/av+2*sv*sv/cv,2/cv-2*kv],[2/cv-2*kv,2/bv+2*rv*rv/cv]])
    T=np.array([[Rv+sv*Pv,Sv-sv*kv],[Rv-rv*kv,Sv+rv*Pv]])
    scale=np.diag([math.sqrt(av),1.])
    N=scale@(U-T@T.T)@scale
    samples.append({'r':rv,'s':sv,'normalized_min_eigenvalue':float(np.linalg.eigvalsh(N)[0])})

out={'exact_assertions':checks,'status':'PASS','proved_margin':'133/1152',
     'domain':'3/5 <= r < 1, 0 <= s <= 1/5, or pair exchange',
     'illustrative_samples_not_proof':samples}
Path('computations/X083/results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
