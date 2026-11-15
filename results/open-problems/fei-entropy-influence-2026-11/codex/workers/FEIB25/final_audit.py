"""Independent witness reconstruction and whole-census inequality checks."""
import json,math,os,resource,subprocess,sys,time
from pathlib import Path
import numpy as np
from levels import ROOT,wht,profile,plan,candidates,profile_mu

def main():
    started=time.monotonic();checked=0;worst=0.;bounds={'A1':-1e9,'A2':-1e9,'Han':-1e9,'sandwich':-1e9}
    for n in range(1,6):
        z=np.load(ROOT/f'census_n{n}.npz');reps=z['tt'];N=1<<n;pp=plan(n);x=pp[0]
        for at in range(0,len(reps),4096):
            tt=reps[at:at+4096];f=1.-2.*((tt[:,None]>>np.arange(N,dtype=np.uint32))&1)
            c=wht(f);mu=c*c;W=z['W_numerator'][at:at+len(tt)]/(N*N);A=z['A'][at:at+len(tt)];E=z['E'][at:at+len(tt)]
            influence=np.stack([np.mean(f!=f[:,x^(1<<i)],axis=1) for i in range(n)],axis=1)
            I=influence.sum(axis=1)
            worst=max(worst,float(np.max(abs(I-(W*np.arange(n+1)).sum(axis=1)))))
            bounds['A1']=max(bounds['A1'],float(np.max(A[:,1]-np.sqrt(W[:,0])*I/math.log(2))))
            if n>=2:bounds['A2']=max(bounds['A2'],float(np.max(A[:,2]-(I*I-(influence*influence).sum(axis=1))/math.log(2))))
            eta=np.zeros_like(mu);positive=mu>0;eta[positive]=-mu[positive]*np.log2(mu[positive]);H=eta.sum(axis=1)
            bounds['Han']=max(bounds['Han'],float(np.max(E-H)))
            bounds['sandwich']=max(bounds['sandwich'],float(np.max(E-A.sum(axis=1)-I/math.log(2))))
            checked+=len(tt)
        # Check selected representatives under independently sampled NPN actions.
        rng=np.random.default_rng(9000+n)
        for t in rng.choice(reps,min(20,len(reps)),replace=False):
            f=1.-2.*((int(t)>>np.arange(N,dtype=np.uint32))&1);p=profile(f)
            perm=rng.permutation(n);mask=int(rng.integers(N));image=np.zeros(N,dtype=np.int64)
            for j in range(n):image|=((x>>j)&1)<<int(perm[j])
            q=profile(-f[image^mask]);worst=max(worst,float(np.max(abs(np.array(p['A'])-q['A']))))
    hill=json.load(open(ROOT/'hill.json'));hill_error=0.
    for row in hill:
        f=np.load(ROOT/row['truth_table_file'])['f'];p=profile(f);W=np.array(p['W']);A=np.array(p['A']);den=candidates(W)[row['objective']]
        d=row['d'];ratio=A[d]/den[d]
        hill_error=max(hill_error,abs(ratio-row['best_ratio']),float(np.max(abs(A-row['A']))))
    assert max(bounds.values())<1e-11
    assert worst<1e-11 and hill_error<1e-11
    result=dict(census_functions_checked=checked,max_identity_and_NPN_error=worst,
                max_inequality_residuals=bounds,hill_witnesses_checked=len(hill),max_hill_error=hill_error,
                inherited_nice=os.getpriority(os.PRIO_PROCESS,0),elapsed_seconds=time.monotonic()-started,
                max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    (ROOT/'final_audit.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))

if __name__=='__main__':main()
