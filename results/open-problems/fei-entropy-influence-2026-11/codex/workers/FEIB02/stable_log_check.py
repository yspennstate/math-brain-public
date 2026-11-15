import mpmath as mp
from symmetric import evaluate
from parity_thresholds import all_parity_thresholds
mp.mp.dps=100
maxerr=0
for n in range(2,17):
 vals,logs=all_parity_thresholds(n)
 for r in range(1,n+1):
  f=[(1 if t<r else -1)*(-1)**t for t in range(n+1)];v=evaluate(f,100)
  for name,x in vals.items():
   err=abs(float(v[name])-x[r-1]);maxerr=max(maxerr,err);assert err<1e-11
print('parity stable log max_absolute_error_n2_to16',maxerr)
for family in ['AND','parity_times_AND']:
 n=2000;f=[1]*n+[-1]
 if family!='AND':f=[x*(-1)**t for t,x in enumerate(f)]
 a=evaluate(f,80);b=evaluate(f,720)
 for name in ['A/I','B/I','Gamma/I','P/I']:
  if b[name]:assert abs(a[name]/b[name]-1)<mp.mpf('1e-70'),(family,name)
 print(family,{name:mp.nstr(a[name],60) for name in ['A/I','B/I','Gamma/I']})
