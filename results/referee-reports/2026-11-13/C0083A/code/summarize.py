"""Export roots and descriptive asymptotic fits; no inferential claims."""
import os
for name in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:
    os.environ[name]='1'
import csv
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data'
rows=sorted([json.loads(p.read_text()) for p in OUT.glob('mc_n*_d*_lambda*.json')],
            key=lambda a:(a['d'],a['lambda'],a['n']))
columns=['d','n','V','lambda','target_chi','pc','se','interpolation_spread','leading',
         'a2_n','two_terms_n','two_terms_m','window_scale','scaled_window_residual',
         'n2_leading_residual','n3_two_term_residual']
with (OUT/'roots.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=columns);w.writeheader()
    for a in rows:
        a['scaled_window_residual']=(a['pc']-a['two_terms_n'])/a['window_scale']
        a['n2_leading_residual']=a['n']**2*(a['pc']-a['leading'])
        a['n3_two_term_residual']=a['n']**3*(a['pc']-a['two_terms_n'])
        w.writerow({key:a[key] for key in columns})

def fit(group,drop):
    a=group[drop:];d=a[0]['d']
    n=np.array([r['n'] for r in a],dtype=float)
    y=np.array([r['pc']-r['two_terms_n'] for r in a])*n**2
    sigma=np.array([np.hypot(r['se'],r['interpolation_spread']) for r in a])*n**2
    if d==3:
        X=np.column_stack([np.ones(len(n)),1/n]);terms=['window offset in n^-2','n^-3 correction']
    elif d==6:
        X=np.column_stack([1/n,1/n**2]);terms=['combined window / n^-3 correction','n^-4 correction']
    else:
        X=np.column_stack([n**(1-d/3),1/n]);terms=['n^(-1-d/3) window correction','n^-3 correction']
    beta,_,_,sv=np.linalg.lstsq(X/sigma[:,None],y/sigma,rcond=None)
    chisq=np.sum(((X@beta-y)/sigma)**2)
    return {'n_values':list(n),'terms':terms,'coefficients':list(beta),
            'chi_square':float(chisq),'dof':len(n)-2,'condition':float(sv[0]/sv[-1])}

fits=[]
for d in sorted(set(r['d'] for r in rows)):
    for lam in sorted(set(r['lambda'] for r in rows if r['d']==d)):
        group=[r for r in rows if r['d']==d and r['lambda']==lam]
        if len(group)<4:continue
        fits.append({'d':d,'lambda':lam,'all':fit(group,0),'drop_smallest':fit(group,1)})
(OUT/'fits.json').write_text(json.dumps(fits,indent=2)+'\n')

print('Largest n per dimension, lambda=1')
for d in sorted(set(r['d'] for r in rows)):
    a=max((r for r in rows if r['d']==d and r['lambda']==1),key=lambda r:r['n'])
    print(d,a['n'],f"{a['pc']:.10f}",f"se={a['se']:.2g}",
          f"spread={a['interpolation_spread']:.2g}",f"two_terms={a['two_terms_n']:.10f}",
          f"window_residual={a['scaled_window_residual']:.3f}")
for f in fits:print('fit',f['d'],f['lambda'],f['all']['coefficients'],f['drop_smallest']['coefficients'],f['all']['chi_square'])
