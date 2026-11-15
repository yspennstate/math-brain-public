#!/usr/bin/env python3
import os
os.environ['MPLCONFIGDIR']='/tmp/d0056-mpl'
os.environ['XDG_CACHE_HOME']='/tmp/d0056-cache'
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
 os.environ[key]='1'
import csv,json,math
from pathlib import Path
import numpy as np
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parent.parent
os.chdir(ROOT)
def rows(p):return list(csv.DictReader(Path(p).open()))
def series(p):
 r=rows(p);return np.array([int(x['n']) for x in r]),np.array([float(x['n2q']) for x in r])
def path(m,law):
 c=Path(f'data/cert_m{m}_{law}.csv')
 return c if c.exists() else Path(f'data/m{m}_{law}.csv')
laws=('two2','two5','geom','power2.5','power3','power3.5','power4')
labels={'two2':'{0,2}','two5':'{0,5}','geom':'geometric','power2.5':'b=2.5','power3':'b=3','power3.5':'b=3.5','power4':'b=4','sparse':'sparse (rho=1)'}
fits=[]
for m in (2,3):
 for law in laws:
  p=path(m,law);n,y=series(p)
  for start in (1000,3000,5000):
   use=n>=start;x=n[use];z=y[use];t=5000/x
   B=np.array([np.ones(len(x)),t,t*np.log(x/5000)]).T
   coeff,*_=np.linalg.lstsq(B,z,rcond=None)
   fits.append(dict(m=m,law=law,source=str(p),nmin=start,nmax=int(n[-1]),model='C+a/n+b*log(n)/n',
        C=coeff[0],C1=5000*(coeff[1]-coeff[2]*math.log(5000)),C2=5000*coeff[2],
        rmse=float(np.sqrt(np.mean((B@coeff-z)**2))),condition=float(np.linalg.cond(B))))
  if law in ('power3.5','power4'):
   use=n>=3000;x=n[use];z=y[use]
   B=np.array([np.ones(len(x)),(5000/x)**.5,5000/x]).T if law=='power3.5' else np.array([np.ones(len(x)),1/np.log(x),1/np.log(x)**2]).T
   coeff,*_=np.linalg.lstsq(B,z,rcond=None)
   fits.append(dict(m=m,law=law,source=str(p),nmin=3000,nmax=int(n[-1]),model='C+a/sqrt(n)+b/n' if law=='power3.5' else 'C+a/log(n)+b/log(n)^2',
        C=coeff[0],C1=coeff[1],C2=coeff[2],rmse=float(np.sqrt(np.mean((B@coeff-z)**2))),condition=float(np.linalg.cond(B))))
with open('data/fits.csv','w') as f:
 w=csv.DictWriter(f,fieldnames=fits[0]);w.writeheader();w.writerows(fits)
text=['### 5.0 Sparse tails: the elementary counterexample','',
'The law in Theorem A with rho=1 has isolated survival spikes. The table includes the depths n_j=2^j−1 where the direct leaf lower bound applies. C denotes certified fixed-point output; F denotes FFT output. A constant-plus-logarithmic fit is inappropriate for this oscillatory sequence.','',
'| m | n | n² q_n | arithmetic |','|---:|---:|---:|:---:|']
for m in (2,3):
 p=path(m,'sparse');r={int(x['n']):x for x in rows(p)}
 for j in (511,1023,2047,4095,8191,10000):
  text.append(f'| {m} | {j} | {float(r[j]["n2q"]):.9f} | {"C" if "cert_" in str(p) else "F"} |')
text+=['','At n=10,000 the scaled probabilities are small again. The subsequence spikes, rather than a single large endpoint value, exhibit the failure of the proposed limit. The proof of divergence in Theorem A is independent of these computations.','',
'### 5.1 Values through 10,000 generations','',
'`F` denotes binary64 FFT output with the rigorous support bound (16) but no rounding certificate. `C` denotes the independently certified fixed-point computation. The six-decimal display is a numerical value; certified rational endpoints are provided separately below.','',
'| m | initial law | arithmetic | n=1,000 | n=5,000 | n=10,000 | proposed limit |',
'|---:|---|:---:|---:|---:|---:|---:|']
for m in (2,3):
 for law in laws:
  p=path(m,law);r={int(x['n']):x for x in rows(p)}
  b=float(law[5:]) if law.startswith('power') else None
  target=(b*(b-2)/2 if b else 4)/(m-1)**2
  vals=[float(r[j]['n2q']) for j in (1000,5000,10000)]
  text.append(f'| {m} | {labels[law]} | {"C" if "cert_" in str(p) else "F"} | '+ ' | '.join(f'{v:.6f}' for v in vals)+f' | {target:.6f} |')
text+=['','The stable tail changes the observed prefactor. At b=3 the values are close to 1.5 for m=2 and 0.375 for m=3, far from 4 and 1. At b=3.5 the approach to 2.625/(m-1)^2 is slower. At b=4 it is slower still; these finite times do not identify its leading correction.','',
'### 5.2 Certified endpoint intervals','',
'Intervals below include quantization and the rational support bound obtained by using B=m in (16). Endpoints are rounded outwards to twelve decimal places.','',
'| m | law | n | certified enclosure for n² q_n | rounding bound for q_n |','|---:|---|---:|---|---:|']
for m in (2,3):
 for law in ('two2','geom','power3','sparse'):
  p=Path(f'data/cert_m{m}_{law}.csv')
  if not p.exists():continue
  r=rows(p)[-1];n=int(r['n']);meta=json.loads(p.with_suffix('.json').read_text());K=meta['K']
  lo=n*n*F(int(r['q_lower_numerator']),int(r['q_lower_denominator']))
  hi=n*n*(F(int(r['q_upper_numerator']),int(r['q_upper_denominator']))+F(m*(m**(n+1)-1),(m-1)*m**(K+1)))
  scale=10**12;li=lo.numerator*scale//lo.denominator;ui=-(-hi.numerator*scale//hi.denominator)
  fmt=lambda z:f'{z//scale}.{z%scale:012d}'
  text.append(f'| {m} | {labels[law]} | {n} | [{fmt(li)}, {fmt(ui)}] | {float(r["rounding_error_bound"]):.3g} |')
text+=['','### 5.3 Fits and sensitivity','',
'Least-squares fits use the requested model C+C1/n+C2 log(n)/n, with all coefficients free. They are extrapolations of finite-time values, not proofs or statistical confidence intervals. All coefficients, conditioning diagnostics, residuals, arithmetic sources, and fit windows are in `data/fits.csv`.','',
'| m | law | C, n≥1,000 | C, n≥3,000 | C, n≥5,000 |', '|---:|---|---:|---:|---:|']
for m in (2,3):
 for law in laws:
  fs=[f for f in fits if f['m']==m and f['law']==law and f['model'].startswith('C+a/n')]
  text.append(f'| {m} | {labels[law]} | '+' | '.join(f'{f["C"]:.8f}' for f in fs)+' |')
text+=['','A fractional correction is materially better for b=3.5. Over n=3,000–10,000, fitting C+a/sqrt(n)+b/n gives the following intercepts; for b=4 a logarithmic alternative is also displayed.','',
'| m | law | alternative model | C | RMS residual |','|---:|---|---|---:|---:|']
for f in fits:
 if not f['model'].startswith('C+a/n'):
  text.append(f'| {f["m"]} | {labels[f["law"]]} | {f["model"]} | {f["C"]:.8f} | {f["rmse"]:.3g} |')
text+=['','The varying extrapolations at b=3.5 and b=4 demonstrate why a fixed 1/n and log(n)/n basis should not be interpreted as universal. Binary64 finite-moment fits also inherit the rounding drift measured below.','',
'### 5.4 Floating-point checks and long runs','',
'Changing K from 10,128 to 20,128 gives the following changes in n²q at n=10,000. Both cutoffs have negligible support error, so these discrepancies measure numerical sensitivity rather than support bias.','',
'| m | law | FFT at K=10,128 minus FFT at K=20,128 | FFT at K=10,128 minus certified value |', '|---:|---|---:|---:|']
for m in (2,3):
 for law in ('two2','power3'):
  p=Path(f'data/cert_m{m}_{law}.csv')
  a=float(rows(f'data/m{m}_{law}.csv')[-1]['n2q']);b=float(rows(f'data/check_m{m}_{law}.csv')[-1]['n2q'])
  c=float(rows(p)[-1]['n2q']) if p.exists() else math.nan
  text.append(f'| {m} | {labels[law]} | {a-b:.5g} | {a-c:.5g} |')
longpaths=sorted(Path('data').glob('long_m*.csv'))
if longpaths:
 text+=['','The raw binary64 runs to 100,000 generations are saved as `data/long_*.csv`. Their support bound remains exponentially small, but the two-point run shows growing rounding sensitivity. Both long runs are excluded from asymptotic fits. The following values are raw diagnostics, not certified estimates.','',
'| m | law | n=10,000 | n=50,000 | n=100,000 |','|---:|---|---:|---:|---:|']
 for p in longpaths:
  meta=json.loads(p.with_suffix('.json').read_text());r={int(x['n']):float(x['n2q']) for x in rows(p)}
  text.append(f'| {meta["m"]} | {labels[meta["law"]]} | '+' | '.join(f'{r[j]:.8f}' for j in (10000,50000,100000))+' |')
text+=['','### 5.5 Reproduction and resource use','',
'Run from this directory:','', '```sh','python3 code/run_suite.py','python3 code/check_float.py','python3 code/run_long.py',
'python3 -m pip install --target code/vendor gmpy2==2.3.2 python-flint==0.9.0',
'python3 code/certified.py --m 2 --law two2 --N 10000 --out data/cert_m2_two2.csv',
'python3 code/run_cert_suite.py','python3 code/run_cert_geom.py','python3 code/run_sparse.py','python3 code/validate.py','python3 code/analyze.py','```','',
'Every numerical worker uses one thread. No worker pool is used. Resource measurements are stored in the corresponding JSON files.']
metas=[json.loads(p.read_text()) for p in Path('data').glob('*.json') if 'peak_rss_bytes' in p.read_text()]
if metas:text.append(f'The largest recorded worker peak RSS is {max(x["peak_rss_bytes"] for x in metas)/1024**2:.1f} MiB. Concurrent worker peaks remain far below 4 GB.')
text+=['','CSV data are saved at every generation through 10 and every 50 generations thereafter; sparse-law runs also include every depth 2^j−1. `data/fits.csv` contains all fit coefficients; the stdout logs retain intermediate diagnostics.','']
p=Path('REPORT.md');s=p.read_text();start=s.index('<!-- NUMERICAL_RESULTS -->') if '<!-- NUMERICAL_RESULTS -->' in s else s.index('<!-- BEGIN GENERATED RESULTS -->');end=s.index('<!-- END GENERATED RESULTS -->')+len('<!-- END GENERATED RESULTS -->') if '<!-- END GENERATED RESULTS -->' in s else start+len('<!-- NUMERICAL_RESULTS -->')
s=s[:start]+'<!-- BEGIN GENERATED RESULTS -->\n'+'\n'.join(text)+'\n<!-- END GENERATED RESULTS -->'+s[end:];p.write_text(s)
print('updated report',len(fits),'fits')
try:
 import matplotlib
 matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 fig,axs=plt.subplots(1,2,figsize=(11,4),sharey=True)
 for ax,m in zip(axs,(2,3)):
  for law in ('two2','geom','power2.5','power3','power3.5','power4'):
   n,y=series(path(m,law));sel=n>=100
   ax.plot(n[sel],(m-1)**2*y[sel],label=labels[law])
  ax.set_xscale('log');ax.set_xlabel('generation n');ax.set_title(f'm={m}');ax.grid(alpha=.2)
  for v in (.625,1.5,2.625,4):ax.axhline(v,color='gray',linewidth=.5,linestyle=':')
 axs[0].set_ylabel('(m−1)² n² P(X_n>0)');axs[1].legend(fontsize=8)
 fig.tight_layout();fig.savefig('data/survival.png',dpi=180);fig.savefig('data/survival.pdf');plt.close(fig)
 fig,axs=plt.subplots(1,2,figsize=(11,4))
 for ax,m in zip(axs,(2,3)):
  n,y=series(path(m,'sparse'));sel=n>=100
  ax.plot(n[sel],y[sel],'.-',markersize=3,linewidth=.7)
  ax.axhline(4/(m-1)**2,color='gray',linestyle=':',linewidth=.8)
  ax.set_xlabel('generation n');ax.set_title(f'sparse law, m={m}')
  ax.set_yscale('log');ax.grid(alpha=.2)
 axs[0].set_ylabel('n² P(X_n>0)')
 fig.tight_layout();fig.savefig('data/sparse.png',dpi=180);fig.savefig('data/sparse.pdf');plt.close(fig)
except ImportError:pass
