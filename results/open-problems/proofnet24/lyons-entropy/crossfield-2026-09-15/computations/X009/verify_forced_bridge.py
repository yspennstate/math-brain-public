"""Deterministic exact and 60-digit checks of X009's forced cube bridge formulas."""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json
import sympy as sp
import mpmath as mp


def Lcube(n):
 N=1<<n; L=sp.zeros(N)
 for x in range(N):
  L[x,x]=-n
  for i in range(n): L[x,x^(1<<i)]=1
 return L


def faces(n):
 for i,j in combinations(range(n),2):
  for x in range(1<<n):
   if not (x&(1<<i) or x&(1<<j)):
    yield x,x^(1<<i),x^(1<<j),x^(1<<i)^(1<<j),i,j


class LogExpr:
 """Exact rational linear combinations of 1 and logarithms of primes."""
 def __init__(self): self.terms={1:sp.Rational(0)}
 def const(self,x): self.terms[1]+=sp.Rational(x)
 def log(self,c,r):
  r=sp.Rational(r); c=sp.Rational(c)
  for z,sgn in [(r.p,1),(r.q,-1)]:
   for prime,exponent in sp.factorint(z).items():
    self.terms[prime]=self.terms.get(prime,0)+sgn*c*exponent
 def D(self,c,a,b):
  self.log(c*a,a/b); self.const(c*(b-a))
 def same(self,other):
  return all(sp.simplify(self.terms.get(k,0)-other.terms.get(k,0))==0 for k in self.terms.keys()|other.terms.keys())


def exact_cube_check(n):
 N=1<<n; L=Lcube(n)
 rr=[sp.Rational(1+(7*x+3)%17) for x in range(N)]
 kk=[sp.Rational(1+(5*x+2)%13,1+(3*x+1)%7) for x in range(N)]
 Z=sum(r*r for r in rr)
 f=sp.Matrix([r/k for r,k in zip(rr,kk)])
 g=sp.Matrix([r*k/Z for r,k in zip(rr,kk)])
 p=[f[x]*g[x] for x in range(N)]
 v=[g[x]*(L*f)[x]-f[x]*(L*g)[x] for x in range(N)]
 a0=[g[x]*(L*L*f)[x]+f[x]*(L*L*g)[x]-2*(L*f)[x]*(L*g)[x] for x in range(N)]
 direct=LogExpr(); direct.const(sum(v[x]**2/p[x] for x in range(N)))
 for x in range(N): direct.log(a0[x],p[x])
 bregman=LogExpr()
 for x in range(N):
  for z in [f,g]:
   for i in range(n):
    for j in range(n):
     a=z[x^(1<<i)^(1<<j)]/z[x]
     b=z[x^(1<<i)]*z[x^(1<<j)]/z[x]**2
     bregman.D(p[x],a,b)
 assert direct.same(bregman)
 strengthened=LogExpr(); Ekin=0
 for x in range(N):
  for i in range(n):
   y=x^(1<<i)
   if x<y:
    j=f[x]*g[y]-f[y]*g[x]
    Ekin+=j*j*(1/p[x]+1/p[y])
    strengthened.log(2*(p[x]-p[y]),p[x]/p[y])
 strengthened.const(Ekin)
 def coshr(r): return (r+1/r)/2
 for a,b,c,d,i,j in faces(n):
  alpha=rr[a]*rr[d]/Z; beta=rr[b]*rr[c]/Z
  cu=coshr(kk[d]/kk[a]); cv=coshr(kk[c]/kk[b])
  ch=coshr(kk[a]*kk[d]/(kk[b]*kk[c]))
  # Static face curvature 8(beta-alpha) log(beta/alpha).
  strengthened.log(8*(beta-alpha),beta/alpha)
  # Excess face curvature.
  strengthened.const(8*((beta-alpha)*(cu-1)+(alpha-beta)*(cv-1)+(beta*cu+alpha*cv)*(ch-1)))
  strengthened.log(8*(-alpha*(cu-1)+beta*(cv-1)),beta/alpha)
 assert direct.same(strengthened)
 # Exact atom-level face expansion for unforced bridge acceleration.
 acc=[2*sum(p[x]-p[x^(1<<i)] for i in range(n)) for x in range(N)]
 for a,b,c,d,i,j in faces(n):
  Q=f[a]*g[d]+g[a]*f[d]-f[b]*g[c]-g[b]*f[c]
  for x,sign in [(a,1),(b,-1),(c,-1),(d,1)]: acc[x]+=2*sign*Q
 assert all(sp.simplify(acc[x]-a0[x])==0 for x in range(N))
 return {"n":n,"Bregman_curvature_identity":"EXACT PASS","stationary_subtraction_and_cosh_remainder":"EXACT PASS","bridge_face_acceleration":"EXACT PASS"}


def dpp_jet(K,A,x):
 n=K.rows; M=K-sp.diag(*[1-((x>>i)&1) for i in range(n)])
 sign=(-1)**sum(1-((x>>i)&1) for i in range(n))
 p=sign*M.det(); v=0; a=0
 for i in range(n):
  N=M.copy(); N[i,:]=A[i,:]; v+=sign*N.det()
 for i,j in combinations(range(n),2):
  N=M.copy(); N[i,:]=A[i,:]; N[j,:]=A[j,:]; a+=2*sign*N.det()
 return [sp.simplify(z) for z in (p,v,a)]


def mprat(x): return mp.mpf(str(sp.numer(x)))/mp.mpf(str(sp.denom(x)))


def numerical_dpp_check(K,A,name):
 mp.mp.dps=65; n=K.rows; N=1<<n
 jets=[dpp_jet(K,A,x) for x in range(N)]
 assert all(p>0 for p,v,a in jets)
 p=mp.matrix([mprat(z[0]) for z in jets]); v=mp.matrix([mprat(z[1]) for z in jets]); a=mp.matrix([mprat(z[2]) for z in jets])
 edges=[(x,x^(1<<i)) for x in range(N) for i in range(n) if x<x^(1<<i)]
 def build(th):
  grad=mp.zeros(N,1); G=mp.zeros(N); js=[]; ws=[]
  for x,y in edges:
   r=2*mp.sqrt(p[x]*p[y]); d=th[y]-th[x]
   j=r*mp.sinh(d); w=r*mp.cosh(d); js.append(j);ws.append(w)
   grad[x]-=j;grad[y]+=j
   G[x,x]+=w;G[y,y]+=w;G[x,y]-=w;G[y,x]-=w
  return grad,G,js,ws
 th=mp.zeros(N,1)
 for iteration in range(40):
  grad,G,js,ws=build(th); error=grad-v
  if max(abs(x) for x in error)<mp.mpf('1e-55'): break
  step=mp.lu_solve(G[:N-1,:N-1],error[:N-1,:]); factor=mp.mpf(1)
  while True:
   trial=mp.matrix(th)
   for x in range(N-1): trial[x]-=factor*step[x]
   if mp.norm(build(trial)[0]-v)<mp.norm(error): th=trial;break
   factor/=2
   assert factor>mp.mpf('1e-20')
 else: raise AssertionError('Newton did not converge')
 grad,G,js,ws=build(th)
 f=mp.matrix([mp.sqrt(p[x])*mp.exp(-th[x]) for x in range(N)])
 g=mp.matrix([mp.sqrt(p[x])*mp.exp(th[x]) for x in range(N)])
 L=mp.matrix(Lcube(n).tolist()); Lf=L*f;Lg=L*g
 a0=mp.matrix([g[x]*(L*Lf)[x]+f[x]*(L*Lg)[x]-2*Lf[x]*Lg[x] for x in range(N)])
 ell=mp.matrix([mp.log(z) for z in p]); I=sum(v[x]**2/p[x] for x in range(N))
 C=I+mp.fdot(a0,ell)
 bregman=mp.mpf(0)
 def D(a,b):return a*mp.log(a/b)-a+b
 for x in range(N):
  for z in [f,g]:
   for i in range(n):
    for j in range(n):
     bregman+=p[x]*D(z[x^(1<<i)^(1<<j)]/z[x],z[x^(1<<i)]*z[x^(1<<j)]/z[x]**2)
 Ekin=sum(j*j*(1/p[x]+1/p[y]) for (x,y),j in zip(edges,js))
 R=mp.mpf(0); adyn=mp.zeros(N,1); forced_face=mp.mpf(0); Qmax=mp.ninf
 for aa,bb,cc,dd,i,j in faces(n):
  alpha=mp.sqrt(p[aa]*p[dd]); beta=mp.sqrt(p[bb]*p[cc]); logr=mp.log(beta/alpha)
  u=th[dd]-th[aa]; vv=th[cc]-th[bb]; h=th[aa]+th[dd]-th[bb]-th[cc]
  cu=mp.cosh(u);cv=mp.cosh(vv);ch=mp.cosh(h)
  R+=8*((beta-alpha-alpha*logr)*(cu-1)+(alpha-beta+beta*logr)*(cv-1)+(beta*cu+alpha*cv)*(ch-1))
  DQ=2*alpha*(cu-1)-2*beta*(cv-1)
  for x,sign in [(aa,1),(bb,-1),(cc,-1),(dd,1)]: adyn[x]+=2*sign*DQ
  B=[i,j];RR=[r for r in range(n) if r not in B]
  M=K.extract(RR,RR)-sp.diag(*[1-((aa>>r)&1) for r in RR])
  q=(-1)**sum(1-((aa>>r)&1) for r in RR)*M.det()
  V=A.extract(B,B)-A.extract(B,RR)*M.inv()*K.extract(RR,B)
  Q=mprat(sp.simplify(q*sp.re(V.det())))
  Qmax=max(Qmax,Q)
  lam=2*logr;assert lam>=-mp.mpf('1e-60')
  forced_face+=2*(DQ-Q)*lam
 # Full and stationary-calibrated force potentials, gauged at the last atom.
 Vforce=mp.zeros(N,1);Omega=mp.zeros(N,1)
 raw=mp.lu_solve(G[:N-1,:N-1],(a-a0)[:N-1,:])
 calibrated=mp.lu_solve(G[:N-1,:N-1],(a-adyn)[:N-1,:])
 for x in range(N-1): Vforce[x]=raw[x];Omega[x]=calibrated[x]
 fullwork=mp.fdot(Vforce,G*ell);work=mp.fdot(Omega,G*ell)
 curvature=I+mp.fdot(a,ell)
 errors=[abs(C-bregman),abs(curvature-C-fullwork),abs(curvature-Ekin-R-work),abs(work-forced_face),mp.norm(G*Omega-a+adyn)]
 assert max(errors)<mp.mpf('1e-50')
 assert R>=-mp.mpf('1e-50')
 EO=mp.fdot(Omega,G*Omega);El=mp.fdot(ell,G*ell)
 bound=Ekin+R-mp.sqrt(max(EO,0)*max(El,0))
 fmt=lambda x:mp.nstr(x,28)
 return {"name":name,"noncommuting":K*A!=A*K,"p_prime_zero":all(z[1]==0 for z in jets),"max_identity_error":fmt(max(errors)),"theta_solve_residual":fmt(mp.norm(grad-v)),"negative_entropy_Hessian":fmt(curvature),"edge_kinetic_term":fmt(Ekin),"nonnegative_excess_face_term":fmt(R),"calibrated_force_work":fmt(work),"Cauchy_force_certificate_lower_bound":fmt(bound),"largest_DPP_face_Q":fmt(Qmax),"status":"PASS"}


if __name__=='__main__':
 K=sp.diag(sp.Rational(2,5),sp.Rational(1,2),sp.Rational(3,5))
 A=sp.diag(sp.Rational(1,7),sp.Rational(-1,6),sp.Rational(1,9))
 for i,j in combinations(range(3),2):
  K[i,j]=sp.Rational(i+j+1,80)+sp.I*sp.Rational(i-j,110);K[j,i]=sp.conjugate(K[i,j])
  A[i,j]=sp.Rational(i+j+1,60)+sp.I*sp.Rational(2*i-j+1,70);A[j,i]=sp.conjugate(A[i,j])
 Kr=sp.eye(3)/2+(sp.ones(3)-sp.eye(3))/10
 Ar=sp.Matrix([[0,sp.I,10*sp.I],[-sp.I,0,0],[-10*sp.I,0,0]])
 result={"exact_bridge_cases":[exact_cube_check(3),exact_cube_check(4)],"DPP_cases":[numerical_dpp_check(K,A,'dense complex noncommuting'),numerical_dpp_check(Kr,Ar,'imaginary current with positive hidden face')]}
 path=Path(__file__).with_name('results.json');path.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
