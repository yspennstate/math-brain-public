"""Summarize evidence without interpreting finite EM runs as global optimizers."""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:
 os.environ[key]='1'
import csv,json,collections
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/'data'/'recovery.csv').open()))
groups=collections.defaultdict(list)
for r in rows:groups[(r['L'],r['sigma'],r['n'],r['method'])].append(float(r['relative_squared_error']))
with (ROOT/'data'/'recovery_summary.csv').open('w') as f:
 out=csv.writer(f);out.writerow(['L','sigma','n','method','replicates','mean_relative_squared_error','median_relative_squared_error'])
 for key,v in sorted(groups.items(),key=lambda kv:(int(kv[0][0]),float(kv[0][1]),int(kv[0][2]),kv[0][3])):
  out.writerow([*key,len(v),np.mean(v),np.median(v)])
ms=collections.defaultdict(list);theory={}
for r in csv.DictReader((ROOT/'data'/'moment_scaling.csv').open()):
 s=float(r['sigma']);ms[s].append(float(r['squared_error']));theory[s]=float(r['exact_variance_over_n'])
summary=[]
for s,v in sorted(ms.items()):
 summary.append({'sigma':s,'replicates':len(v),'mse':float(np.mean(v)),'standard_error':float(np.std(v,ddof=1)/np.sqrt(len(v))),'theory_mse':theory[s],'ratio':float(np.mean(v)/theory[s])})
slope=float(np.polyfit(np.log([x['sigma'] for x in summary if x['sigma']>=2]),np.log([x['mse'] for x in summary if x['sigma']>=2]),1)[0])
# Independent arithmetic: centered complex moments via explicit fourth/second Gaussian moments.
a=b=.2
for s in ms:
 direct=((a*a+4*a*s*s+2*s**4)*(b+s*s)-a*a*b)/20000
 assert abs(direct-theory[s])<1e-10*max(1,direct)
metadata={'datasets':len(rows)//4,'estimates':len(rows),'L':sorted({int(r['L']) for r in rows}),'max_n':max(int(r['n']) for r in rows),'moment_loglog_slope_sigma_ge_2':slope,'moment_results':summary}
(ROOT/'data'/'summary.json').write_text(json.dumps(metadata,indent=2)+'\n')
print(json.dumps(metadata,indent=2))
print('\nSelected recovery medians:')
for key,v in groups.items():
 if key[0]=='5' and key[1] in ['0.5','1.5'] and key[2] in ['200','2000','20000']:
  print(key,'median',round(float(np.median(v)),6))
print('\nScaling suite medians:')
g=collections.defaultdict(list)
for r in rows:
 if r['suite']=='scaling':g[(r['sigma'],r['n'],r['method'])].append(float(r['relative_squared_error']))
for key,v in g.items():
 if key[2] in ['marginal','quasi_constrained']:print(key,round(float(np.median(v)),5))
