import itertools,json
from pathlib import Path
import numpy as np
ROOT=Path(__file__).parent
rng=np.random.default_rng(700720260915)

def atoms2(A):
 a,b=A[0,0].real,A[1,1].real
 r=a*b-abs(A[0,1])**2
 return np.array([1-a-b+r,a-r,b-r,r])

def dp2(A,E):
 a,b=A[0,0].real,A[1,1].real;u,v=E[0,0].real,E[1,1].real
 r=u*b+a*v-2*(A[0,1].conjugate()*E[0,1]).real
 return np.array([-u-v+r,u-r,v-r,r])

def atoms_derivatives(K,A):
 n=len(K);p=[];p1=[];p2=[]
 for x in range(1<<n):
  bits=np.array([(x>>j)&1 for j in range(n)])
  M=np.where(bits[None,:],K,np.eye(n)-K)
  E=A*(2*bits-1)[None,:]
  val=np.linalg.det(M).real;R=np.linalg.solve(M,E);tr=np.trace(R)
  p.append(val);p1.append((val*tr).real);p2.append((val*(tr*tr-np.trace(R@R))).real)
 return np.array(p),np.array(p1),np.array(p2)

def Rj(p,j,d):
 out=p.copy()
 for x in range(len(p)):
  if not ((x>>j)&1):
   y=x|(1<<j);total=p[x]+p[y];out[x]=(1-d)*total;out[y]=d*total
 return out

def DJ(p,q,u,v):
 r=np.log(p/q)
 return np.dot(u,r+1-q/p)+np.dot(v,-r+1-p/q)

def conditionals(K,p):
 n=len(K);out=[];O=list(range(2,n));C=K[np.ix_(O,O)]
 for y in range(1<<(n-2)):
  inds=[x+(y<<2) for x in range(4)];q=p[inds].sum()
  if O:
   absent=np.diag([1-((y>>j)&1) for j in range(n-2)])
   Q=C-absent
   CC=K[:2,:2]-K[:2,2:]@np.linalg.solve(Q,K[2:,:2])
  else:CC=K.copy()
  CC=(CC+CC.conj().T)/2
  assert np.max(np.abs(p[inds]-q*atoms2(CC)))<1e-11
  out.append((inds,q,CC))
 return out

def decomposition(K,D):
 n=len(K);A=K-D;p,p1,p2=atoms_derivatives(K,A)
 minus_hess=np.sum(p1*p1/p)+np.dot(p2,np.log(p))
 b=D[:2,:2];part=np.zeros_like(p);GB=0.;z=[]
 for inds,q,C in conditionals(K,p):
  pc=atoms2(C);direction=C-b;v=dp2(C,direction)
  L=np.log(pc[1]*pc[2]/(pc[0]*pc[3]))
  GB+=q*(np.sum(v*v/pc)-2*np.linalg.det(direction).real*L)
  part[inds]=q*v;z.append(q*C[0,1])
 QO=0.;Es=[]
 for j in range(2,n):
  q=Rj(p,j,D[j,j].real)
  QO+=np.sum((p-q)**2/p)
  for k in range(2,n):
   if j==k:continue
   u=Rj(p,k,D[k,k].real)-p;v=Rj(q,k,D[k,k].real)-q
   QO-=DJ(p,q,u,v)
  Es.append(DJ(p,q,part,Rj(part,j,D[j,j].real)))
 # Independent check of the closed occupation generator.
 L0=sum((Rj(p,j,D[j,j].real)-p for j in range(n)),start=np.zeros_like(p))
 coh=np.zeros_like(p)
 for y,zz in enumerate(z):coh[y*4:y*4+4]=-2*(D[0,1].conjugate()*zz).real*np.array([1,-1,-1,1])
 generator_error=np.max(np.abs(-p1-L0-coh))
 return dict(minus_hessian=float(minus_hess),outside_curvature=float(QO),block_curvature=float(GB),cross_dissipations=[float(x) for x in Es],identity_error=float(abs(minus_hess-QO-GB-2*sum(Es))),generator_error=float(generator_error))

def randK(n):
 Z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));U,_=np.linalg.qr(Z)
 ev=rng.uniform(.12,.88,size=n);return (U*ev)@U.conj().T

checks=[]
for n in [3,4,5]:
 for rep in range(12):
  K=randK(n);D=np.diag(rng.uniform(.15,.85,size=n)).astype(complex);D[:2,:2]=randK(2)
  checks.append(decomposition(K,D))
max_error=max(r['identity_error'] for r in checks)
max_gen=max(r['generator_error'] for r in checks)
assert max_error<1e-9 and max_gen<1e-11

A=np.array([[1,2],[2,5]],float)/20
B=np.array([[1003,1996],[1996,3997]],float)/5000
K=np.zeros((3,3));K[:2,:2]=A;K[:2,2]=[.01,-.02];K[2,:2]=[.01,-.02];K[2,2]=.5
D=np.zeros((3,3));D[:2,:2]=B;D[2,2]=.5
example=decomposition(K,D)
assert -5e-6<example['cross_dissipations'][0]<-4e-6

# Pure inter-block perturbation: independently extract determinant coefficients.
n=5;K0=np.diag([.4,.6,.35,.55,.65]).astype(complex);K0[0,1]=.15+.04j;K0[1,0]=.15-.04j
Z=(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/10
E=(Z+Z.conj().T)/2;np.fill_diagonal(E,0);E[:2,:2]=0
mu,_,_=atoms_derivatives(K0,E)
coefs=np.zeros((1<<n,n+1))
for x in range(1<<n):
 bits=np.array([(x>>j)&1 for j in range(n)])
 M=np.where(bits[None,:],K0,np.eye(n)-K0);V=E*(2*bits-1)[None,:]
 for r in range(n+1):
  for J in itertools.combinations(range(n),r):
   T=M.copy();T[:,J]=V[:,J];coefs[x,r]+=np.linalg.det(T).real
Cdirect=np.sum(coefs[:,2]**2/mu)
Cformula=0.
for j in range(2,n):
 a=E[:2,j];Q=np.outer(a,a.conjugate());v=dp2(K0[:2,:2],Q)
 Cformula+=np.sum(v*v/atoms2(K0[:2,:2]))/(K0[j,j].real*(1-K0[j,j].real))
for j in range(2,n):
 for k in range(j+1,n):
  vj=K0[j,j].real*(1-K0[j,j].real);vk=K0[k,k].real*(1-K0[k,k].real)
  Cformula+=abs(E[j,k])**4/(vj*vk)
orth=np.sum(coefs[:,2]*coefs[:,3]/mu)
assert abs(Cdirect-Cformula)<1e-12 and abs(orth)<1e-12
out={'seed':700720260915,'random_cases':len(checks),'max_hessian_identity_error':max_error,'max_closed_generator_error':max_gen,'minimum_sampled_total_curvature':min(x['minus_hessian'] for x in checks),'exact_obstruction_example_hessian_decomposition':example,'quartic':{'direct_coefficient_C':Cdirect,'formula_coefficient_C':Cformula,'inner_product_q2_q3':orth,'interpretation':'H(K0+tE)=H(K0) - C*t^4/2 + O(t^6)'}}
(ROOT/'results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
