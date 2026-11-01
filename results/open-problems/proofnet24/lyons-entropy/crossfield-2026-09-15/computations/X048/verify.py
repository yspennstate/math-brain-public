"""Exact finite algebra checks for the continuous localization identities."""
import itertools, json
from pathlib import Path
import sympy as s
I=s.I; R=s.Rational; n=3; eye=s.eye(n)
T=s.Matrix([[2,R(1,3),I/5],[R(1,3),1,-R(1,7)],[-I/5,-R(1,7),R(3,2)]])
L=T*T; K=L*(eye+L).inv(); Mh=T*(eye+L).inv()
A=s.Matrix([[R(1,3),R(1,5)+I/7,-R(2,9)],[R(1,5)-I/7,-R(1,4),I/8],[-R(2,9),-I/8,R(1,6)]])
D=s.diag(R(1,4),4,9); Dh=s.diag(R(1,2),2,3); E=D-eye
sets=[tuple(j for j in range(n) if mask>>j&1) for mask in range(1<<n)]
checks=0
def eq(a,b):
 global checks
 dif=a-b
 if isinstance(dif,s.MatrixBase): assert all(s.cancel(x)==0 for x in dif)
 else: assert s.cancel(dif)==0, s.cancel(dif)
 checks+=1
def atoms(J):
 return [s.cancel((-1)**(n-len(S))*(J-s.diag(*[int(i not in S) for i in range(n)])).det()) for S in sets]
def jets(J,V,W=None):
 p=atoms(J); d=[]; dd=[]
 for S,ps in zip(sets,p):
  Y=(J-s.diag(*[int(i not in S) for i in range(n)])).inv()
  z=Y*V; d.append(s.cancel(ps*s.trace(z)))
  dd.append(s.cancel(ps*(s.trace(z)**2-s.trace(z*z)+(s.trace(Y*W) if W is not None else 0))))
 return p,d,dd
def crossjet(J,U,V):
 p=atoms(J); out=[]
 for S,ps in zip(sets,p):
  Y=(J-s.diag(*[int(i not in S) for i in range(n)])).inv()
  out.append(s.cancel(ps*(s.trace(Y*U)*s.trace(Y*V)-s.trace(Y*U*Y*V))))
 return out
p=atoms(K); eq(sum(p),1)
Pi=[]
for S in sets:
 W=T[:,list(S)]
 Pi.append(W*L.extract(S,S).inv()*W.conjugate().T if S else s.zeros(n))
weights=[ps*s.prod(D[i,i] for i in S) for S,ps in zip(sets,p)]
Z=s.cancel(sum(weights)); post=[s.cancel(w/Z) for w in weights]
Q=eye-(eye+T*D*T).inv(); J=Dh*L*Dh*(eye+Dh*L*Dh).inv()
eq(Q,sum((ps*P for ps,P in zip(post,Pi)),s.zeros(n)))
for degree in (1,2,3):
 combos=list(itertools.combinations(range(n),degree))
 for U in combos:
  for V in combos:
   eq(Q.extract(U,V).det(),sum(ps*P.extract(U,V).det() for ps,P in zip(post,Pi)))
for j,S in enumerate(sets): eq(post[j],atoms(J)[j])
B=Mh.inv()*A*Mh.inv(); C=Q-K
sig=s.trace(B*C); eta=sig**2-s.trace(B*C*B*C)
F=E*(eye+K*E).inv(); U=Dh*(eye+K*E).inv()
Ad=U*A*U.conjugate().T; Add=-2*U*A*F*A*U.conjugate().T
eq(sig,s.trace(F*A)); eq(eta,s.trace(F*A)**2-s.trace(F*A*F*A))
_,dp,ddp=jets(K,A)
eq(sig,sum(w*d/ps for w,d,ps in zip(post,dp,p)))
eq(eta,sum(w*d/ps for w,d,ps in zip(post,ddp,p)))
Rinv=(eye+E*K).inv()
eq(Ad,Dh*(A*Rinv-K*Rinv*E*A*Rinv)*Dh)
eq(Add,Dh*(-2*A*Rinv*E*A*Rinv+2*K*Rinv*E*A*Rinv*E*A*Rinv)*Dh)
_,pd,pdd=jets(J,Ad,Add)
for j in range(1<<n):
 eq(pd[j],post[j]*(dp[j]/p[j]-sig))
 eq(pdd[j],post[j]*(ddp[j]/p[j]-2*sig*dp[j]/p[j]+2*sig**2-eta))
for i in range(n):
 ei=eye[:,i]; Ei=ei*ei.T; m=J[i,i]
 Vi=D[i,i]*(eye-Q)*T*Ei*T*(eye-Q)
 eq(Vi,sum((ps*(int(i in S)-m)*P for ps,S,P in zip(post,sets,Pi)),s.zeros(n)))
 assert Vi.rank()==1; checks+=1
 for Base in (K,J):
  m=Base[i,i]; q=m*(1-m)
  Ri=(Ei*Base+Base*Ei)/2-Base*Ei*Base
  Gi=I*(Ei*Base-Base*Ei)
  Di=Ei*Base+Base*Ei-2*Ei*Base*Ei
  def DR(V): return (Ei*V+V*Ei)/2-V*Ei*Base-Base*Ei*V
  eq((m-R(1,2))*Ri+DR(Ri)/2,-Di/8)
  pp,pr,prr=jets(Base,Ri); _,pg,pgg=jets(Base,Gi)
  prg=crossjet(Base,Ri,Gi)
  for h,S in enumerate(sets):
   eq(pr[h],pp[h]*(int(i in S)-m)); eq(pg[h],0)
   eq(prr[h],pgg[h]/4); eq(prg[h],0)
  eq(sum(v*v/ps for v,ps in zip(pr,pp)),q)
  al,be=R(2,3),-R(3,5); V=al*Ri+be*Gi
  assert V.det()==0; checks+=1
  tt=R(1,1000); pp1=atoms(Base+tt*V)
  for h,S in enumerate(sets):
   eq(pp1[h],pp[h]+tt*al*pr[h]+tt**2*(al*al/4+be*be)*pgg[h]/2)
# The scalar martingale determinant has the same exact finite affine likelihood.
tt=R(1,1000); pt=atoms(K+tt*A)
eq((eye+tt*B*C).det(),sum(w*v/ps for w,v,ps in zip(post,pt,p)))
# Exact Hessian formal-log comparison is certified by the atom jet checks above.
result={"status":"PASS","exact_assertions":checks,"dimension":n,
 "verified":["posterior exterior moments","rank-one recovered covariance noise","physical posterior drift","affine tilt first and second kernel jets","moving normalization jets","finite determinant likelihood","field-gauge full atom jets","finite quadratic likelihood"]}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
