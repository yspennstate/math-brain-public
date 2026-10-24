import numpy as np,json
from scipy.optimize import brentq
from scipy.linalg import eigh
from pathlib import Path
# load definitions without running exploratory main
src=Path(__file__).with_name('explore_power.py').read_text().split('rng=np.random')[0]
exec(src)

def hb(p):
    if p==0:return 0.
    if p==1:return 0.
    return -p*np.log(p)-(1-p)*np.log1p(-p)
def vn(H,n):
    r=brentq(lambda x:hb(x)-H/n,1e-15,.5-1e-15)
    return n*r*(1-r)*np.log((1-r)/r)**2
rng=np.random.default_rng(3202);rows=[]
for n in [2,3,4,5]:
    B=basis(n);best=None
    for k in range(200 if n<4 else 60):
        U,_=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
        lam=1/(1+np.exp(-rng.normal(size=n)*2.4));K=(U*lam)@U.conj().T
        r=metric(K,B)
        if r is None:continue
        r['number_cap']=vn(r['H'],n);r['relative']=r['ratio']/r['number_cap']
        if best is None or r['relative']>best['relative']:best=dict(r,K=K,lam=lam)
    if best:
        np.savez(out/f'number_seed_{n}.npz',K=best['K'],A=best['A'])
        row={k:(float(v) if np.isscalar(v) else v.tolist()) for k,v in best.items() if k not in ['K','A']}
        row['n']=n;rows.append(row);print(row,flush=True)
(out/'explore_number.json').write_text(json.dumps(rows,indent=2))
