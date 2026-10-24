"""Floating-point exploration only; not an acceptance or asymptotic proof.

Uses exact threshold coefficients from the executed integer checker, but logs
and final sums are floating point. Run from this directory:
  python entropy_weight_probe.py > entropy_weight_probe_replayed.json
The all-dimensional separation uses the analytical theorem and the published
symmetric-function FEI bound, not these finite values.
"""
from verify_threshold_obstruction import threshold_spectrum,binomial_row,overlap_ratio
from math import log,log2,log1p
from fractions import Fraction as F
import json
out=[]
for m in [2,4,8,16,32,64]:
 n=m*m+1;s=(m*m-m)//2
 W,piv=threshold_spectrum(n,s);row=binomial_row(n-1)
 den=piv*(1<<(n+1));K=B=0.; contrib=[]
 for k in range(n):
  lo,hi=sorted([W[k]**2,W[k+1]**2])
  if not lo:continue
  mass=float(F(row[k]*lo,den))
  lr=log2(hi)-log2(lo)
  ratio=float(F(lo,hi))
  K+=mass*lr
  first=mass*(lr+log1p(ratio)/log(2))
  second=mass*(log1p(ratio)/ratio/log(2)) if ratio else mass/log(2)
  B+=first+second
  contrib.append((k,mass*lr))
 out.append({'n':n,'K_i/I_i':K,'B_i/I_i':B,'O_i/I_i':float(overlap_ratio(n,s)[0]),'largest_K_levels':sorted(contrib,key=lambda a:-a[1])[:5]})
print(json.dumps(out,indent=2))
