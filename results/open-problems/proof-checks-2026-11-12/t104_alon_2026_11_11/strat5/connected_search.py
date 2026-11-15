"""NUMERICAL: local searches with a positive floor on all ten weights."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse, json, time
import numpy as np
from scipy.optimize import minimize
from stratum import BASIS, closed, matrices, ratio, tmax

def frame(theta):
    z=np.zeros((4,4))
    for x,(i,j) in zip(theta,[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]):
        z[i,j]=x
        z[j,i]=-x
    return BASIS@np.linalg.solve(np.eye(4)-z,np.eye(4)+z)[:,:2]

def run(floor, starts, seed):
    rng=np.random.default_rng(seed)
    def decode(x): return x[6],x[6]*x[7],frame(x[:6])
    def fun(x):
        terms=closed(*decode(x))
        return 1-terms[3]/max(sum(terms[:3]),1e-20)
    def cons(x):
        a,b,u=decode(x)
        lam,_,_,_,z=matrices(a,b,u)
        return np.r_[z-floor,lam-a,sum(closed(a,b,u)[:3])-1e-9]
    records=[]
    best=None
    tic=time.monotonic()
    # The previous exact sparse family, connected by adding the complete graph.
    ell=6.394205213654777
    delta=ell*ell-ell-3
    ww=np.zeros((5,5))
    for i,j,v in ((0,1,(ell-2)/delta),(0,3,(ell-2)/delta),
                  (0,2,ell*(ell-3)/(2*delta)),(1,3,(ell-2)*(ell-1)/(2*delta))):
        ww[i,j]=ww[j,i]=v
    ll=np.diag(ww.sum(axis=1))-ww
    vals,vecs=np.linalg.eigh(ll)
    target=np.column_stack(((np.array([1.,1.,1.,1.,-4.])/np.sqrt(20)),vecs[:,2]))
    from scipy.optimize import least_squares
    for trial in range(10):
        fit=least_squares(lambda th:(frame(th)-target).ravel(),rng.normal(size=6),max_nfev=500,
                          bounds=(-10.,10.),ftol=1e-13,xtol=1e-13,gtol=1e-13)
        if np.max(np.abs(frame(fit.x)-target))<1e-8: break
    assert np.max(np.abs(frame(fit.x)-target))<1e-8
    sparse_x=np.r_[fit.x,(1-10*floor)*vals[-1],(vals[-1]-vals[2])/vals[-1]]
    for k in range(starts):
        theta=rng.normal(size=6)
        r=rng.uniform(.01,1)
        a=.9*(1-10*floor)*tmax(r,frame(theta))
        x=np.r_[theta,a,r]
        if k==0:
            x=sparse_x.copy()
        elif k%3==0 and best is not None:
            x=np.array(best['x'])+rng.normal(size=8)*.05
            x[6:]=np.clip(x[6:],1e-5,.999)
        res=minimize(fun,x,method='SLSQP',bounds=[(-60,60)]*6+[(1e-7,1),(1e-7,1)],
                     constraints={'type':'ineq','fun':cons},options={'ftol':2e-13,'maxiter':350})
        a,b,u=decode(res.x)
        terms=closed(a,b,u)
        rec=dict(k=k,success=bool(res.success),ratio=float(ratio(terms)),
                 residual=float(min(cons(res.x))),a=float(a),b=float(b),
                 x=res.x.tolist(),frame=u.tolist(),weights=matrices(a,b,u)[4].tolist(),
                 terms=terms.tolist(),direct_terms=None)
        records.append(rec)
        if rec['residual']>=-2e-10 and np.isfinite(rec['ratio']) and sum(terms[:3])>1e-8:
            if best is None or rec['ratio']<best['ratio']:
                best=rec
                print('NUMERICAL: floor',floor,'start',k,'best',best['ratio'],'residual',best['residual'],flush=True)
        if (k+1)%10==0:
            print('NUMERICAL: progress',k+1,'seconds',round(time.monotonic()-tic,2),flush=True)
    if best:
        from stratum import direct
        best['direct_terms']=direct(best['a'],best['b'],np.array(best['frame'])).tolist()
    result=dict(floor=floor,starts=starts,seed=seed,seconds=time.monotonic()-tic,best=best,records=records)
    with open('connected_floor_'+str(floor)+'.json','w') as out: json.dump(result,out,indent=2)
    print('NUMERICAL: FINAL',json.dumps({k:v for k,v in result.items() if k!='records'}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--starts',type=int,default=60)
    p.add_argument('--seed',type=int,default=131113)
    args=p.parse_args()
    for j,floor in enumerate((1e-3,1e-6)):
        run(floor,args.starts,args.seed+j)
