import pathlib,numpy as np,json,math
R=pathlib.Path(__file__).parent
rng=np.random.default_rng(31)
worst=0.;cdf_worst=0.;trials=0
for n in [2,3,5,10,20]:
 for _ in range(40):
  A=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
  B=A.copy();B[rng.integers(n)]=10*(rng.normal(size=n)+1j*rng.normal(size=n))
  sa=np.linalg.svd(A,compute_uv=False);sb=np.linalg.svd(B,compute_uv=False)
  thresholds=np.unique(np.r_[sa,sb])
  diff=max(abs(int(np.count_nonzero(sa<x))-int(np.count_nonzero(sb<x))) for x in thresholds)
  assert diff<=1,(n,diff)
  cdf_worst=max(cdf_worst,diff)
  b=2.;cap=b*math.log(n)
  ha=np.clip(np.log(sa),-cap,cap);hb=np.clip(np.log(sb),-cap,cap)
  ratio=abs(ha.mean()-hb.mean())/(2*cap/n)
  assert ratio<=1+1e-10
  worst=max(worst,ratio);trials+=1
diag=[]
for n in [10,100,1000,10000,100000]:
 m=int(n/math.log(n)); mass=m/n; logtail=mass*math.log(n)
 diag.append({'n':n,'fraction_small':mass,'small_log_integral':logtail})
# Analytic Pareto alpha=1 normalization boundary example: E count above n is n.
# At alpha=1, P(R>t)=log(e t)/t (t>=1), a valid slowly varying tail.
boundary=[{'n':n,'expected_entries_above_n':n*math.log(math.e*n)} for n in [10,100,1000]]
result={'row_replacement_trials':trials,'max_count_discrepancy':cdf_worst,'max_clamp_change_ratio':worst,'diagonal_counterexample':diag,'slowly_varying_tail_diagnostic':boundary,'scope':'Finite numerical consistency checks only; not evidence that unrestricted convergence holds.'}
(R/'checks.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result,indent=2))
