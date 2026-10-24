"""Attempt to break Rossman's auxiliary spectral conjectures, not Sidorenko.

Optimizes either tail weak-majorization or signed Schatten norm monotonicity.
All numerical output is exploratory, never an exact mathematical certificate.
"""
import argparse,json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize

def transfer(A,t):
    return ((A[:,:,None,None]*A[None,None,:,:])**t *
            (A[:,None,None,:]*A[None,:,:,None])**(1-t)).reshape(len(A)**2,len(A)**2)

def objective(z,n,t,kind,k,p,q):
    ix=np.triu_indices(n);A=np.empty((n,n));A[ix]=np.exp(z);A[ix[::-1]]=A[ix]
    M=transfer(A,t);lam,U=np.linalg.eigh(M);N=n*n
    if kind=='majorization':
        weights=np.zeros(N);weights[-k:-1]+=1;weights[:k-1]+=1
        num=weights@lam;den=lam[-1];value=num/den
        deriv=weights/den;deriv[-1]-=num/den**2
    else:
        Sp=np.sum(np.sign(lam)*abs(lam)**p);Sq=np.sum(np.sign(lam)*abs(lam)**q)
        if Sp<=0 or Sq<=0:return 1e4,np.zeros_like(z)
        # The conjecture requires this log norm ratio to be <=0; minimize its negative.
        value=np.log(Sp)/p-np.log(Sq)/q
        deriv=abs(lam)**(p-1)/Sp-abs(lam)**(q-1)/Sq
    L=(U*deriv)@U.T;T=(L*M).reshape(n,n,n,n)
    grad=t*(T.sum(axis=(2,3))+T.sum(axis=(0,1)))
    grad+=(1-t)*(T.sum(axis=(1,2))+T.sum(axis=(0,3)).T)
    out=grad[ix].copy();off=ix[0]!=ix[1];out[off]+=grad[ix[::-1]][off]
    return value,out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=5);ap.add_argument('--runs',type=int,default=100)
    ap.add_argument('--t',type=float,default=1/3);ap.add_argument('--kind',default='majorization')
    ap.add_argument('--k',type=int,default=2);ap.add_argument('--p',type=float,default=1);ap.add_argument('--q',type=float,default=1.25)
    ap.add_argument('--seed',type=int,default=73913);ap.add_argument('--output',required=True)
    args=ap.parse_args();rng=np.random.default_rng(args.seed);records=[];best=None
    for r in range(args.runs):
        z=rng.normal(0,[.3,1,2,4,8][r%5],args.n*(args.n+1)//2)
        result=minimize(objective,z,args=(args.n,args.t,args.kind,args.k,args.p,args.q),jac=True,
                        method='L-BFGS-B',bounds=[(-12,12)]*len(z),options={'maxiter':500,'ftol':1e-13,'gtol':1e-9})
        record={'run':r,'value':float(result.fun),'iterations':int(result.nit),'success':bool(result.success)}
        records.append(record)
        if best is None or result.fun<best['value']:
            ix=np.triu_indices(args.n);A=np.empty((args.n,args.n));A[ix]=np.exp(result.x);A[ix[::-1]]=A[ix];A/=np.linalg.norm(A)
            M=transfer(A,args.t);best=record|{'A_Frobenius_one':A.tolist(),'eigenvalues':np.linalg.eigvalsh(M).tolist()}
            print(best['run'],best['value'],flush=True)
        Path(args.output).write_text(json.dumps({'status':'numerical exploration only','args':vars(args),'best':best,'records':records},indent=2))

if __name__=='__main__':main()
