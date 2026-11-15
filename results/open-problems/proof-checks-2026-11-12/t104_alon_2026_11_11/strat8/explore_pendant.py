"""OPEN: symbolic investigation of the three-zero-edge (pendant) face."""
import sympy as s
from zero_face import construct
rr,t,V,R,M,de,Q,N,D,ed,Pi,C=construct()
# x1=x2=x5=-1, leaving vertex 4 adjacent only to vertex 3.
y1,y2,z,tt=s.symbols('y1 y2 z tt')
lookup=dict(zip(rr.symbols,(tt,-1,y1,-1,y2,z)))
p=s.Poly(C.as_expr().subs(lookup).expand()/80,y1,y2,z)
print('terms',len(p.terms()))
print('degree',p.total_degree())
q,rem,syms=s.symmetrize(p.as_expr(),[y1,y2,z], formal=True)
print('remainder',rem)
print('symmetric',s.factor(q))
a,b,c=[x[0]for x in syms]
# Replace elementary moments with sum s, centered squared norm k and cubic j.
S,K,J=s.symbols('S K J')
e2=S*S/3-K/2
e3=J/3+S*e2/3-2*S**3/27
form=s.Poly(s.expand(q.subs({a:S,b:e2,c:e3})),J)
for (d,),co in form.terms(): print('J degree',d,s.factor(co))
print('degree t',s.degree(q,tt))
with open('pendant_symbolic.txt','w') as f:
 f.write('OPEN: exploratory formula only; no positivity claim.\n'+str(s.factor(q))+'\n')
# Test the unconstrained minimum in J under only the spectral determinant bounds.
coef=form.all_coeffs()
mini=s.factor(4*coef[0]*coef[2]-coef[1]**2)
power=s.Poly(mini,S)
assert all(m[0]%2==0 for m,c in power.terms())
P=s.symbols('P')
mini=s.Add(*(c*P**(m[0]//2)for m,c in power.terms()))
print('Schur factor',s.factor(mini))
import numpy as np
fn=s.lambdify((tt,K,P),mini,'numpy',cse=True)
rng=np.random.default_rng(82)
ts=rng.uniform(1.5,4,10000); xs=rng.uniform(0,1,10000); ys=rng.uniform(0,1,10000)
vals=fn(ts,5*ts*(1-xs)*ys,3*(2*ts-3)*xs)
idx=int(vals.argmin());print('NUMERICAL: Schur relaxed min',vals[idx], 'at',ts[idx],xs[idx],ys[idx], 'negative count',int((vals<0).sum()))
