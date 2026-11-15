"""Check candidate measure inequalities and independently verify search outputs."""
import json,math
from pathlib import Path
import numpy as np
from common import tables,mv

def one(mu,n):
    pc,z,L,fac,meta=tables(n);rr=np.array([r for r,k in meta]);mu=np.array(mu)
    up=mv(z,mu); left=mv(L,mu); right=fac*up[rr]**1.5
    assert abs(mu.sum()-1)<1e-10 and mu.min()>=0
    ratios=np.divide(left,right,out=np.zeros_like(left),where=right>0)
    assert np.max(ratios)<=1+1e-10
    D=mu[1:]-4.**(pc[1:]-1)*up[1:]**2
    pp=np.minimum(1,4.**(pc-1)*up);pp[0]=1
    Pdiff=left-3.**np.array([k for r,k in meta])*up[rr]*np.sqrt(pp[rr])
    worst=-math.inf
    for r in range(1<<n):
        val=0.;ir=0.
        for u in range(1<<n):
            if (u&r)!=r or u==r or mu[u]==0:continue
            v=u^r;mn=min(up[r|(1<<i)] for i in range(n) if (v>>i)&1)
            val+=mu[u]*math.log2(1/mn)
            ir+=mu[u]*v.bit_count()
        K=4*math.log2(3)+4/(3*math.e*math.log(2))
        bound=K*ir+8*(pc[r]+1)*(up[r]-mu[r])
        worst=max(worst,val-bound)
    assert worst<1e-9
    return {'max_C_left_right':float(ratios.max()),'max_D_violation':float(D.max()),
            'max_P_size_violation':float(Pdiff.max()),'max_L1D_violation':worst}

if __name__=='__main__':
    out=[]
    for r in json.load(open('small_repaired.json')):
        out.append({'source':'small_repaired','n':r['n'],'checks':one(r['mu'],r['n'])})
    for row in json.load(open('families_output.json'))['results']:
        for name,r in row['families'].items():
            out.append({'source':name,'n':row['n'],'checks':one(r['mu'],row['n'])})
    rho=1/8
    thinning={'rho':rho,'mu_empty':1-rho,'mu_singleton':rho,
              'C_left':rho,'C_right':2*rho**1.5,'C_left_right':1/(2*math.sqrt(rho)),
              'spectral_source':'dictator x_1'}
    assert thinning['C_left']>thinning['C_right']
    Path('properties_output.json').write_text(json.dumps({'finite_measures':out,'thinning_counterexample':thinning},indent=2)+'\n')
    print('finite measures checked',len(out),'max C left/right',max(x['checks']['max_C_left_right'] for x in out))
    print('max L1D violation',max(x['checks']['max_L1D_violation'] for x in out))
    print('thinning counterexample',thinning)
