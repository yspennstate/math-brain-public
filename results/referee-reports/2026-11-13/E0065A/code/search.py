"""Reproducible constrained search for QSO two-cycles / distinct fixed points.
Only numerical evidence; exact family certificates are separate.
"""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:
 os.environ[key]='1'
import json, time, resource
from pathlib import Path
import numpy as np
from scipy.optimize import minimize, Bounds, LinearConstraint

class Model:
 def __init__(self,m,gap,kind):
  self.m=m; self.gap=gap; self.kind=kind
  self.pairs=[(i,j) for i in range(m) for j in range(i,m)]
  self.np=len(self.pairs)*m; self.n=self.np+2*m+1
  self.xs=slice(self.np,self.np+m);self.ys=slice(self.np+m,self.np+2*m)
  # coefficients of all linear equality and inequality constraints
  self.E=np.zeros((len(self.pairs)+2,self.n))
  for r in range(len(self.pairs)): self.E[r,r*m:(r+1)*m]=1
  self.E[-2,self.xs]=1;self.E[-1,self.ys]=1
  self.L=np.zeros((self.np+1,self.n)); self.L[:self.np,:self.np]=np.eye(self.np);self.L[:self.np,-1]=-1
  self.L[-1,self.np]=1;self.L[-1,self.np+m]=-1
  self.lb=np.r_[np.zeros(self.np),gap]
 def unpack(self,z):return z[:self.np].reshape(-1,self.m),z[self.xs],z[self.ys],z[-1]
 def weights(self,x): return np.array([(1 if i==j else 2)*x[i]*x[j] for i,j in self.pairs])
 def dw(self,x):
  W=np.zeros((len(self.pairs),self.m))
  for r,(i,j) in enumerate(self.pairs):
   if i==j: W[r,i]=2*x[i]
   else: W[r,i]=2*x[j];W[r,j]=2*x[i]
  return W
 def fun(self,z):
  P,x,y,l=self.unpack(z)
  u,v=(y,x) if self.kind=='cycle' else (x,y)
  return np.r_[(self.weights(x)@P-u)[:-1],(self.weights(y)@P-v)[:-1]]
 def jac(self,z):
  m=self.m;P,x,y,l=self.unpack(z);J=np.zeros((2*(m-1),self.n))
  for block,w in enumerate((x,y)):
   sl=slice(block*(m-1),(block+1)*(m-1))
   J[sl,:self.np]=np.kron(self.weights(w).reshape(1,-1),np.eye(m)[:-1,:])
   src=self.xs if block==0 else self.ys
   dst=(self.ys if block==0 else self.xs) if self.kind=='cycle' else src
   J[sl,src]=P[:,:-1].T@self.dw(w)
   J[sl,dst]-=np.eye(m)[:-1,:]
  return J
 def seed(self,rng,idx):
  m=self.m
  if idx%4==0:
   T=(2*(m+1)+np.sqrt(4*(m+1)+m*m*self.gap*self.gap))/(4*(m+1)-m*self.gap*self.gap)
   l=(1-T)/m; t=T; z=1/t-1; ss=2-1/t
   x=np.r_[(ss+self.gap)/2,z-(m-3)*l,(ss-self.gap)/2,np.full(m-3,l)]
   y=x.copy();y[0],y[2]=x[2],x[0]
   P=np.full((len(self.pairs),m),l)
   for r,(i,j) in enumerate(self.pairs):
    if i==0 and j==2:k=1
    elif i==0 or j==0:k=(2 if self.kind=='cycle' else 0)
    elif i==2 or j==2:k=(0 if self.kind=='cycle' else 2)
    else:k=1
    P[r,k]+=t
  elif idx%4==1:
   l=.8*((m+1-np.sqrt(m*m+m+1))/(2*m));t=1-m*l
   # f(s)=l+t(1-s)^2, lift other types uniformly.
   P=np.zeros((len(self.pairs),m))
   for r,(i,j) in enumerate(self.pairs):
    P[r,0]=l+t*float(i!=0 and j!=0)
    P[r,1:]=(1-P[r,0])/(m-1)
   disc=4*t*(1-l)-3
   x0=1-(1-np.sqrt(disc))/(2*t);y0=1-(1+np.sqrt(disc))/(2*t)
   x=np.r_[x0,np.full(m-1,(1-x0)/(m-1))];y=np.r_[y0,np.full(m-1,(1-y0)/(m-1))]
  else:
   l=rng.uniform(.01,.10)
   P=l+(1-m*l)*rng.dirichlet(np.full(m,.15 if idx%3==1 else 1.),len(self.pairs))
   x=rng.dirichlet(np.ones(m));y=rng.dirichlet(np.ones(m))
   if x[0]<y[0]:x,y=y,x
  return np.r_[P.ravel(),x,y,l]
 def diagnostics(self,z):
  P,x,y,l=self.unpack(z);T=np.zeros((self.m,self.m,self.m))
  for p,(i,j) in zip(P,self.pairs):T[i,j]=T[j,i]=p
  D=2*np.einsum('ijk,j->ki',T,x)
  R=D[:-1,:-1]-D[:-1,-1:]
  return {'lambda':float(l),'min_P':float(P.min()),'equality_error':float(max(np.max(np.abs(self.fun(z))),np.max(np.abs(np.einsum('ij,j->i',self.E,z)-1)))),'gap':float(x[0]-y[0]),'distance':float(np.linalg.norm(x-y,1)),'P':P.tolist(),'pairs':self.pairs,'x':x.tolist(),'y':y.tolist(),'eigenvalues_at_x':[[float(v.real),float(v.imag)] for v in np.linalg.eigvals(R)]}

def run(starts=24,gaps=(.02,.002,.0002)):
 rng=np.random.default_rng(651113);results=[];start=time.time()
 for m in (3,4):
  for kind in ('cycle','fixed'):
   best=None
   for gap in gaps:
    M=Model(m,gap,kind)
    cons=[LinearConstraint(M.E,1,1),LinearConstraint(M.L,M.lb,np.inf),{'type':'eq','fun':M.fun,'jac':M.jac}]
    for idx in range(starts):
     z0=np.array(best['z']) if best is not None and idx==0 else M.seed(rng,idx)
     res=minimize(lambda z:-z[-1],z0,jac=lambda z:np.r_[np.zeros(M.n-1),-1.],constraints=cons,bounds=Bounds(np.zeros(M.n),np.r_[np.ones(M.n-1),1/m]),method='SLSQP',options={'ftol':2e-12,'maxiter':450})
     d=M.diagnostics(res.x);d.update(m=m,kind=kind,requested_gap=gap,success=bool(res.success),message=res.message,start=idx,iterations=res.nit,z=res.x.tolist())
     feasible=d['equality_error']<2e-8 and np.min(np.einsum('ij,j->i',M.L,res.x)-M.lb)>-2e-8 and np.min(res.x)>-2e-8
     d['feasible']=bool(feasible); results.append(d)
     if feasible and (best is None or d['lambda']>best['lambda']):best=d;print('BEST',m,kind,gap,idx,d['lambda'],d['distance'],d['equality_error'],flush=True)
     Path('data/search_results.json').write_text(json.dumps({'seed':651113,'starts_per_gap':starts,'elapsed_seconds':time.time()-start,'runs':results},indent=2))
   print('FINISHED',m,kind,'best',None if best is None else best['lambda'],flush=True)
 print('elapsed',time.time()-start,'rss',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,flush=True)
if __name__=='__main__':
 import sys
 run(int(sys.argv[1]) if len(sys.argv)>1 else 24)
