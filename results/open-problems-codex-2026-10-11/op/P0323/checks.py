import math, json, time
from pathlib import Path
import mpmath as mp
mp.mp.dps=50
start=time.monotonic()
results={'tail_checks':[],'image_checks':[],'normalization_checks':[]}
# One-sided lattice tail has a nonzero first-order term; unlike symmetric tails,
# it exercises the slow R^{-s} mechanism. Analytic continuation of Hurwitz zeta
# evaluates the convergent difference even for s<1.
for s0 in ['0.05','0.3','0.9','1.1','2','8']:
 s=mp.mpf(s0);x=mp.mpf('0.7')
 for R in [5,20,100]:
  tail=mp.zeta(s,R-x)-mp.zeta(s,R)
  bound=s*x*(mp.mpf(R)/(R-x))**(s+1)*(mp.mpf(R)**(-s-1)+mp.mpf(R)**(-s)/s)
  assert 0<tail<=bound
  results['tail_checks'].append(dict(s=s0,R=R,tail=float(tail),bound=float(bound),ratio=float(tail/bound)))
# Paired-image correction after subtracting the constant. The sum is positive
# by convexity, and its infinite value is given by Hurwitz zeta differences.
for s0 in ['0.05','0.3','0.9','1.1','2','8']:
 s=mp.mpf(s0);r=mp.mpf('1.4')
 for N in [8,20,80]:
  q=r/N
  correction=N**(-s)*(mp.zeta(s,1+q)+mp.zeta(s,1-q)-2*mp.zeta(s))
  bound=s*(s+1)*r*r*2**(s+2)*N**(-s-2)*mp.zeta(s+2)
  assert 0<=correction<=bound
  results['image_checks'].append(dict(s=s0,N=N,correction=float(correction),bound=float(bound)))
# Direct finite normalized-weight perturbation stress tests, including weights
# whose unnormalized normalizer is extremely small (computed in log scale).
for b in [0.01,1,20]:
 for offset in [-10000,0,10000]:
  E=[offset+z for z in [0,.1,2,11]];delta=[-.03,.03,.02,-.01]
  def normalized(logs):
   maximum=max(logs);w=[math.exp(z-maximum) for z in logs];Z=sum(w);return [z/Z for z in w]
  p=normalized([-b*z for z in E]);q=normalized([-b*(z+d) for z,d in zip(E,delta)])
  l1=sum(abs(u-v) for u,v in zip(p,q));bound=math.expm1(2*b*max(abs(d) for d in delta))
  assert l1<=bound+1e-10
  results['normalization_checks'].append(dict(b=b,offset=offset,l1=l1,bound=bound))
results['seconds']=time.monotonic()-start
Path('numerical_checks.json').write_text(json.dumps(results,indent=2))
print({k:len(v) for k,v in results.items() if isinstance(v,list)},'seconds',results['seconds'])
