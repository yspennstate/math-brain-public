"""Independent finite generator checks and an exhaustive drift-inequality audit."""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:
    os.environ[key]='1'
import json, math
from pathlib import Path
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import expm_multiply
ROOT=Path(__file__).resolve().parents[1]

def spins(n):
    states=np.arange(1<<n)
    return ((states[:,None]>>np.arange(n))&1).astype(np.int8)

def generator(n,q):
    eta=spins(n);rows=[];cols=[];vals=[]
    for state in range(1<<n):
        total=0.
        for x in range(n):
            legal=x==0 or x==n-1 or eta[state,x-1]==0 or eta[state,x+1]==0
            if legal:
                rate=q if eta[state,x]==1 else 1-q
                rows.append(state);cols.append(state^(1<<x));vals.append(rate);total+=rate
        rows.append(state);cols.append(state);vals.append(-total)
    return csr_matrix((vals,(rows,cols)),shape=(1<<n,1<<n)),eta

def initial(eta,law,q):
    if law=='equilibrium': return np.prod(np.where(eta==0,q,1-q),axis=1)
    if law=='renewal':
        T=np.array([[0.,1.],[.25,.75]]);alpha=np.array([.2,.8])
        return np.array([alpha[word[0]]*np.prod(T[word[:-1],word[1:]]) for word in eta])
    D=[np.diag([.02,.38]),np.diag([.98,.62])]
    T=np.array([[.97,.03],[.03,.97]])
    out=[]
    for word in eta:
        v=np.array([.5,.5])@D[word[0]]
        for s in word[1:]:v=v@T@D[s]
        out.append(v.sum())
    return np.array(out)

report={'finite_generator':{},'drift':[]}
for law,q in [('renewal',.25),('hmm',.65),('equilibrium',.25)]:
    n=8;G,eta=generator(n,q);mu=initial(eta,law,q);pi=initial(eta,'equilibrium',q)
    detailed=pi[:,None]*G.toarray()
    rowerr=float(np.max(np.abs(G.sum(1))));balance=float(np.max(np.abs(detailed-detailed.T)))
    assert rowerr<1e-12 and balance<1e-12 and abs(mu.sum()-1)<1e-12
    eqerr=float(np.max(np.abs(G.T@pi)));assert eqerr<1e-12
    path=ROOT/'data'/f'validation_{law}_q{int(q*100):03d}.csv'
    raw=np.genfromtxt(path,delimiter=',',names=True);times=np.unique(raw['time']);reps=len(np.unique(raw['rep']))
    obs={'density':(eta==0).mean(1),'pair':((eta[:,:-1]==0)&(eta[:,1:]==0)).mean(1),
         'origin':(eta[:,n//2-1]==0).astype(float),
         'origin_pair':((eta[:,n//2-1]==0)&(eta[:,n//2]==0)).astype(float)}
    stats={};mu_t=mu.copy();last=0.
    expected={key:[] for key in obs}
    for time in times:
        if time>last:mu_t=expm_multiply(G.T*(time-last),mu_t)
        for key in obs:expected[key].append(float(mu_t@obs[key]))
        last=time
    for key in obs:
        values=raw[key].reshape(reps,len(times));mean=values.mean(0);se=values.std(0,ddof=1)/np.sqrt(reps)
        z=np.divide(mean-np.array(expected[key]),se,out=np.zeros_like(se),where=se>1e-14)
        stats[key]={'max_abs_z':float(max(abs(z))),'final_exact':expected[key][-1],
                    'final_simulated':float(mean[-1]),'final_se':float(se[-1])}
        assert max(abs(z))<6
    report['finite_generator'][law]={'q':q,'n':n,'replicates':reps,'row_sum_error':rowerr,
              'detailed_balance_error':balance,'stationarity_error':eqerr,'observables':stats}

# Check every configuration, not just states visited by the simulator.
n=10;x=n//2-1;eta=spins(n);positions=np.arange(n)
D=[]
for word in eta:
    zeros=np.flatnonzero(word==0)
    D.append(min([abs(int(z)-x) for z in zeros]+[x+1,n-x]))
D=np.array(D)
for q in [.2,.49,.5,.51,.65,.9]:
    G,_=generator(n,q)
    for theta in [1.05,1.2,1.5]:
        F=theta**D;lam=(theta-1)*(q/theta-(1-q));b=q*(theta-1)/theta
        residual=G@F+lam*F-b
        maximum=float(max(residual));assert maximum<1e-11
        report['drift'].append({'q':q,'theta':theta,'configurations':1<<n,
                               'lambda':lam,'max_LF_plus_lambdaF_minus_b':maximum})

# Independently check the algebra defining the constants in the cone proof.
for q in [.5001,.51,.65,.9]:
    theta=(1+q/(1-q))/2;a=math.log(theta);lam=(theta-1)*(q/theta-(1-q))
    rho=lam/(8*a);eps=min(.25,rho/(32*math.e))
    assert -lam*(1-eps)+2*a*rho<=-lam/2
    assert rho/2>=8*math.e*eps
report['cone_constants']='algebraic inequalities passed at four q values; proof is symbolic in REPORT.md'
(ROOT/'data'/'verification.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
