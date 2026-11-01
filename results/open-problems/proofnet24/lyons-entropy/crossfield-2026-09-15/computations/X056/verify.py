"""Exact self-checks for complementary balancing and its complete second jet."""
import itertools, json
from pathlib import Path
import sympy as S
Q=S.Rational; ii=S.I; n=3; I=S.eye(n)
assertions=0
def check(a,b=0):
 global assertions
 if isinstance(a,S.MatrixBase):
  assert all(S.simplify(x)==0 for x in a-b)
 else: assert S.simplify(a-b)==0, (a,b,S.simplify(a-b))
 assertions+=1
masks=list(range(8)); xs=[S.Matrix([(m>>i)&1 for i in range(3)]) for m in masks]
zs=[x-S.ones(3,1)/2 for x in xs]
def atoms(K):
 return [S.simplify(S.Matrix.hstack(*[(K if (m>>j)&1 else I-K)[:,j] for j in range(3)]).det()) for m in masks]
def jets(K,A):
 t=S.symbols('t'); ps=atoms(K+t*A)
 return [S.expand(p).coeff(t,0) for p in ps], [S.expand(p).coeff(t,1) for p in ps], [2*S.expand(p).coeff(t,2) for p in ps]
def tilt(K,D):
 Dhalf=S.diag(*[S.sqrt(D[i,i]) for i in range(3)])
 return S.simplify(Dhalf*K*(I+(D-I)*K).inv()*Dhalf)
def mean(vals,weights): return sum((p*v for p,v in zip(weights,vals)), S.zeros(*vals[0].shape) if isinstance(vals[0],S.MatrixBase) else S.S(0))
def center_project(vals,weights):
 sig=mean(vals,weights)
 cov=mean([z*(v-sig) for z,v in zip(zs,vals)],weights)
 Sigma=mean([z*z.T for z in zs],weights)
 coef=Sigma.inv()*cov
 return [S.simplify(v-sig-(coef.T*z)[0]) for v,z in zip(vals,zs)],coef
# A centered base with nonzero odd interaction tests the general balancing jets.
B=I/2+S.Matrix([[0,Q(1,10),Q(1,20)*(1+ii)],[Q(1,10),0,Q(1,12)],[Q(1,20)*(1-ii),Q(1,12),0]])
D=S.diag(Q(9,4),Q(16,9),Q(25,16)); K=tilt(B,D.inv()); check(tilt(K,D),B)
A=S.Matrix([[Q(1,7),Q(1,9)+ii/10,-Q(1,11)+ii/13],[Q(1,9)-ii/10,-Q(1,5),Q(1,8)+ii/15],[-Q(1,11)-ii/13,Q(1,8)-ii/15,Q(1,6)]])
p,p1,p2=jets(K,A); q=atoms(B); scores=[a/b for a,b in zip(p1,p)]; acc=[a/b for a,b in zip(p2,p)]
for j in range(3): check(mean([z[j] for z in zs],q))
h,minus_v=center_project(scores,q); v=-minus_v
T=[r-s*s+hh*hh for r,s,hh in zip(acc,scores,h)]; rr,minus_w=center_project(T,q); w=-minus_w
E=D-I; U=S.sqrt(D)*(I+K*E).inv(); F=E*(I+K*E).inv()
A0=S.simplify(U*A*U.conjugate().T); C0=S.simplify(-2*U*A*F*A*U.conjugate().T)
def R(z):
 V=S.diag(*list(z)); return (V*B+B*V)/2-B*V*B
def dR(z,X):
 V=S.diag(*list(z)); return (V*X+X*V)/2-X*V*B-B*V*X
B1=S.simplify(A0+R(v)); B2=S.simplify(C0+2*dR(v,A0)+R(w)+dR(v,R(v)))
for j in range(3): check(B1[j,j]); check(B2[j,j])
q0,q1,q2=jets(B,B1); c0,c1,c2=jets(B,B2)
for j in range(8):
 check(q1[j]/q[j],h[j]); check((q2[j]+c1[j])/q[j],rr[j])
check(mean(h,q)); check(mean(rr,q))
for j in range(3):
 check(mean([z[j]*a for z,a in zip(zs,h)],q));check(mean([z[j]*a for z,a in zip(zs,rr)],q))
# Closed complementary balancing and field-invariant pair interactions.
V=S.Matrix([[0,-Q(2,5),Q(1,5)],[Q(2,5),0,-Q(1,10)],[-Q(1,5),Q(1,10),0]])
Bc=I/2+ii*V; Kc=tilt(Bc,D.inv()); pc=atoms(Kc); qc=atoms(Bc)
for j in range(3):
 d2=S.factor(pc[0]*pc[7^(1<<j)]/(pc[7]*pc[1<<j]));check(d2,D[j,j]**2)
for m in masks:
 check(qc[m],qc[7^m]);check(pc[m]*pc[7^m]/(qc[m]**2),pc[0]*pc[7]/(qc[0]**2))
check(pc[0]*pc[3]*pc[5]*pc[6],pc[1]*pc[2]*pc[4]*pc[7])
# Actual fixed-field affine Hessian ingredients, no dropped field acceleration.
J=tilt(Bc,D); pp,aa,bb=jets(Bc,A); qq=atoms(J)
Uc=S.sqrt(D)*(I+Bc*(D-I)).inv(); Fc=(D-I)*(I+Bc*(D-I)).inv(); Ac=S.simplify(Uc*A*Uc.conjugate().T)
x0,x1,x2=jets(J,Ac); sc=[a/b for a,b in zip(aa,pp)]; rc=[a/b for a,b in zip(bb,pp)]
y0,y1,y2=jets(Bc,S.simplify(A*Fc*A)); sc2=[a/b for a,b in zip(y1,pp)]
sigma=S.trace(Fc*A); eta=sigma**2-S.trace(Fc*A*Fc*A)
for m in masks:
 check(x1[m]/qq[m],sc[m]-sigma)
 check(x2[m]/qq[m],rc[m]-2*sigma*sc[m]+2*sc2[m]+eta)
# Symbolic normalization of the quantitative center-gap extraction.
f=S.symbols('f',positive=True); den=(1-f)*(3+f)
al=(36-12*f*f-8*f**3)/den; be=-16*f**3/den; ga=16*f*f*(3-2*f)/den
check(al*ga-be*be,576*f*f/den)
check(al-ga,12*(3+3*f-2*f*f)/(3+f))
check((Q(384,25)*f*f/den)/(Q(18,5)*al+Q(9,5)*ga),16*f*f/(45*(3+f*f-2*f**3)))
# Quantitative example uses only rational bounds on log/exponential functions.
t=Q(3069,3073); delta=16*t*t/(45*(3+t*t-2*t**3)); assert delta>Q(1,6);assertions+=1
rho=Q(3,1000); cost=14*rho/(1-rho); assert (1-Q(3,2500))*(Q(1,6)-cost)>Q(3,25);assertions+=1
# c=10 log 2 lies between 20/3 and 7 via a finite atanh series.
x=Q(1,3); lower=2*sum(x**(2*k+1)/Q(2*k+1) for k in range(8)); upper=lower+2*x**17/(17*(1-x*x))
assert lower>Q(2,3) and upper<Q(7,10); assertions+=1
out={'status':'PASS','exact_assertions':assertions,'scope':'Algebraic balancing, every atom of both second jets, complementary normal form, rational simultaneous-field bound.'}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
