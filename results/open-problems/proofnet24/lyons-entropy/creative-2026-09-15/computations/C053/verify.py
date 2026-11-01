"""Exact verifier for C053. Run from the campaign root; no floating-point signs."""
import json
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import sympy as s
OUT=Path('computations/C053');raw=json.loads((OUT/'polynomial_data.json').read_text());saved=json.loads((OUT/'bernstein_certificate.json').read_text())
z=s.Symbol('z');x=list(map(s.Rational,raw['x']));r=list(map(s.Rational,raw['r']));edges=list(combinations(range(4),2));small=raw['small_masks'];tail=[t for t in range(16) if t.bit_count()>=3];alpha=list(map(s.Rational,raw['alpha']));clo=list(map(s.Rational,raw['log_lower']));w=list(map(s.Rational,raw['weights']))
def mat(a):return s.Matrix([[s.Rational(v) for v in row] for row in a])
def enc(a):
 if isinstance(a,s.MatrixBase):return [[str(v) for v in a.row(i)] for i in range(a.rows)]
 return str(a)
def ldl(A):
 n=A.rows;L=s.eye(n);D=[]
 for i in range(n):
  di=A[i,i]-sum(L[i,k]**2*D[k] for k in range(i));assert di>0;D.append(di)
  for j in range(i+1,n):L[j,i]=(A[j,i]-sum(L[j,k]*L[i,k]*D[k] for k in range(i)))/di
 assert L*s.diag(*D)*L.T==A
 return L,D
def log_unit(q,N=70):
 h=(q-1)/(q+1);ans=sum(2*h**(2*k+1)/s.Rational(2*k+1) for k in range(N));tail=2*h**(2*N+1)/(s.Rational(2*N+1)*(1-h*h));return ans,ans+tail
log2=log_unit(s.Integer(2))
def logq(q):
 assert q>0
 if q<1:
  a,b=logq(1/q);return -b,-a
 k=0
 while q>=2:q/=2;k+=1
 a,b=log_unit(q);return a+k*log2[0],b+k*log2[1]
logs=[]
for e,(i,j) in enumerate(edges):
 a,b=logq((x[i]+x[j])/abs(x[i]-x[j]));logs.append((2*a,2*b));assert clo[e]<2*a and 2*b<clo[e]+s.Rational(1,1000)
L=s.Matrix(4,4,lambda i,j:2*r[i]*r[j]/(x[i]+x[j]));assert L==mat(raw['L'])
for t in range(16):
 ii=[i for i in range(4) if t>>i&1];assert (L.extract(ii,ii).det() if ii else 1)==w[t]
Z=sum(w[t]*z**t.bit_count() for t in range(16));assert [s.expand(Z).coeff(z,k) for k in range(5)]==list(map(s.Rational,raw['Z_coefficients']))
kn=[mat(a) for a in raw['K_numerator_coefficients']];Knum=sum((z**k*B for k,B in enumerate(kn)),s.zeros(4));assert ((s.eye(4)+z*L)*Knum-z*L*Z).applyfunc(s.expand)==s.zeros(4)
assert s.expand((s.eye(4)+z*L).det(method='domain-ge')-Z)==0
print('PASS: exact Cauchy atoms, odds polynomial, and all six log brackets',flush=True)
def g(a,t):
 k=t.bit_count()
 if a==0:return 1-k+k*(k-1)//2
 if a.bit_count()==1:return (2-k)*int(a&t==a)
 return int(a&t==a)
gramrat=[]
for h,a in enumerate(small):
 ratio=1+sum(w[t]*abs(g(a,t))*sum(abs(g(b,t)) for b in small) for t in tail)/w[a]
 assert ratio<alpha[h];gramrat.append(ratio)
# Exact polynomial matrix construction, including the Frobenius margin.
D=s.zeros(6,10)
for e,(i,j) in enumerate(edges):D[e,i]=Knum[j,j];D[e,j]=Knum[i,i];D[e,4+e]=-2*Knum[i,j]
Ad=s.zeros(4,10)
for i in range(4):Ad[i,i]=Z
M=s.zeros(11,10);M[0,:]=-s.ones(1,4)*Ad+s.ones(1,6)*D
for i in range(4):M[1+i,:]=Ad[i,:]-sum((D[e,:] for e,ed in enumerate(edges) if i in ed),s.zeros(1,10))
for e in range(6):M[5+e,:]=D[e,:]
Fhat=s.zeros(10)
for i in range(4):Fhat[i,i]=s.Rational(3,1000)
for e,((i,j),c) in enumerate(zip(edges,clo)):Fhat[i,j]=Fhat[j,i]=c;Fhat[4+e,4+e]=-2*c
Q=-z**2*Z*Fhat
for h,a in enumerate(small):Q+=z**(2-a.bit_count())*M[h,:].T*M[h,:]/(alpha[h]*w[a])
cc=[mat(a) for a in raw['polynomial_coefficients']]
assert (Q-sum((z**k*B for k,B in enumerate(cc)),s.zeros(10))).applyfunc(s.expand)==s.zeros(10)
for k in range(5):cc[k+2]-=s.Rational(raw['Z_coefficients'][k])*s.diag(*([1]*4+[2]*6))
d=len(cc)-1;a=s.Rational(1,4);width=s.Rational(3,4);mins=[]
for i,cert in enumerate(saved['coefficients']):
 weights=[sum(s.Rational(comb(i,j),comb(d,j))*comb(k,j)*a**(k-j)*width**j for j in range(min(i,k)+1)) for k in range(d+1)]
 B=sum((weights[k]*cc[k] for k in range(d+1)),s.zeros(10));assert B==mat(cert['matrix']);LL=mat(cert['L']);DD=list(map(s.Rational,cert['D']));assert LL*s.diag(*DD)*LL.T==B
 assert all(DD[k]>cert['integer_lower_bounds'][k]>0 for k in range(10));mins.append(min(cert['integer_lower_bounds']))
print('PASS: Lagrange Gram domination and all 11 positive Bernstein LDL factorizations',flush=True)
# Exact degree-one failure and exact degree-two Schur success at z=1.
p=s.Matrix([w[t]/Z.subs(z,1) for t in range(16)]);K=Knum.subs(z,1)/Z.subs(z,1)
X=s.Matrix([[int(t>>i&1) for i in range(4)] for t in range(16)]);ff=X.row_join(s.Matrix([[int(t>>i&1)*int(t>>j&1) for i,j in edges] for t in range(16)]));mu=ff.T*p;G=ff.T*s.diag(*p)*ff-mu*mu.T
Sigma=G[:4,:4];Pl=s.zeros(10);Pl[:4,:4]=s.eye(4)
for e,(i,j) in enumerate(edges):Pl[4+e,i]=K[j,j];Pl[4+e,j]=K[i,i];Pl[4+e,4+e]=-2*K[i,j]
I2=Pl.T*G.inv()*Pl;Q2=I2-Fhat;Schur=Q2[:4,:4]-Q2[:4,4:]*Q2[4:,4:].inv()*Q2[4:,:4]
LS,DS=ldl(Schur-7*s.eye(4));a0=s.Matrix([2,3,1,3]);Clo=Fhat[:4,:4]-s.Rational(3,1000)*s.eye(4);fail=(a0.T*(Sigma.inv()-Clo)*a0)[0];assert fail<-100
# The exact connected four-site base also defeats the full C045 shared-coefficient allocation.
N=s.Matrix([t.bit_count() for t in range(16)]);nbar=(N.T*p)[0];h=N-s.ones(16,1)*nbar;var=(h.T*s.diag(*p)*h)[0];du=[57,13,10,63,6,18];rho=[]
for e,(i,j) in enumerate(edges):
 marg=[sum(p[t] for t in range(16) if ((t>>i&1)+2*(t>>j&1))==q) for q in range(4)]
 hp=[sum(p[t]*h[t] for t in range(16) if ((t>>i&1)+2*(t>>j&1))==q) for q in range(4)]
 Tsq=(marg[1]+marg[2])**2/(4*marg[0]*marg[3]);assert Tsq<(s.Rational(du[e],2)-1)**2
 rho.append(sum(hp[q]**2/marg[q] for q in range(4))/var)
rlo=[s.Rational(q,1000) for q in [388,20,375,211,632,359]]
assert all(rho[e]>rlo[e] for e in range(6))
ray0=sum(clo[e]*rlo[e]/du[e] for e in range(6));raym=clo[2]*var;assert ray0>s.Rational(29,20);assert raym>s.Rational(3,2)
print('PASS: degree-one failure, degree-two Schur > 7 I, and every C045 shared coefficient fails',flush=True)
# Actual full atom derivatives and degree-two projection, independent of the polynomial proof.
Aind=s.diag(2,3,1,3);Aind[1,2]=Aind[2,1]=2
Acx=s.Matrix([[2,s.Rational(1,3)+s.I/5,-s.Rational(1,4),s.I/6],[s.Rational(1,3)-s.I/5,-1,s.Rational(2,5)+s.I/7,s.Rational(1,8)],[-s.Rational(1,4),s.Rational(2,5)-s.I/7,1,s.Rational(1,9)-s.I/4],[-s.I/6,s.Rational(1,8),s.Rational(1,9)+s.I/4,-2]])
checks=[]
for z0 in [s.Rational(1,4),s.Integer(1)]:
 k=Knum.subs(z,z0)/Z.subs(z,z0);pp=s.Matrix([w[t]*z0**t.bit_count()/Z.subs(z,z0) for t in range(16)]);gg=s.Matrix([[g(a,t) for a in small] for t in range(16)]);gram=gg.T*s.diag(*pp)*gg;graminv=gram.inv()
 for name,A0 in [('rank_four_indefinite',Aind),('complex_Hermitian',Acx)]:
  qp=[];qpp=[]
  for t in range(16):
   mm=s.Matrix.hstack(*[(k[:,j] if t>>j&1 else s.eye(4)[:,j]-k[:,j]) for j in range(4)]);dd=s.Matrix.hstack(*[(A0[:,j] if t>>j&1 else -A0[:,j]) for j in range(4)]);assert s.simplify(mm.det()-pp[t])==0
   R=mm.inv()*dd;tr=s.simplify(s.trace(R));qp.append(s.simplify(pp[t]*tr));qpp.append(s.simplify(pp[t]*(tr**2-s.trace(R*R))))
  qp=s.Matrix(qp);qpp=s.Matrix(qpp);assert sum(qp)==sum(qpp)==0
  m=gg.T*qp;proj=(m.T*graminv*m)[0];fi=sum(qp[t]**2/pp[t] for t in range(16));lower=sum(m[j]**2/(alpha[j]*pp[small[j]]) for j in range(11));assert fi>=proj>=lower
  norm=s.simplify(s.trace(A0*A0));fl=0;fu=0
  for e,(i,j) in enumerate(edges):
   det=s.simplify(A0[i,i]*A0[j,j]-A0[i,j]*A0[j,i]);v=sum(qpp[t] for t in range(16) if t>>i&1 and t>>j&1);assert s.simplify(v-2*det)==0
   lo,hi=logs[e];fl+=2*det*(lo if det>=0 else hi);fu+=2*det*(hi if det>=0 else lo)
  assert lower-fu>=norm
  # Independent full frozen log-atom curvature from the Cauchy atom weights.
  slo=0;shi=0
  for t in range(16):
   lo,hi=logq(pp[t]);slo+=-qpp[t]*(lo if qpp[t]<=0 else hi);shi+=-qpp[t]*(hi if qpp[t]<=0 else lo)
  assert max(slo,fl)<=min(shi,fu)
  if z0==1 and name=='rank_four_indefinite':
   linear=(a0.T*Sigma.inv()*a0)[0];assert fl-linear>8
  checks.append({'z':str(z0),'direction':name,'A':enc(A0),'atom_probabilities':list(map(str,pp)),'q':list(map(str,qp)),'qpp':list(map(str,qpp)),'Fisher':str(fi),'degree_two_projection':str(proj),'Lagrange_lower':str(lower),'frozen_lower':str(fl),'frozen_upper':str(fu),'frobenius_squared':str(norm)})
print('PASS: 64 exact atom derivative triples; full Fisher >= degree-two >= Lagrange; full-Hermitian strong margins',flush=True)
report={'status':'PASS','K_at_one':enc(K),'log_intervals':[[str(a),str(b)] for a,b in logs],'gram_alpha_ratios':list(map(str,gramrat)),'bernstein_min_pivot_integer_lower_bounds':mins,'Schur_minus_7I_L':enc(LS),'Schur_minus_7I_D':list(map(str,DS)),'degree_one_failure_upper':str(fail),'allocation_rayleigh_lower_t0':str(ray0),'allocation_rayleigh_lower_tm':str(raym),'directional_checks':checks}
(OUT/'verification_results.json').write_text(json.dumps(report,indent=2))
