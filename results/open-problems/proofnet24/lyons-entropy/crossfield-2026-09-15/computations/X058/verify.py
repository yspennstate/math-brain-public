"""Exact determinant/current checks; decimals are diagnostics, not proof inputs."""
from itertools import product
import json
import sympy as S
import mpmath as mp
from pathlib import Path
mp.mp.dps=70
R=S.Rational; I=S.I
D=S.Matrix([[R(2,5),R(1,10)+I/20],[R(1,10)-I/20,R(3,5)]])
u=S.Matrix([1,R(1,2)]); U=u*u.conjugate().T
p0=[R(1,5),R(2,5),R(4,5)]; p1=[R(2,5),R(3,5),R(3,5)]
z0=S.Matrix([(2+I)/20,(1+2*I)/20,(1-I)/20])
z1=S.Matrix([(1+I)/20,(3+I)/20,(2-I)/20])
t=S.symbols('t',real=True)
p=[p0[i]+t*(p1[i]-p0[i]) for i in range(3)]
z=z0+t*(z1-z0); strength=[S.expand(z[i]*S.conjugate(z[i])) for i in range(3)]
K=S.diag(*p).row_join(z*u.T).col_join((u*z.conjugate().T).row_join(D))
K0=K.subs(t,0); A=K.diff(t)
checks=0
def eq(x,y):
 global checks
 assert S.simplify(x-y)==0,(x,y)
 checks+=1
def pos(x):
 global checks
 assert x>0,x
 checks+=1
av=(u.T*D.inv()*u)[0].simplify(); bv=(u.T*(S.eye(2)-D).inv()*u)[0].simplify(); c=max(av,bv)
eq(av,R(240,91));eq(bv,R(20,7))
reservoir={}
v=S.symbols('v',real=True)
for y in product([0,1],repeat=2):
 Q=D-S.diag(*[1-j for j in y]); d=S.simplify((-1)**(2-sum(y))*Q.det())
 a=S.diff((-1)**(2-sum(y))*(Q+v*U).det(),v).subs(v,0).simplify()
 reservoir[y]=(d,a);pos(d)
eq(sum(d for d,a in reservoir.values()),1);eq(sum(a for d,a in reservoir.values()),0)
J=S.simplify(sum(a*a/d for d,a in reservoir.values()));pos(J)
polys={};jets={}
for x in product([0,1],repeat=3):
 mu=[p[i] if x[i] else 1-p[i] for i in range(3)]
 for y,(d,a) in reservoir.items():
  bits=x+y
  sam=S.expand(d*S.prod(mu)-a*sum(strength[i]*(2*x[i]-1)*S.prod(mu[j] for j in range(3) if j!=i) for i in range(3)))
  Q=K-S.diag(*[1-j for j in bits]); direct=S.expand((-1)**(5-sum(bits))*Q.det(method='domain-ge'))
  eq(sam,direct);eq(S.diff(sam,t),S.diff(direct,t));eq(S.diff(sam,t,2),S.diff(direct,t,2))
  pos(sam.subs(t,0));pos(sam.subs(t,1))
  polys[bits]=sam
  Q0=Q.subs(t,0);inv=Q0.inv();mass=sam.subs(t,0)
  jets[bits]=(mass,inv)
eq(sum(polys.values()),1)
margins=[]
for pa,za in [(p0,z0),(p1,z1)]:
 ss=[S.expand(za[i]*S.conjugate(za[i])) for i in range(3)]
 AA=S.simplify(sum(ss[i]/pa[i] for i in range(3)));BB=S.simplify(sum(ss[i]/(1-pa[i]) for i in range(3)))
 pos(R(2,5)-c*AA);pos(R(2,5)-c*BB);margins.append([str(c*AA),str(c*BB)])
# Exact inertia by a diagonal-block congruence.
alphas=[p1[i]-p0[i] for i in range(3)];etas=z1-z0
schur=S.simplify((etas.conjugate().T*S.diag(*alphas).inv()*etas)[0])
eq(schur,R(1,16));eq(A.rank(),4)
# Whole Hermitian parameter tangent space at the reference point.
basis=[]
for j in range(3):
 B=S.zeros(5);B[j,j]=1;basis.append(B)
for j in range(3):
 for eta in [1,I]:
  zz=S.zeros(3,1);zz[j]=eta
  basis.append(S.zeros(3).row_join(zz*u.T).col_join((u*zz.conjugate().T).row_join(S.zeros(2))))
dirs=basis+[basis[i]+basis[j] for i in range(9) for j in range(i+1,9)]
curvs=[]
# Derive sampler jets by the product rule, preserving p'', cross histories and s''.
for B in dirs:
 alpha=[B[i,i] for i in range(3)]; eta=[B[i,3] for i in range(3)]
 sts=[S.expand(z0[i]*S.conjugate(z0[i])) for i in range(3)]
 sig=[S.simplify(2*S.re(S.conjugate(z0[i])*eta[i])) for i in range(3)]
 acc=[2*S.expand(eta[i]*S.conjugate(eta[i])) for i in range(3)]
 curvature=mp.mpf('0')
 for bits,(mass,inv) in jets.items():
  x=bits[:3]; y=bits[3:];d,a=reservoir[y]
  hist=[p0[i] if x[i] else 1-p0[i] for i in range(3)]
  dh=[alpha[i]*(2*x[i]-1) for i in range(3)]
  hist1=sum(dh[i]*S.prod(hist[j] for j in range(3) if j!=i) for i in range(3))
  hist2=2*sum(dh[i]*dh[j]*hist[3-i-j] for i in range(3) for j in range(i+1,3))
  sm1=d*hist1;sm2=d*hist2
  for i in range(3):
   rem=[j for j in range(3) if j!=i];j,k=rem
   h=hist[j]*hist[k];h1=dh[j]*hist[k]+hist[j]*dh[k];h2=2*dh[j]*dh[k]
   sm1-=a*(2*x[i]-1)*(sig[i]*h+sts[i]*h1)
   sm2-=a*(2*x[i]-1)*(acc[i]*h+2*sig[i]*h1+sts[i]*h2)
  rr=inv*B;pr=mass*S.trace(rr);ppr=mass*(S.trace(rr)**2-S.trace(rr*rr))
  eq(sm1,pr);eq(sm2,ppr)
  mm=mp.mpf(str(mass));d1=mp.mpf(str(S.simplify(sm1)));d2=mp.mpf(str(S.simplify(sm2)))
  curvature+=d1*d1/mm+d2*mp.log(mm)
 curvs.append(curvature)
M=mp.matrix(9)
for i in range(9):M[i,i]=curvs[i]
k=9
for i in range(9):
 for j in range(i+1,9):M[i,j]=M[j,i]=(curvs[k]-curvs[i]-curvs[j])/2;k+=1
# Independent affine-current identities for polynomial test functions.
pp=[R(1,5),R(7,10)];tt=[R(1,40),R(1,25)];aa=[R(1,7),-R(1,9)];ss=[-R(1,50),R(1,30)]
r0,r1=S.symbols('r0 r1',real=True);vv,ww=S.symbols('v w',real=True)
lo=[-tt[i]/(1-pp[i]) for i in range(2)];hi=[tt[i]/pp[i] for i in range(2)]
for degree in range(2,8):
 ex=0
 for x in product([0,1],repeat=2):
  ps=[pp[i]+[r0,r1][i]*aa[i] for i in range(2)]
  ts=[tt[i]+[r0,r1][i]*ss[i] for i in range(2)]
  mu=S.prod(ps[i] if x[i] else 1-ps[i] for i in range(2))
  yy=sum(ts[i]/ps[i] if x[i] else -ts[i]/(1-ps[i]) for i in range(2))
  ex+=mu*(1+yy)**degree
 direct=S.diff(ex,r0,r1).subs({r0:0,r1:0})
 f4=S.diff((1+vv+ww)**degree,vv,2,ww,2)
 rhs=S.integrate(S.integrate((ss[0]-aa[0]*vv)*(ss[1]-aa[1]*ww)*f4,(vv,lo[0],hi[0])),(ww,lo[1],hi[1]))
 eq(direct,rhs)
 for i,ri in enumerate([r0,r1]):
  rhs=0
  for x in product([0,1],repeat=2):
   mu=S.prod(pp[j] if x[j] else 1-pp[j] for j in range(2))
   vals=[tt[j]/pp[j] if x[j] else -tt[j]/(1-pp[j]) for j in range(2)]
   mui=pp[i] if x[i] else 1-pp[i]
   yi1=(ss[i]-aa[i]*vals[i])/mui*(1 if x[i] else -1)
   rhs+=mu*degree*(degree-1)*(1+sum(vals))**(degree-2)*yi1**2
  eq(S.diff(ex,ri,2).subs({r0:0,r1:0}),rhs)
# Constants and reported finite gap.
eq((R(7,5)*R(4,5)**2)/(8*R(3,5)**3),R(14,27))
beta=R(10,21)*J
def entropy(at):
 return -sum(mp.mpf(str(vv))*mp.log(mp.mpf(str(vv))) for vv in [S.simplify(v.subs(t,at)) for v in polys.values()])
def h(x):
 x=mp.mpf(str(x));return -x*mp.log(x)-(1-x)*mp.log(1-x)
gap=entropy(R(1,2))-(entropy(0)+entropy(1))/2
leaf=sum(h((p0[i]+p1[i])/2)-(h(p0[i])+h(p1[i]))/2 for i in range(3))
quart=S.simplify(beta*sum((S.expand(z0[i]*S.conjugate(z0[i]))**2+S.expand(z1[i]*S.conjugate(z1[i]))**2)/2-S.expand(((z0[i]+z1[i])/2)*S.conjugate((z0[i]+z1[i])/2))**2 for i in range(3)))
result={'exact_assertions':checks,'a_D':str(av),'b_D':str(bv),'Fisher_J_D':str(J),'endpoint_radius_values':margins,'direction_inertia':[2,2,1],'quartic_bound_exact':str(quart),'numerical_midpoint_gap':str(gap),'numerical_leaf_gap':str(leaf),'numerical_total_bound':str(leaf+mp.mpf(str(quart))),'numeric_Hessian_eigenvalues':[str(q) for q in mp.eigsy(M,eigvals_only=True)]}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
