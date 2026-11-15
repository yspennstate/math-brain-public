"""Independent checks of formulas and witnesses; assertions are numeric only."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:
    os.environ[k]='1'
import itertools
import json
import math
from pathlib import Path
import numpy as np
from scipy import linalg
from numerics import omega, harmonic, record, out

def vol2(a):
    if len(a)==0:return 1.
    return float(np.prod(np.linalg.svd(a,compute_uv=False))**2)

def checks():
    rng=np.random.default_rng(960096)
    results=[]
    for m in range(2,8):
        n=2*m-1
        a=rng.standard_normal((n,m));a/=np.linalg.norm(a,axis=1).max()
        v_m=0;v_ridge=0;weighted=0;max_distance_error=0
        for s in itertools.combinations(range(n),m):v_m+=vol2(a[list(s)])
        for t in itertools.combinations(range(n),m-1):
            ridge=a[list(t)]
            weight=vol2(ridge);v_ridge+=weight
            normal=np.linalg.svd(ridge,full_matrices=True)[2][-1]
            for k in sorted(set(range(n))-set(t)):
                d=abs(a[k]@normal)
                ratio=vol2(a[list(t)+[k]])/weight
                max_distance_error=max(max_distance_error,abs(d*d-ratio))
                weighted+=weight*d*d
        g=a.T@a
        cb=float(np.linalg.det(g))
        ridge_cb=cb*float(np.trace(np.linalg.inv(g)))
        mean=weighted/(m*v_ridge)
        rhs=1/float(np.trace(np.linalg.inv(g)))
        result={'m':m,'cb_relative_error':abs(v_m/cb-1),
                'ridge_cb_relative_error':abs(v_ridge/ridge_cb-1),
                'distance_identity_max_abs_error':max_distance_error,
                'weighted_mean':mean,'inverse_trace':rhs,'mean_abs_error':abs(mean-rhs),
                'bound_trace_over_m_squared':float(np.trace(g))/m**2,
                'harmonic_tight_error':float(np.linalg.norm(harmonic(m).T@harmonic(m)-(n/m)*np.eye(m)))}
        assert result['cb_relative_error']<1e-10
        assert result['ridge_cb_relative_error']<1e-10
        assert result['distance_identity_max_abs_error']<1e-10
        assert abs(mean-rhs)<1e-10
        # Local real Plucker identity after fixing m-2 rows.
        if m>=3:
            base=list(range(m-2));i,j,k,l=range(m-2,m+2)
            def minor(x,y):return float(np.linalg.det(a[base+[x,y]]))
            pl=minor(i,j)*minor(k,l)-minor(i,k)*minor(j,l)+minor(i,l)*minor(j,k)
            result['plucker_residual']=pl
            assert abs(pl)<1e-10
        # Right invariance and the circuit-imbalance bound for whitened A.
        b=np.linalg.qr(a)[0]
        kap=1.
        for s in itertools.combinations(range(n),m):
            s=list(s);z=b@np.linalg.inv(b[s])
            for h in set(range(n))-set(s):
                kap=max(kap,float(np.max(np.abs(z[h]))))
        result['circuit_imbalance']=kap
        result['parseval_omega']=omega(b)
        result['imbalance_lower_bound']=1/math.sqrt(m+m*(m-1)*kap**2)
        result['imbalance_upper_bound']=float(np.linalg.norm(b,axis=1).max())/kap
        assert result['parseval_omega']>=result['imbalance_lower_bound']-1e-10
        assert result['parseval_omega']<=result['imbalance_upper_bound']+1e-10
        results.append(result)
    # Independent full reenumeration using QR/SVD for best witnesses at m<=7.
    rows=list(map(json.loads,(out/'numerics.jsonl').read_text().splitlines()))
    audit=[]
    for m in range(2,13):
        r=max((r for r in rows if r['m']==m),key=lambda r:r['omega'])
        a=np.loadtxt(out/r['matrix_file'],delimiter=',')
        s=a[r['witness_zero_based']]
        qr=np.linalg.qr(s)[1]
        alt=float(linalg.svdvals(qr)[-1])
        entry={'m':m,'recorded':r['omega'],'qr_gesdd':alt,'abs_difference':abs(alt-r['omega']),
               'max_row_norm':float(np.linalg.norm(a,axis=1).max())}
        assert abs(alt-r['omega'])<2e-14
        assert entry['max_row_norm']<=1+2e-14
        if m<=7:
            other=min(float(linalg.svdvals(a[list(s)])[-1]) for s in itertools.combinations(range(2*m-1),m))
            entry['independent_full_min']=other
            assert abs(other-r['omega'])<2e-14
        audit.append(entry)
    (out/'identity_checks.json').write_text(json.dumps(results,indent=2))
    (out/'witness_audit.json').write_text(json.dumps(audit,indent=2))
    print(json.dumps({'identity_dimensions':len(results),'witness_dimensions':len(audit),
                      'max_cb_error':max(r['cb_relative_error'] for r in results),
                      'max_witness_error':max(r['abs_difference'] for r in audit)},indent=2))

def paley():
    for m in (3,5,7,9):
        q=2*m-1
        if q==9:
            # F_9 = F_3[x]/(x^2+1).
            elems=[(i,j) for i in range(3) for j in range(3)]
            def mul(a,b):return ((a[0]*b[0]-a[1]*b[1])%3,(a[0]*b[1]+a[1]*b[0])%3)
            squares={mul(a,a) for a in elems[1:]}
            def chi(x,y):
                v=((x[0]-y[0])%3,(x[1]-y[1])%3)
                return 0 if v==(0,0) else 1 if v in squares else -1
        else:
            elems=list(range(q));squares={i*i%q for i in range(1,q)}
            def chi(x,y):return 0 if x==y else 1 if (x-y)%q in squares else -1
        c=np.zeros((q+1,q+1));c[0,1:]=1;c[1:,0]=1
        for i,x in enumerate(elems):
            for j,y in enumerate(elems):c[i+1,j+1]=chi(x,y)
        ci=c.astype(np.int64)
        assert np.array_equal(ci@ci,q*np.eye(q+1,dtype=np.int64))
        vals,vecs=np.linalg.eigh(c)
        a=np.sqrt(2)*vecs[:,-m:]
        assert np.linalg.norm(np.linalg.norm(a,axis=1)-1)<1e-10
        # Remove one row to reach N=2M-1. A zero minimum disqualifies it.
        row=record(a[1:],m,'paley_conference','candidate',0,{'q':q})
        print('Paley',m,row['omega'],'numerically full spark',row['omega']>1e-12)

if __name__=='__main__':
    import sys
    (paley if len(sys.argv)>1 and sys.argv[1]=='paley' else checks)()
