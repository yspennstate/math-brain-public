import json,math,time
from pathlib import Path
import mpmath as mp
from symmetric import evaluate
mp.mp.dps=100
records=[];start=time.monotonic()
for n in [31,127,511,1999]:
 row=json.loads(Path(f'balanced_hill_v2_{n:04d}.json').read_text())
 for s in row['searches']:
  f=[1 if x=='+' else -1 for x in s['value_vector']]
  assert all(f[n-t]==-f[t] for t in range(n+1))
  v=evaluate(f,100);assert v['balanced']
  for name,x in s['balanced_ratios'].items():assert abs(float(v[name])-x)<1e-10
  records.append({'n':n,'objective':s['objective'],'ratios':{name:mp.nstr(v[name],70) for name in s['balanced_ratios']}})
  print(n,s['objective'],flush=True)
Path('balanced_high_precision.json').write_text(json.dumps(records,indent=2)+'\n')
print('wall_seconds',time.monotonic()-start)
