"""Independent finite-time checks; no submitted code imported or read.
Run: OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/check_backbone.py
Inherited process priority must be nice >=10. One vectorized worker, <100 MB.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
os.environ['VECLIB_MAXIMUM_THREADS']='1'
import csv, ctypes, json, math, time
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
libc=ctypes.CDLL(None, use_errno=True)
ctypes.set_errno(0)
nice=libc.getpriority(0,0)
assert ctypes.get_errno()==0 and nice>=10, (nice,ctypes.get_errno())

def exact(heights,T):
    # All vertices reachable in T steps. Dropped mass can only cross the
    # frontier at step T+1. Degrees are correct at every vertex used
    # for a departure through time T; artificial tips occur only too far away
    # to be left before the horizon.
    R=T
    h=np.minimum(np.asarray(heights,dtype=np.int64),T)
    p=np.zeros((2*R+1,T+1)); p[R,0]=1.
    yy=np.arange(T+1)[None,:]
    valid=yy<=h[:,None]
    degree=np.where(yy==0, 2+(h[:,None]>0), np.where(yy<h[:,None],2,1))
    degree=np.where(valid,degree,1)
    out=[]
    for t in range(T+1):
        assert abs(p.sum()-1)<2e-13
        assert p[:,0][(np.arange(-R,R+1)-t)%2!=0].sum()<1e-14
        out.append(float(p[:,0]@p[:,0]))
        if t==T: break
        flow=p/degree
        q=np.zeros_like(p)
        q[1:,0]+=flow[:-1,0]; q[:-1,0]+=flow[1:,0]
        q[:,1:]+=flow[:,:-1]*(yy[:,:-1]<h[:,None])
        q[:,:-1]+=flow[:,1:]
        p=q
    return out

def heights_for(rng,gamma,T):
    # H=floor(U^(-1/gamma)) >=1 has P(H>t)~t^-gamma.
    # Values above T+1 are indistinguishable up to the horizon, so only
    # their representation is clipped; no visited tooth tip is shortened.
    exponent=np.minimum(-np.log(rng.random(2*T+1))/gamma,math.log(T+1))
    return np.floor(np.exp(exponent)+1e-10).astype(np.int64)

def monte(heights,T,M,rng,checkpoints):
    x=np.zeros(M,dtype=np.int64); y=x.copy(); rows=[]
    for t in range(1,T+1):
        old_y=y.copy()
        z=old_y==0
        up=(~z)&(old_y<heights[x+T])
        tip=(~z)&(~up)
        moves=rng.integers(0,3,int(z.sum()))
        x[z]+=np.where(moves==0,-1,np.where(moves==1,1,0))
        y[z]=(moves==2)
        y[up]+=2*rng.integers(0,2,int(up.sum()))-1
        y[tip]-=1
        if t in checkpoints:
            assert np.all((x+y-t)%2==0)
            a=np.bincount(x[y==0]+T,minlength=2*T+1).astype(np.float64)
            # U-statistic: independent distinct walkers in one shared env.
            # sum count^2/M^2 would have a substantial self-pair bias.
            q=float(np.sum(a*(a-1))/(M*(M-1)))
            rows.append((t,q,int(a.sum()),float(t*q)))
    return rows

start=time.time()
# Analytic control: H=0 graph is Z, whose Q_n=binom(2n,n)/4^n.
line=exact(np.zeros(65,dtype=int),32)
line_error=max(abs(q-math.comb(2*n,n)/4**n) for n,q in enumerate(line))
assert line_error<1e-14
# A sampled comb, exact propagation versus independent MC, finite time.
g=np.random.default_rng(2026111301)
h=heights_for(g,1/3,64)
q=exact(h,64)
mc=monte(h,64,100000,g,{16,32,64})
validation={'nice':nice,'line_max_absolute_error':line_error,
            'finite_comb': [{'n':n,'exact':q[n],'mc':v,'absolute_error':abs(v-q[n])} for n,v,_,_ in mc]}
# Small long-horizon ensemble. Conditional walkers share each sampled comb;
# fresh environments are the statistical units for uncertainty summaries.
T=4096; M=4000; E=8; cps={64,128,256,512,1024,2048,4096}
rows=[]
for gi,gamma in enumerate([0.28,1/3,0.40]):
    for env in range(E):
        seed=2026111300+1000*gi+env
        rng=np.random.default_rng(seed)
        heights=heights_for(rng,gamma,T)
        for n,v,count,nq in monte(heights,T,M,rng,cps):
            rows.append({'gamma':gamma,'environment':env,'seed':seed,'n':n,'walkers':M,'Q_hat':v,'backbone_walkers':count,'nQ_hat':nq})
    print('finished gamma',gamma,flush=True)
with (ROOT/'data/backbone_kernel.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
summary=[]
for gamma in [0.28,1/3,0.40]:
    for n in sorted(cps):
        vals=np.array([r['Q_hat'] for r in rows if r['gamma']==gamma and r['n']==n])
        summary.append({'gamma':gamma,'n':n,'mean_Q':float(vals.mean()),'environment_SE_Q':float(vals.std(ddof=1)/math.sqrt(E)),'mean_nQ':float(n*vals.mean()),'environment_SE_nQ':float(n*vals.std(ddof=1)/math.sqrt(E)),'environments':E})
with (ROOT/'data/summary.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(summary[0])); w.writeheader(); w.writerows(summary)
validation.update({'T':T,'walkers':M,'environments_per_gamma':E,'gamma_values':[.28,1/3,.40],'elapsed_seconds':time.time()-start,'method':'distinct-walker U-statistic; environments are independent; finite light cones exact; sample variability is not proof'})
(ROOT/'data/validation.json').write_text(json.dumps(validation,indent=2)+'\n')
print(json.dumps(validation,indent=2),flush=True)
