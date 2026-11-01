"""Exploratory floating point search; never a proof certificate."""
import json
from pathlib import Path
from itertools import combinations, product
import numpy as np
from scipy.linalg import eigvalsh, qr

ROOT=Path(__file__).resolve().parent
rng=np.random.default_rng(650915)
n=4
edges=list(combinations(range(n),2))
bits=np.array([[s>>i&1 for i in range(n)] for s in range(1<<n)])
bas=[]
for i in range(n):
 E=np.zeros((n,n));E[i,i]=1;bas.append(E)
for i,j in edges:
 E=np.zeros((n,n));E[i,j]=E[j,i]=1;bas.append(E)
bas=np.array(bas)
fb=np.column_stack([np.ones(1<<n),bits]+[bits[:,i]*bits[:,j] for i,j in edges])

def data(K,p0=None,C=None):
 p=[];score=[];acc=np.zeros((10,10))
 for s,b in enumerate(bits):
  M=K-np.diag(1-b);R=np.linalg.inv(M)
  ps=(-1)**sum(1-b)*np.linalg.det(M) if p0 is None else p0[s]
  if ps<=0: raise ValueError('nonpositive mass')
  v=np.einsum('ij,bji->b',R,bas)
  E=np.einsum('ij,bjk->bik',R,bas)
  second=np.outer(v,v)-np.einsum('bij,cji->bc',E,E)
  acc-=ps*np.log(ps)*second
  p.append(ps);score.append(v)
 p=np.array(p);score=np.array(score);z=np.sqrt(p)[:,None]*score
 if C is not None:
  acc=np.zeros((10,10));acc[:4,:4]=C
  for k,(i,j) in enumerate(edges):acc[4+k,4+k]=-2*C[i,j]
 F=z.T@z;ortho=qr(np.sqrt(p)[:,None]*fb,mode='economic')[0]
 F2=z.T@ortho@ortho.T@z
 count=bits.sum(axis=1);Fc=np.zeros((10,10))
 for k in range(5):
  b=count==k;dq=p[b]@score[b];Fc+=np.outer(dq,dq)/sum(p[b])
 return p,score,acc,F,F2,Fc

def tree_info(p,score,root,child,grand):
 F=np.zeros((10,10));leaves=[]
 for a,b in product(range(2),repeat=2):
  j=child[a];k=grand[2*a+b]
  for c in range(2):
   mask=(bits[:,root]==a)&(bits[:,j]==b)&(bits[:,k]==c)
   ids=np.where(mask)[0].tolist();leaves.append(ids)
   dq=p[mask]@score[mask];F+=np.outer(dq,dq)/sum(p[mask])
 return F,leaves

def best_tree(p,score,acc):
 best=(-1e100,None)
 for root in range(4):
  others=[i for i in range(4) if i!=root]
  for child in product(others,repeat=2):
   allowed=[[i for i in others if i!=child[a]] for a,b in product(range(2),repeat=2)]
   for grand in product(*allowed):
    F,leaves=tree_info(p,score,root,child,grand)
    e=eigvalsh(F-acc)[0]
    if e>best[0]:best=(e,(root,child,grand,leaves,F))
 return best

def cauchy(x,r):
 L=2*r[:,None]*r[None,:]/(x[:,None]+x[None,:]);K=np.linalg.solve(np.eye(4)+L,L)
 C=np.zeros((4,4));lp=bits@np.log(r*r/x)
 for i,j in edges:
  c=2*np.log((x[i]+x[j])/abs(x[i]-x[j]));C[i,j]=C[j,i]=c;lp-=c*bits[:,i]*bits[:,j]
 p=np.exp(lp-max(lp));p/=sum(p)
 return K,p,C

def main():
 best=0
 for it in range(30000):
  kind=it%3
  if kind==0:
   x=np.sort(np.exp(rng.uniform(0,4,4)));r=np.exp(rng.uniform(-1,8,4))
   K,p,C=cauchy(x,r)
  elif kind==1:
   # Rational K with prescribed eigenvalue scale, rounded away from boundary.
   V=np.linalg.qr(rng.normal(size=(4,4)))[0]
   lam=1/(1+np.exp(-rng.uniform(-9,9,4)))
   K=V@np.diag(lam)@V.T;p=C=None
  else:
   B=rng.integers(-8,9,size=(4,4));L=B@B.T/10**rng.uniform(-2,2)
   K=np.linalg.solve(np.eye(4)+L,L);p=C=None
  try:p,s,acc,F,F2,Fc=data(K,p,C)
  except (np.linalg.LinAlgError,ValueError):continue
  e2=eigvalsh(F2-acc)[0];ef=eigvalsh(F-acc)[0]
  if e2<-.01 and ef>.01:
   e,tree=best_tree(p,s,acc)
   print('CANDIDATE',it,kind,'degree2',e2,'full',ef,'tree',e,flush=True)
   rec=dict(it=it,kind=kind,K=K.tolist(),p=p.tolist(),acc=acc.tolist(),e2=e2,ef=ef,tree_e=e)
   if kind==0:rec.update(x=x.tolist(),r=r.tolist())
   if tree is not None:
    root,child,grand,leaves,FT=tree
    rec.update(root=root,child=child,grand=grand,leaves=leaves)
    # Also retain degree-two features plus the adaptively selected leaves.
    f=np.column_stack([fb]+[np.isin(np.arange(16),l).astype(float) for l in leaves])
    u,sv,_=np.linalg.svd(np.sqrt(p)[:,None]*f,full_matrices=False)
    u=u[:,sv>1e-10];z=np.sqrt(p)[:,None]*s
    ep=eigvalsh(z.T@u@u.T@z-acc)[0];rec['aug_e']=ep
   path=ROOT/f'candidate_{it}.json';path.write_text(json.dumps(rec,indent=2))
   if e>.001:
    print('FOUND',path,flush=True);return
  if it%1000==0:print('progress',it,'degree2',e2,flush=True)

if __name__=='__main__':main()
