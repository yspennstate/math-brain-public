from pathlib import Path
import itertools,json,time
from fractions import Fraction as F
start=time.monotonic();q=F(1,4);a=F(1,8);r=F(3,8)
fresh= sum(((q-s*a)*q*q for s in [-1,1]),F(0))/2
prefix=sum((r*(q-s*a) for s in [-1,1]),F(0))/2
joint=sum((r*(q-s*a)*(q-s*a)*q*q for s in [-1,1]),F(0))/2
posterior=joint/prefix
assert joint<=fresh and posterior>fresh
paths=0;covercases=0
steps=[(1,0),(-1,0),(0,1),(0,-1)]
for word in itertools.product(range(4),repeat=8):
 x=y=0;pos=[(0,0)]
 for e in word:x+=steps[e][0];y+=steps[e][1];pos.append((x,y))
 h=[z[0] for z in pos];paths+=1
 for m in range(4):
  if m not in h:continue
  tm=h.index(m)
  assert all(z<m for z in h[:tm])
  for L in range(1,5):
   if m+L not in h:continue
   top=h.index(m+L);assert tm<top
   visits=[t for t in range(tm,top) if h[t]==m];last=visits[-1]
   for c in range(3):
    if L<=c or last-tm>c:continue
    pi=[(pos[t][0]-pos[tm][0],pos[t][1]-pos[tm][1]) for t in range(tm,last+1)]
    assert len(pi)-1<=c and pi[0]==(0,0) and pi[-1][0]==0
    assert all(h[t]>m for t in range(last+1,top))
    assert all(h[t]<m+L for t in range(tm,last+1))
    covercases+=1
# Without positive weights, the zero-continuation replay implication is false.
weighted=F(1,2)*0*1+F(1,2)*1*0;unweighted=F(1,2)*1+F(1,2)*0
assert weighted==0 and unweighted==F(1,2)
result={'unweighted_fresh_continuation':str(fresh),'prefix_probability_given_old_left_data':str(prefix),'prefix_and_continuation_probability':str(joint),'continuation_after_conditioning_on_prefix':str(posterior),'pre_prefix_domination_passed':True,'post_prefix_freshness_is_false':True,'planar_eight_step_paths_checked':paths,'finite_prefix_cover_cases_checked':covercases,'positive_weight_hypothesis_essential_example':{'weighted_probability':str(weighted),'unweighted_probability':str(unweighted)},'elapsed_seconds':time.monotonic()-start,'scope':'Exact finite checks of the new cover and likelihood steps; asymptotic probability lemmas are proved in the handwritten proof.'}
Path('fresh_history_experiments.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
