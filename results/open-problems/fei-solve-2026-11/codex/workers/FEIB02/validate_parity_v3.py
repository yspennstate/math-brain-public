import json,math,time
from pathlib import Path
import mpmath as mp
from symmetric import evaluate
mp.mp.dps=100
start=time.monotonic();records=[];max_linear=0.;max_log=0.
for n in [25,64,256,1024,2000]:
 row=json.loads(Path(f'parity_thresholds_v3_{n:04d}.json').read_text())
 thresholds={row['maxima'][k]['threshold'] for k in ['A/I','B/I','Gamma/I']}
 thresholds.add(1)
 for r in sorted(thresholds):
  f=[(1 if t<r else -1)*(-1)**t for t in range(n+1)];v=evaluate(f,100)
  for name in ['A/I','B/I','Gamma/I']:
   true=v[name];approx=row['ratios'][name][r-1];la=row['log2_ratios'][name][r-1]
   if approx is not None:
    err=abs(float(true)-approx);max_linear=max(max_linear,err);assert err<1e-10
   if true:
    le=abs(float(mp.log(true,2))-la);max_log=max(max_log,le);assert le<2e-10,(n,r,name,le)
   else:assert la is None
  records.append({'n':n,'threshold':r,'ratios':{name:mp.nstr(v[name],70) for name in ['A/I','B/I','Gamma/I']}})
  print(n,r,'checked',flush=True)
Path('parity_v3_high_precision.json').write_text(json.dumps(records,indent=2)+'\n')
print('max_absolute_ratio_error',max_linear)
print('max_absolute_log2_ratio_error',max_log)
print('wall_seconds',time.monotonic()-start)
