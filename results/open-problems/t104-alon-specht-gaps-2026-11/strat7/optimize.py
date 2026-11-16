"""NUMERICAL local optimization on every component pattern; no proof claims."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import json
import numpy as np
from scipy.linalg import helmert
from scipy.optimize import minimize
from terms import terms

rng=np.random.default_rng(717)

def calculate(W,Pi,lm):
    N=len(W); L=np.diag(W.sum(1))-W
    G=lm*(np.eye(N)-np.ones((N,N))/N)-L
    c=2*N/(N-2)
    x1=2*(lm*np.trace(G)-np.sum(G*G))
    x2=c*np.sum(Pi*G*G)
    x3=(1-lm)/(N-2)*(2*np.trace(G)-c*np.diag(Pi)@np.diag(G))
    p=np.diag(Pi); g=np.diag(G)
    y=np.sum(W*(p[:,None]+p[None,:]-2*Pi)*(g[:,None]+g[None,:]-2*G))
    return np.array([x1,x2,x3,y])

def make_double(m,extra):
    d=m-1; H=helmert(m).T; ids=np.triu_indices(d,1)
    k=len(ids[0]); r=m-3
    def build(x):
        K=np.zeros((d,d)); K[ids]=x[:k]; K-=K.T
        U=H@np.linalg.solve(np.eye(d)+K,np.eye(d)-K)[:,:r]
        A=np.ones((m,m))/m+(U*x[k:k+r])@U.T
        np.fill_diagonal(A,0)
        W=np.zeros((6,6)); W[:m,:m]=A
        if extra: W[m,m+1]=W[m+1,m]=x[-1]/2
        mass=W.sum()/2
        P=np.zeros((6,6)); P[:m,:m]=np.eye(m)-np.ones((m,m))/m-U@U.T
        return W/mass,P,1/mass
    bounds=[(-10,10)]*k+[(1e-7,1-1e-7)]*r+([(1e-7,1-1e-7)] if extra else [])
    def start(): return np.r_[rng.normal(size=k),rng.uniform(.05,.3,size=r),[rng.uniform(.05,.9)] if extra else []]
    return build,bounds,start

def make_split(part,carriers):
    sizes=[m*(m-1)//2 for m in part]; offsets=np.cumsum([0]+sizes)
    def build(x):
        W=np.zeros((6,6)); P=np.zeros((6,6)); at=0
        for j,m in enumerate(part):
            if m>1:
                a=np.zeros((m,m)); ids=np.triu_indices(m,1)
                a[ids]=x[offsets[j]:offsets[j+1]]; a+=a.T
                ev,U=np.linalg.eigh(np.diag(a.sum(1))-a)
                a/=ev[-1]
                if j in carriers: P[at:at+m,at:at+m]=np.outer(U[:,-1],U[:,-1])
                else:a*=x[-1]
                W[at:at+m,at:at+m]=a
            at+=m
        mass=W.sum()/2
        return W/mass,P,1/mass
    noncar=any(m>1 and j not in carriers for j,m in enumerate(part))
    bounds=[(1e-7,1)]*offsets[-1]+([(1e-7,1-1e-7)] if noncar else [])
    def start():return rng.uniform(.01,1,size=len(bounds))
    return build,bounds,start

def main(starts=80):
    cases=[('5+1 both5',make_double(5,False)),('4+2 both4',make_double(4,True)),('4+1+1 both4',make_double(4,False))]
    for part,car in [((4,2),(0,1)),((3,3),(0,1)),((3,2,1),(0,1))]:
        cases.append(('+'.join(map(str,part))+' split',make_split(part,car)))
    output=[]
    for name,(build,bounds,start) in cases:
        best=None
        def objective(x):
            W,P,lm=build(x); v=calculate(W,P,lm); den=sum(v[:3])
            return (den-v[3])/den if den>1e-13 else 2
        def constraint(x):
            W,P,lm=build(x)
            return W[np.triu_indices(6,1)]
        for j in range(starts):
            ans=minimize(objective,start(),bounds=bounds,constraints=[dict(type='ineq',fun=constraint)],method='SLSQP',options=dict(maxiter=400,ftol=1e-11))
            if min(constraint(ans.x)) < -1e-8:continue
            W,P,lm=build(ans.x); v=calculate(W,P,lm)
            D,*ref=terms(W)
            if D!=2 or max(abs(v-np.array(ref)))>1e-7: continue
            q=objective(ans.x)
            if best is None or q<best['quotient']:
                best=dict(quotient=float(q),W=W.tolist(),terms=v.tolist(),params=ans.x.tolist(),success=bool(ans.success))
                print('NUMERICAL',name,j,q,flush=True)
            if q < -1e-7:
                output.append(dict(name=name,best=best)); json.dump(output,open('optimized.json','w'),indent=2)
                print('NUMERICAL NEGATIVE: STOP',flush=True);return
        output.append(dict(name=name,best=best));json.dump(output,open('optimized.json','w'),indent=2)
if __name__=='__main__':main()
