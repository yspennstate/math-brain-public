"""Multistart SLSQP on all atom probabilities for n<=6. Local lower bounds only."""
import json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from common import tables,quantities,check

def search(n,restarts=20):
    pc,z,L,fac,meta=tables(n); m=1<<n
    rr=np.array([r for r,k in meta]); Z=z[rr]
    rng=np.random.default_rng(10010+n)
    def obj(x,grad=False):
        up=z@x; us=np.maximum(up,1e-250)
        A=-np.dot(x,np.log(us))/np.log(2); I=np.dot(x,pc)
        if I<1e-12: return np.zeros(m) if grad else 0.
        if not grad: return -A/I
        dA=-(np.log(us)+z.T@(x/us))/np.log(2)
        return -(dA*I-A*pc)/I**2
    def con(x):
        up=np.maximum(Z@x,0)
        # Divide by the coefficient to keep huge k rows well scaled.
        return up**1.5-(L@x)/fac
    def jac(x): return 1.5*np.sqrt(np.maximum(Z@x,0))[:,None]*Z-L/fac[:,None]
    constraints=[{'type':'eq','fun':lambda x: x.sum()-1,'jac':lambda x:np.ones(m)},
                 {'type':'ineq','fun':con,'jac':jac}]
    best=-1.; out=None; attempts=[]
    for j in range(restarts):
        if j==0:
            p=.25; x=p**pc*(1-p)**(n-pc)
        elif j==1:
            x=np.ones(m)/m
        elif j==2:
            x=np.zeros(m); x[-1]=.2; x[1:]=.8/(m-1); x/=x.sum()
        else:
            # A large top atom makes starts feasible often; other starts probe boundary faces.
            x=rng.dirichlet(np.full(m,.4)); x=.6*x; x[-1]+=.4
        sol=minimize(obj,x,jac=lambda x:obj(x,True),method='SLSQP',bounds=[(0,1)]*m,
                     constraints=constraints,options={'maxiter':700,'ftol':1e-11})
        x=np.maximum(sol.x,0); x/=x.sum(); c=check(x,n)
        attempts.append({'success':bool(sol.success),'message':str(sol.message),'A_I':c['A_I'],'violation':c['max_violation'],'nit':int(sol.nit)})
        if c['max_violation']<=2e-8 and c['A_I']>best:
            best=c['A_I']; out={'n':n,'best':c,'mu':x.tolist(),'attempt':j}
        if j%5==0: print('progress',n,j,best,flush=True)
    return {**out,'attempts':attempts}

if __name__=='__main__':
    start=time.time(); results=[]
    for n in range(1,7):
        result=search(n,24 if n<=4 else 16)
        results.append(result)
        Path('small_output.json').write_text(json.dumps({'results':results,'seconds':time.time()-start,'seed':10010},indent=2)+'\n')
        print('DONE',n,result['best'],flush=True)
