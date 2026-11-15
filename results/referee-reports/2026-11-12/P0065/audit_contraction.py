"""Finite-depth tests on compactly represented trees, at most 20 levels.

Sharing is storage only: unfold the layered DAG to obtain a locally finite tree.
This tests treewise inequalities; samples are not claimed to be independent GW trees.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name] = '1'
import signal
signal.alarm(280)
import json
import numpy as np


def calc(topology, lam, depth, derivative=True):
    lam = np.asarray(lam)[:,None]
    p = len(topology[0][0])
    b = np.ones((len(lam),p))
    db = np.zeros_like(b)
    for lev in range(depth-1,-1,-1):
        n, children = topology[lev]
        mask = np.arange(children.shape[1])[None,:] < n[:,None]
        s = (b[:,children]*mask).sum(axis=2)
        ds = (db[:,children]*mask).sum(axis=2)
        db = (lam*ds-s)/(lam+s)**2
        b = s/(lam+s)
    return np.log(b), db/b, db


def main():
    results=[]
    for k in (1,2,3):
        rng = np.random.default_rng(8800+k)
        p=384
        top = [(rng.choice([k,k+1,k+3],p),rng.integers(p,size=(p,k+3))) for _ in range(20)]
        for rho in (.3,.6,.9):
            r=k*rho
            c=1-rho
            M=k/(k-r)**2
            K=(1+3*r*M)/(k*c*c)
            grid=np.linspace(0,r,17)
            prevx=np.zeros((len(grid),p)); prevy=prevx.copy()
            rows=[]; fd_error=0.; max_db=0.
            for j in range(1,21):
                x,y,db=calc(top,grid,j)
                dx=float(np.max(np.abs(x-prevx)))
                dy=float(np.max(np.abs(y-prevy)))
                eta_bound=rho**(j-1)*(1/(k-r)+(j-1)*K)
                assert dx<=rho**j+2e-14
                assert dy<=eta_bound+2e-14
                rows.append(dict(j=j,delta=dx,delta_bound=rho**j,eta=dy,eta_bound=eta_bound))
                max_db=max(max_db,float(np.max(np.abs(db))))
                if j in (12,16,20):
                    h=1e-5
                    xp,_,_=calc(top,grid+h,j)
                    xm,_,_=calc(top,grid-h,j)
                    fd_error=max(fd_error,float(np.max(np.abs(y-(xp-xm)/(2*h)))))
                prevx,prevy=x,y
            result=dict(k=k,r=r,rho=rho,M=M,K=K,roots=p,grid=len(grid),rows=rows,
                        max_db=max_db,max_db_depth20=float(np.max(np.abs(db))),fd_error=fd_error,
                        max_delta_ratio=max(row['delta']/row['delta_bound'] for row in rows),
                        max_eta_ratio=max(row['eta']/row['eta_bound'] for row in rows))
            results.append(result)
            print({key:val for key,val in result.items() if key!='rows'},flush=True)
    with open('contraction_results.json','w') as f:
        json.dump(results,f,indent=2)


if __name__=='__main__':
    main()
