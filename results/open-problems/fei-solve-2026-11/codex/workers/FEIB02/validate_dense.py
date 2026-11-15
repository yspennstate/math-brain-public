import json,math,time
from pathlib import Path
rows=[json.loads(x) for x in Path('thresholds_dense.jsonl').read_text().splitlines()]
assert [r['n'] for r in rows]==list(range(1,2001))
maxerr=0.;checks=0
for n in [25,32,64,128,256,512,1000,1024,2000]:
 a=rows[n-1];b=json.loads(Path(f'thresholds_{n:04d}.json').read_text())
 for name in ['A/I','B/I','Gamma/I']:
  delta=abs(a['maxima'][name]['value']-b['maxima'][name]['value']);maxerr=max(maxerr,delta);assert delta<1e-10
  center=a['central_threshold'][name];other=b['majority_or_nearest_threshold'][name]
  maxerr=max(maxerr,abs(center-other));assert abs(center-other)<1e-10
  checks+=2
for row in rows:
 n=row['n'];exact=3-4/n-(2-4/n)*2.**(-n)
 assert abs(row['maxima']['A/I']['value']-exact)<1e-10
 # For n<=24 the dense thresholds must lie below the exhaustive symmetric extrema.
 if n<=24:
  small=json.loads(Path(f'census_{n:02d}.json').read_text())
  for key in row['maxima']:assert row['maxima'][key]['value']<=small['maxima'][key]['value']+1e-10
print('dense_dimensions_checked',len(rows))
print('thresholds_total_including_reflection',sum(r['n'] for r in rows))
print('independent_python_C_ratio_checks',checks)
print('maximum_absolute_ratio_difference',maxerr)
print('corner_formula_checks',len(rows))
