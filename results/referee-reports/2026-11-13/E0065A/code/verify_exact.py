"""Exact symbolic audits; no numerical solver is used as a certificate."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
from pathlib import Path
import json, sympy as S
x,a,b,c,l,t,m,d,z=S.symbols('x a b c l t m d z',real=True)
A=a-2*b+c; B=2*(b-c);C=c
f=A*x*x+B*x+C
H=A*A*x*x+A*(B+1)*x+A*C+B+1
checks={}
checks['binary_factorization']=S.expand(f.subs(x,f)-x-(f-x)*H)==0
D=(B-1)**2-4*A*C
checks['binary_D']=S.expand(D-((2*b-1)**2+4*c*(1-a)))==0
checks['binary_bound']=S.expand(D.subs({a:l,b:l,c:1-l})-(5-12*l+8*l*l))==0
binary=(3-S.sqrt(7))/4
checks['binary_threshold']=S.simplify((5-12*l+8*l*l).subs(l,binary)-4)==0
z0=1/t-1;s0=2-1/t
Dcycle=S.factor(s0*s0-4*l/t)
checks['cycle_discriminant']=S.simplify(Dcycle.subs(l,(1-t)/m)-((m+1)*(2*t-1)**2-1)/(m*t*t))==0
lm=(1-1/S.sqrt(m+1))/(2*m)
checks['general_critical']=S.simplify(Dcycle.subs(t,1-m*l).subs(l,lm))==0
up_l1=1/(m+1+S.sqrt(m*m+1))
up=2/(3*m+2+S.sqrt(m*m+12*m+4))
checks['upper_l1_critical']=S.simplify(2*(1-m*up_l1)*(1-up_l1)-1)==0
checks['upper_fisher_critical']=S.simplify(2*(1-m*up)**2-(1-m*up)-2*up)==0

certs=[]
for dim,lam in [(3,S.Rational(2,25)),(4,S.Rational(11,160))]:
 T=1-dim*lam; Z=1/T-1; SD=2-1/T; delta=S.sqrt(SD**2-4*lam/T)
 u=(SD+delta)/2;v=(SD-delta)/2
 xx=[u,Z-(dim-3)*lam,v]+[lam]*(dim-3)
 yy=[v,Z-(dim-3)*lam,u]+[lam]*(dim-3)
 pairs=[(i,j) for i in range(dim) for j in range(i,dim)]
 PP=[]
 for i,j in pairs:
  if (i==0 and j==2): k=1
  elif i==0 or j==0: k=2
  elif i==2 or j==2: k=0
  else:k=1
  PP.append([lam+T*int(k==r) for r in range(dim)])
 def V(w):return [S.expand(sum((1 if i==j else 2)*PP[r][k]*w[i]*w[j] for r,(i,j) in enumerate(pairs))) for k in range(dim)]
 assert all(S.simplify(i-j)==0 for i,j in zip(V(xx),yy))
 assert all(S.simplify(i-j)==0 for i,j in zip(V(yy),xx))
 assert S.simplify(sum(xx)-1)==0
 assert all(q.is_positive for q in xx)
 b2=S.factor(T*T*delta*delta); aa=3-4*T
 tr=S.factor(1+aa**2-2*b2);det=S.factor((aa+b2)**2)
 jury=[S.factor(1-tr+det),S.factor(1+tr+det),S.factor(1-det)]
 assert all(q>0 for q in jury)
 certs.append({'m':dim,'lambda':str(lam),'t':str(T),'x':[str(S.simplify(q)) for q in xx],'y':[str(S.simplify(q)) for q in yy],'P':[[str(q) for q in row] for row in PP],'pairs':pairs,'two_cycle_trace':str(tr),'two_cycle_det':str(det),'jury_positive':[str(q) for q in jury]})

# Numerical table is presentation only, derived from the exact formulas.
table=[]
for dim in [3,4,5,10,100,1000]:
 low=lm.subs(m,dim);hi=up.subs(m,dim)
 table.append({'m':dim,'lower_exact':str(low),'lower':float(low),'upper_exact':str(hi),'upper':float(hi),'old_upper':1/(2*dim)})
assert all(checks.values()),checks
result={'checks':checks,'binary_threshold_exact':str(binary),'binary_threshold':float(binary),'certificates':certs,'bounds_table':table}
Path('data/exact_verification.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
