import math,json,pathlib,random,time
from fractions import Fraction as F
R=pathlib.Path(__file__).resolve().parent
random.seed(137)
results={}
# Exact log-gamma computation, not a Monte Carlo estimate.
cases=[(0.35,0.2,0.10,0.15),(2.,1.,1.2,1.2),(0.51,0.01,0.24,0.24),
       (0.10,0.08,0.05,0.07),(0.3,0.1,0.2,0.15),(0.100001,0.1,0.1,0.1),
       (1.5,1.,1.,1.)]
loops=[]
for alpha in cases:
 A=sum(alpha); pairs=[alpha[0]+alpha[2],alpha[1]+alpha[3]]; j=max(range(2),key=pairs.__getitem__)
 a,b=alpha[j],alpha[j+2]; kap=2*A-a-b
 C=2*math.lgamma(A)-math.lgamma(a)-math.lgamma(b)
 rows=[]
 for n in [10,100,1000,10000,100000]:
  logprob=math.lgamma(a+n)+math.lgamma(b+n)-2*math.lgamma(A+n)+C
  rows.append({'n':n,'log_probability':logprob,'normalized_asymptotic_ratio':math.exp(logprob+kap*math.log(n)-C)})
 loops.append({'alpha':alpha,'kappa':kap,'log_asymptotic_constant':C,'rows':rows})
results['exact_loop_asymptotics']=loops
# Independent combinatorial check of directed boundary formula and minimum.
cutchecks=[]
coords=[(x,y) for x in range(3) for y in range(3)]
for rawalpha in cases:
 alpha=tuple(F(str(a)) for a in rawalpha)
 A=sum(alpha); kap=2*A-max(alpha[0]+alpha[2],alpha[1]+alpha[3]); best=None; minimizers=[]
 connected_min={}; connected_counts={}
 for mask in range(1,1<<9):
  S={coords[i] for i in range(9) if mask>>i&1}
  if len(S)<2: continue
  cut=sum(alpha[i] for x,y in S for i,(dx,dy) in enumerate([(1,0),(0,1),(-1,0),(0,-1)]) if (x+dx,y+dy) not in S)
  assert cut>=kap,(alpha,S,cut,kap)
  if best is None or cut<best: best=cut; minimizers=[sorted(S)]
  elif cut==best: minimizers.append(sorted(S))
  reached={next(iter(S))}; stack=list(reached)
  while stack:
   x,y=stack.pop()
   for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
    z=(x+dx,y+dy)
    if z in S and z not in reached: reached.add(z); stack.append(z)
  if reached==S:
   D=max(max(x for x,y in S)-min(x for x,y in S),max(y for x,y in S)-min(y for x,y in S))
   m=A-max(alpha[0]+alpha[2],alpha[1]+alpha[3]); assert cut>=A+D*m
   connected_min[D]=min(cut,connected_min.get(D,cut)); connected_counts[D]=connected_counts.get(D,0)+1
 cutchecks.append({'alpha':[str(a) for a in alpha],'minimum_cut':str(best),'kappa':str(kap),'subsets_checked':502,
 'minimizers':minimizers,'connected_minimum_by_diameter':{str(k):str(v) for k,v in connected_min.items()},
 'connected_counts_by_diameter':connected_counts})
results['finite_boundary_enumeration']=cutchecks
# Independently check gamma-ratio loops against sequential urn probabilities in exact rational arithmetic.
direct=[]
for rawalpha in cases:
 alpha=tuple(F(str(a)) for a in rawalpha); A=sum(alpha)
 for j in [0,1]:
  a,b=alpha[j],alpha[j+2]
  for n in range(1,9):
   sequential=F(1); numerator=F(1); denominator=F(1)
   for k in range(n):
    sequential *= (a+k)/(A+k); sequential *= (b+k)/(A+k)
    numerator *= (a+k)*(b+k); denominator *= (A+k)**2
   assert sequential==numerator/denominator
 direct.append({'alpha':[str(a) for a in alpha],'directions_checked':2,'loop_counts_checked':8})
results['exact_rational_loop_crosscheck']=direct
# Test the posterior one-step tilt, conditional on backward two-site loops.
p,q,t=0.35,0.10,0.35; A=p+q+t; lam=0.1
results['posterior_tilt']=[{'loops':n,'conditional_drift':(p-q-n)/(A+n),
 'exponential_factor':(p*math.exp(-lam)+(q+n)*math.exp(lam)+t)/(A+n)} for n in [0,1,10,100]]
(R/'experiment_results.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print(json.dumps(results,indent=2))
