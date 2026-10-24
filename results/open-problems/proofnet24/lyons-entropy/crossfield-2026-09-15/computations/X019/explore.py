from fractions import Fraction as F
import itertools, math, json, os
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import HalfspaceIntersection
import sympy as sp
E=range(6); pairs=list(itertools.combinations(E,2)); triples=list(itertools.combinations(E,3))
atoms=[(a,b) for a in pairs for b in pairs if not set(a)&set(b)]
D=np.zeros((50,90),dtype=int)
for j,(a,b) in enumerate(atoms):
 D[pairs.index(a),j]=1; D[35+pairs.index(b),j]=1
 J=sorted(set(E)-set(a)-set(b))
 for k in J: D[15+triples.index(tuple(sorted(a+(k,)))),j]=1

def coeff(c=F(99,101),s=F(20,101)):
 # scalar unitary T=R(c,s) F_3; entries represented as (real, sqrt(3)*imag) / sqrt(3)
 # operations on x+i sqrt(3)y
 def add(x,y): return (x[0]+y[0],x[1]+y[1])
 def mul(x,y): return (x[0]*y[0]-3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
 def conj(x): return (x[0],-x[1])
 def ab(x):return x[0]**2+3*x[1]**2
 al=[c+s,c-s,F(1)]
 be=[(c-s/2,s/2),(-s-c/2,c/2),(F(-1,2),F(-1,2))]
 A=[x*x/3 for x in al];B=[ab(x)/3 for x in be]
 cc=[(al[r]*be[r][0]/3,al[r]*be[r][1]/3) for r in range(3)]
 C=(F(0),F(0))
 for r,z,t in [(0,1,2),(1,2,0),(2,0,1)]:
  zc=mul(cc[r],conj(cc[z])); C=add(C,(A[t]*zc[0],A[t]*zc[1]))
 c0=sum(B[r]*A[(r+1)%3]*A[(r+2)%3] for r in range(3))
 eta={}
 for r,z in itertools.combinations(range(3),2):
  t=3-r-z
  K=A[r]*A[z]*B[t]+2*A[t]*mul(cc[r],conj(cc[z]))[0]
  eta[(r,z)]=(C[0]-K)/2
 T=np.zeros((50,5),dtype=object);T[:]=F(0)
 ds={(0,1):1,(1,2):2,(0,2):3}
 for start,weights in [(0,A),(35,B)]:
  for j,p in enumerate(pairs):
   r,z=p[0]//2,p[1]//2
   if r==z: T[start+j,0]=weights[r]**2
   else:
    sg=(-1)**(p[0]%2+p[1]%2)
    T[start+j,0]=weights[r]*weights[z]/2
    T[start+j,ds[(r,z)]]=-sg*weights[r]*weights[z]/2
 for j,p in enumerate(triples):
  rs=[i//2 for i in p]
  if len(set(rs))==2:
   r=next(t for t in rs if rs.count(t)==2);z=next(t for t in rs if rs.count(t)==1);t=3-r-z
   T[15+j,0]=A[r]*B[t]
  else:
   sig=[(-1)**(i%2) for i in p]
   T[15+j,0]=(c0-C[0])/2
   for rz,et in eta.items():T[15+j,ds[rz]]=et*sig[rz[0]]*sig[rz[1]]
   T[15+j,4]=-C[1]*np.prod(sig)/2
 return T, (A,B,C,eta)

def constraints(T,extra=True):
 # H p <= k; start nonnegativity, dot range, Gram lower, chirality bound 7/4>sqrt3
 H=[];k=[];labels=[]
 def add(v,z,label):
  v=np.array(v,dtype=object);z=F(z)
  if any(v):H.append(v);k.append(z);labels.append(label)
 for r,t in enumerate(T):add(-t[1:],t[0],('mass',r))
 for j in range(3):
  for sg in [-1,1]:
   v=[F(0)]*4;v[j]=F(sg);add(v,1,('box',j,sg))
 if extra:
  for eps in itertools.product([-1,1],repeat=3):
   if math.prod(eps)==1:add([-F(a) for a in eps]+[F(0)],F(3,2),('gram',eps))
  for sg in [-1,1]:add([F(0),F(0),F(0),F(sg)],F(7,4),('chirality',sg))
 # normalize duplicate same inequality
 unique={}
 for v,z,l in zip(H,k,labels):
  pivot=next(x for x in list(v)+[z] if x);den=abs(pivot)
  key=tuple(x/den for x in v)+(z/den,)
  unique[key]=l
 return np.array([key[:4] for key in unique],dtype=object),np.array([key[4] for key in unique],dtype=object),list(unique.values())

def vertices(H,k):
 Hf=np.array(H,dtype=float);kf=np.array(k,dtype=float)
 r=linprog([0,0,0,0,-1],A_ub=np.c_[Hf,np.linalg.norm(Hf,axis=1)],b_ub=kf,bounds=[(None,None)]*5,method='highs')
 assert r.success and r.x[-1]>0
 hs=HalfspaceIntersection(np.c_[Hf,-kf],r.x[:4])
 vs=[]
 for vv in hs.intersections:
  active=np.flatnonzero(abs(Hf@vv-kf)<1e-7)
  found=None
  for ix in itertools.combinations(active,4):
   M=sp.Matrix(H[list(ix)].tolist())
   if M.det():
    v=M.inv()*sp.Matrix(k[list(ix)].tolist())
    vv=tuple(F(t) for t in v)
    assert all(sum(h[i]*vv[i] for i in range(4))<=z for h,z in zip(H,k))
    found=vv;break
  assert found is not None
  if found not in vs:vs.append(found)
 return vs

def lp(T,p):
 b=np.array(T@np.array([F(1),*p],dtype=object),dtype=float)
 r=linprog(np.zeros(90),A_eq=D,b_eq=b,bounds=(0,None),method='highs')
 return r,b
if __name__=='__main__':
 T,data=coeff();print('data',data,flush=True)
 H,k,labs=constraints(T)
 vs=vertices(H,k);print('constraints',len(k),'vertices',len(vs),flush=True)
 bad=[]
 for i,p in enumerate(vs):
  r,b=lp(T,p)
  if not r.success:
   # derive separator max b.y subject D^T y>=0 and box normalization via L1
   rr=linprog(b,A_ub=-D.T,b_ub=np.zeros(90),bounds=[(-1,1)]*50,method='highs')
   bad.append((p,float(rr.fun),rr.x.tolist()))
 print('bad count',len(bad),'bad first',bad[:2],flush=True)
 os.makedirs('computations/X019',exist_ok=True)
 json.dump({'coeff':[[str(x) for x in r] for r in T], 'H':[[str(x) for x in r] for r in H], 'k':[str(x) for x in k], 'vertices':[[str(x) for x in p] for p in vs], 'bad':[[[str(x) for x in p],err,y] for p,err,y in bad]},open('computations/X019/explore.json','w'),indent=2)
