"""Optimise the coefficient floor subject to a fixed point with spectral radius >=1.
Finite multistart search, not a global certificate.
"""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
import json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize, Bounds, LinearConstraint
from search import Model

def run(starts=24):
 rng=np.random.default_rng(651114);allruns=[];start=time.time()
 for m in (3,4):
  M=Model(m,.002,'cycle');pn=M.np;n=pn+m+1
  E=M.E[:-1,:n].copy();E=E[:-1] if E.shape[0]>len(M.pairs)+1 else E
  # Rebuild to avoid depending on the two-point model's variable positions.
  E=np.zeros((len(M.pairs)+1,n))
  for r in range(len(M.pairs)):E[r,r*m:(r+1)*m]=1
  E[-1,pn:pn+m]=1
  L=np.zeros((pn,n));L[:pn,:pn]=np.eye(pn);L[:pn,-1]=-1
  def unpack(w):return w[:pn].reshape(-1,m),w[pn:pn+m],w[-1]
  def eq(w):
   P,x,l=unpack(w);return (M.weights(x)@P-x)[:-1]
  def jac(w):
   P,x,l=unpack(w);J=np.zeros((m-1,n));J[:,:pn]=np.kron(M.weights(x).reshape(1,-1),np.eye(m)[:-1,:]);J[:,pn:pn+m]=P[:,:-1].T@M.dw(x)-np.eye(m)[:-1,:];return J
  def ev(w):
   P,x,l=unpack(w);D=P.T@M.dw(x);return np.linalg.eigvals(D[:-1,:-1]-D[:-1,-1:])
  def rad(w):return max(abs(ev(w)))-1
  best=-1
  for idx in range(starts):
   if idx%4==0:
    tc=(1+1/np.sqrt(m+1))/2;l=(1-tc)/m;z=1/tc-1
    x=np.r_[(1-z)/2,z-(m-3)*l,(1-z)/2,np.full(m-3,l)]
    PP=M.seed(rng,0)[:pn].reshape(-1,m);Q=(PP-PP.min())/(1-m*PP.min());P=l+tc*Q
   else:
    l=rng.uniform(.005,.09);P=l+(1-m*l)*rng.dirichlet(np.full(m,.25),len(M.pairs));x=rng.dirichlet(np.ones(m))
   w=np.r_[P.ravel(),x,l]
   res=minimize(lambda w:-w[-1],w,jac=lambda w:np.r_[np.zeros(n-1),-1.],method='SLSQP',bounds=Bounds(np.zeros(n),np.r_[np.ones(n-1),1/m]),constraints=[LinearConstraint(E,1,1),LinearConstraint(L,0,np.inf),{'type':'eq','fun':eq,'jac':jac},{'type':'ineq','fun':rad}],options={'maxiter':350,'ftol':1e-11})
   P,x,l=unpack(res.x);evals=ev(res.x)
   # Scalar sums verify equality separately from BLAS products.
   scalarV=np.array([sum(float(M.weights(x)[r])*float(P[r,k]) for r in range(len(M.pairs))) for k in range(m)])
   err=max(np.max(abs(scalarV-x)),np.max(abs(P.sum(axis=1)-1)),abs(x.sum()-1))
   feasible=bool(err<1e-7 and P.min()>=l-1e-8 and rad(res.x)>=-1e-7)
   d={'m':m,'start':idx,'lambda':float(l),'min_P':float(P.min()),'rho':float(max(abs(evals))),'eigenvalues':[[float(v.real),float(v.imag)] for v in evals],'equality_error_scalar':float(err),'feasible':feasible,'success':bool(res.success),'message':res.message,'P':P.tolist(),'x':x.tolist()}
   allruns.append(d)
   if feasible and l>best:best=l;print('BEST',m,idx,l,d['eigenvalues'],err,flush=True)
   Path('data/stability_search.json').write_text(json.dumps({'seed':651114,'runs':allruns,'elapsed_seconds':time.time()-start},indent=2))
  print('FINISHED',m,best,flush=True)
 print('seconds',time.time()-start,flush=True)
if __name__=='__main__':run()
