"""OPEN: pendant subface with zero neighbor y-coordinate."""
import sympy as s
from zero_face import construct
rr,t,V,R,M,de,Q,N,D,ed,Pi,C=construct()
tt,y1,y2=s.symbols('t y1 y2')
p=s.Poly(s.expand(C.as_expr().subs(dict(zip(rr.symbols,(tt,-1,y1,-1,y2,-y1-y2))))/80),y1,y2)
# Symmetric zero-sum triple: K=2(y1^2+y1 y2+y2^2), J=-3y1 y2(y1+y2).
K,J=s.symbols('K J')
kk=2*(y1*y1+y1*y2+y2*y2); jj=-3*y1*y2*(y1+y2)
A=s.factor(p.coeff_monomial(y1**2)/2)
B=s.factor(p.coeff_monomial(y1**4)/4)
E=s.factor(p.coeff_monomial(y1**6)/8)
F=12*(tt*tt-3*tt+6)
assert s.expand(p.as_expr()-(K*(A+B*K+E*K*K)+F*J*J).subs({K:kk,J:jj}))==0
print('A=',s.factor(A),'B=',s.factor(B),'E=',s.factor(E))
print('Kmax=',s.factor(A+3*(tt+1)*B+9*(tt+1)**2*E))
for po in [A,A+3*(tt+1)*B+9*(tt+1)**2*E]:
 print('at1.5',po.subs(tt,s.Rational(3,2)),'at4',po.subs(tt,4))
v,h=s.symbols('v h')
P=s.expand(A*(1+v)**2*(3+v*v)+B*(tt+1)*h*(1+v)*(3+v*v)**2+E*(tt+1)**2*h*h*(3+v*v)**3+s.Rational(9,2)*F*(tt+1)**2*h*h*(1-v*v)**2)
print('h2factor',s.factor(P.coeff(h,2)))
print('h1factor',s.factor(P.subs(h,1)))
print('t1.5',s.factor(P.subs({h:1,tt:s.Rational(3,2)})))
print('t4',s.factor(P.subs({h:1,tt:4})))
import numpy as np
f=s.lambdify((tt,v,h),P,'numpy',cse=True)
rng=np.random.default_rng(32)
vals=f(rng.uniform(1.5,4,100000),rng.uniform(0,1,100000),rng.uniform(0,1,100000))
print('NUMERICAL: P minimum',vals.min(),'negative',(vals<0).sum())
# Bernstein coefficients in t on [3/2,4] and v on [0,1].
x=s.symbols('x')
for name,expr in [('A',A),('minus_h2',-P.coeff(h,2)),('h1',P.subs(h,1))]:
 ex=s.Poly(s.expand(expr.subs(tt,(3+5*x)/2)),x,v)
 nx,nv=ex.degree_list(); coeffs=[]
 from math import comb
 for i in range(nx+1):
  for j in range(nv+1):
   val=sum(c*s.Rational(comb(i,m[0]),comb(nx,m[0]))*s.Rational(comb(j,m[1]),comb(nv,m[1])) for m,c in ex.terms()if m[0]<=i and m[1]<=j)
   coeffs.append(val)
 print('Bernstein',name,(nx,nv),'min',min(coeffs),'negative',sum(1 for c in coeffs if c<0))
