import json,math
from pathlib import Path
from fractions import Fraction
import mpmath as mp
from symmetric import evaluate,mask_vector,integer_data
mp.mp.dps=100
rows=[];mindifference=1;count=0
for n in range(1,25):
 row=json.loads(Path(f'census_cert_{n:02d}.json').read_text())
 assert row['B_le_2.18I_integer_certificate']
 # Count balanced symmetric functions independently by meet in the middle.
 weights=[math.comb(n,t) for t in range(1,n+1)]
 left,right=weights[:n//2],weights[n//2:]
 def sums(weights):
  a=[0]
  for w in weights:a+=[x+w for x in a]
  return a
 from collections import Counter
 c=Counter(sums(right));target=1<<(n-1)
 balanced=sum(c[target-x] for x in sums(left))
 assert balanced==row['balanced'],(n,balanced,row['balanced'])
 for objective,entry in row['maxima'].items():
  if entry['value']<0:continue
  candidates=[]
  for mask in entry['candidates']:
   f=mask_vector(n,mask)
   data=integer_data(f)
   assert all(data[k][1]>=data[k+1][1] for k in range(n))
   v=evaluate(f,100)
   candidates.append((v[objective],mask,v['value_vector']));count+=1
  candidates.sort(reverse=True)
  value,mask,vec=candidates[0]
  if entry['runner_up_below_tolerance']>=0:
   gap=float(value)-entry['runner_up_below_tolerance'];mindifference=min(mindifference,gap)
   assert gap>1e-11,(n,objective,gap)
  ties=[{'mask':m,'value_vector':v} for x,m,v in candidates if abs(x-value)<mp.mpf('1e-70')]
  rows.append({'n':n,'objective':objective,'value':mp.nstr(value,70),'extremizers_up_to_global_sign':ties,'candidates_checked':len(candidates)})
Path('certified_extrema.json').write_text(json.dumps(rows,indent=2)+'\n')
print('candidate_extremizers_at_100_digits',count)
print('smallest_gap_to_excluded_candidate',mindifference)
print('balanced_counts_checked_meet_in_the_middle',24)
print('rigorous_B_certificate_all_representatives_through_n24',True)
