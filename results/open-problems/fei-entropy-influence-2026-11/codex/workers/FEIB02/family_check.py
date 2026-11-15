from thresholds import all_thresholds
from parity_thresholds import all_parity_thresholds
from symmetric import evaluate
err={}
for n in range(2,17):
 for dual in [False,True]:
  rows=all_parity_thresholds(n)[0] if dual else all_thresholds(n)
  for r in range(1,n+1):
   f=[(1 if t<r else -1)*((-1)**t if dual else 1) for t in range(n+1)]
   v=evaluate(f,80)
   for key,values in rows.items():
    d=abs(values[r-1]-float(v[key]));err[key]=max(err.get(key,0),d);assert d<1e-11
print('All thresholds and parity times thresholds checked against exact finite differences, n=2..16.')
print('maximum_absolute_errors',err)
