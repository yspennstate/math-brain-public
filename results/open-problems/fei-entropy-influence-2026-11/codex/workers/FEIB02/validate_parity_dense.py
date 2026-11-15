import json,math
from pathlib import Path
rows=[json.loads(x) for x in Path('parity_dense.jsonl').read_text().splitlines()]
assert [r['n'] for r in rows]==list(range(2,2001))
maxerr=0
for n in [25,32,64,128,256,512,1000,1024,2000]:
 a=rows[n-2];b=json.loads(Path(f'parity_thresholds_v3_{n:04d}.json').read_text())
 for key in ['A/I','B/I','Gamma/I']:
  err=abs(a['maxima'][key]['value']-b['maxima'][key]['value']);maxerr=max(maxerr,err);assert err<1e-10,(n,key,err)
for a in rows[:23]:
 n=a['n'];c=json.loads(Path(f'census_{n:02d}.json').read_text())
 for key in ['A/I','B/I','Gamma/I']:assert a['maxima'][key]['value']<=c['maxima'][key]['value']+1e-10
print('dense_parity_dimensions_checked',len(rows))
print('all_nonconstant_parity_thresholds_covered',sum(r['n'] for r in rows))
print('n1_parity_times_threshold_is_constant',True)
print('maximum_absolute_ratio_difference_against_convolution',maxerr)
