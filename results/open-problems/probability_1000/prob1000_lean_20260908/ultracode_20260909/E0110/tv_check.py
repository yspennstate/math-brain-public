"""TV-flavoured check for family F (mu_i = -1, U' = e^{-x}, Gamma = I):
from the 'empty' start x_i = -log m_i + 2 and the 'overfull' start x_i = -log m_i - 1, estimate the
total-variation distance of each coordinate's marginal law at time t from a stationary reference
(the fixed-point start run to a late time), by 15-bin histograms on 3000 paths.  Report the first time
at which every coordinate's marginal TV is below 0.15, for d = 8, 32, 64.  If the relaxation were
d log d (or d), this time would grow by a factor ~4-8 from d=8 to d=64; log d predicts ~+1.4."""
import numpy as np, json, sim_grbm as S
S.rng = np.random.default_rng(7)
def marg_tv(A, B, nb=15):
    lo = min(A.min(), B.min()); hi = max(A.max(), B.max())
    ha,_ = np.histogram(A, bins=nb, range=(lo,hi)); hb,_ = np.histogram(B, bins=nb, range=(lo,hi))
    return 0.5*np.abs(ha/len(A) - hb/len(B)).sum()
out=[]
for d in [8,32,64]:
    mu=-np.ones(d); m=np.cumsum(-mu); xfix=-np.log(m); dt=min(0.5/m.max(),0.01)*0.5; T=14.0; rec=int(round(0.25/dt))
    npaths=3000
    # reference: fixed-point start, sample at T (and at T-1 pooled) -> stationary to within its own noise
    tr, _, _ = S.simulate_pair(xfix, xfix, mu, 0.0, dt, 1, 1)  # warm-up call (no-op)
    def paths(x0):
        X=np.tile(x0,(npaths,1)); snaps={}; n=0; nsteps=int(round(T/dt)); sq=np.sqrt(dt)
        for n in range(nsteps+1):
            if n%rec==0: snaps[round(n*dt,3)]=X.copy()
            if n==nsteps: break
            X = X + S.drift(X,mu)*dt + S.rng.standard_normal((npaths,d))*sq
        return snaps
    ref = paths(xfix)[T]
    res={'d':d}
    for name,x0 in [('empty',xfix+2.0),('overfull',xfix-1.0)]:
        sn=paths(x0); ts=sorted(sn)
        maxtv=[max(marg_tv(sn[t][:,i],ref[:,i]) for i in range(d)) for t in ts]
        # noise floor: TV between two halves of the reference
        floor=max(marg_tv(ref[:npaths//2,i],ref[npaths//2:,i]) for i in range(d))
        first=[t for t,v in zip(ts,maxtv) if v<0.15]
        res[name]=dict(t_first_below_0p15=(first[0] if first else None), noise_floor=float(floor),
                       maxtv_curve={str(t):round(float(v),3) for t,v in zip(ts,maxtv)})
    print(json.dumps({k:(v if k=='d' else {kk:vv for kk,vv in v.items() if kk!='maxtv_curve'}) for k,v in res.items()}))
    out.append(res)
json.dump(out,open('tv_check.json','w',encoding='utf-8'),indent=1)
