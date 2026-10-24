import random,math,json
from pathlib import Path
rng=random.Random(8108);rows=[]
for t in range(300):
 lo=-rng.randrange(1,80);hi=rng.randrange(1,80)
 slopes=sorted(rng.uniform(-15,15) for _ in range(hi-lo))
 vals=[0.0]
 for x in slopes:vals.append(vals[-1]+x)
 m=min(vals); w=[x-m for x in vals]
 z=sum(math.exp(-x) for x in w); zh=sum(math.exp(-x/2) for x in w)
 e=sum(x*math.exp(-x) for x in w)/z
 assert zh<=3*z+1e-10 and e<=2*math.log(3)+1e-10
 rows.append({'domain':[lo,hi],'partition_ratio':zh/z,'expected_excess':e})
# Truncated heavy slope mixing: normalize with the same infinite mixing constant
# estimated by a long sum; the exact divergence is proved by harmonic comparison.
cutoffs=[10,100,1000,10000]
normalizer=1+2*sum((1+k)**-3 for k in range(1,100001))
mixture=[{'cutoff':n,'partial_first_abs_moment':2*sum(k/(1+k)**3 for k in range(1,n+1))/normalizer,'partial_second_moment':2*sum(k*k/(1+k)**3 for k in range(1,n+1))/normalizer} for n in cutoffs]
# Given the sum of two gradients S, the quadratic bridge is independent of slope K.
bridge=[]
for S in [-6,-1,0,3,12]:
 a=list(range(-30,31)); m=math.ceil(S*S/2)
 weights=[math.exp(-(x*x+(S-x)**2-m)) for x in a];z=sum(weights)
 excess=sum(w*(x*x+(S-x)**2-m) for x,w in zip(a,weights))/z
 for K in [-5,0,4]:
  logs=[-(x-K)**2-(S-x-K)**2 for x in a];mx=max(logs);wk=[math.exp(v-mx) for v in logs];zk=sum(wk)
  err=max(abs(w/zk-v/z) for w,v in zip(wk,weights));assert err<1e-13
 bridge.append({'sum':S,'local_minimum':m,'expected_thermal_excess':excess})
result={'seed':8108,'convex_potential_tests':300,'max_partition_ratio':max(x['partition_ratio'] for x in rows),'max_expected_excess':max(x['expected_excess'] for x in rows),'mixture_partial_moments':mixture,'quadratic_bridge_tests':bridge,'all_checks_passed':True,'rows':rows}
Path('heatbath_experiment_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print({k:v for k,v in result.items() if k!='rows'})
