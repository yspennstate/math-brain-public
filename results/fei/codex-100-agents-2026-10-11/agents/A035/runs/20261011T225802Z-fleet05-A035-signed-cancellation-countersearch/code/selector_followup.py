from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import importlib.util,json,time
ROOT=Path(__file__).resolve().parents[1]
# Extract the reusable kernel before the first search loop, to avoid re-running it.
namespace={'__file__':str(ROOT/'code'/'payment_test.py')}
source=(ROOT/'code'/'payment_test.py').read_text(encoding='utf-8')
exec(source.split('for n in range(1,LIMIT+1):')[0],namespace)
table=namespace['exact_table'];cert=namespace['certify'];start=time.perf_counter();records=[];witnesses=[]
for depth in range(5):
 n=1<<depth
 for word in range(1<<depth):
  def formula(x):
   vals=[bool((x>>i)&1) for i in range(n)]
   for level in range(depth):
    use_or=(word>>level)&1
    vals=[(vals[j] or vals[j+1]) if use_or else (vals[j] and vals[j+1]) for j in range(0,len(vals),2)]
   return 1 if vals[0] else -1
  h,I,a=table(n,formula);r=dict(depth=depth,word=word,n=n,**cert(h,n,I));records.append(r)
  Hlo=F(r['H'][0]);Hhi=F(r['H'][1])
  for t in range(1,17):
   # g=y*seed^t is balanced. F=1 on selector=+1, g otherwise.
   # H(F)=2+t H(seed)/2, Hinf(F)=2, I(F)=1+t I(seed)/2.
   if t*Hlo>4*(t*I+2):
    witnesses.append(dict(seed_depth=depth,seed_word=word,copies=t,dimension=t*n+2,I=str(1+t*I/2),Hinf='2',gap_interval=[str(t*Hlo/2),str(t*Hhi/2)],gap_minus_4I_lower=str(t*Hlo/2-4*(1+t*I/2))))
summary=dict(seed_count=len(records),selector_count=16*len(records),exact_checks=namespace['checks'],runtime_seconds=time.perf_counter()-start,records=records,gap4_witnesses=witnesses,
 max_H_over_I=max(records,key=lambda r:F(r['ratios_H_Hinf_gap'][0][0])))
(ROOT/'out'/'selector_followup.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print('Seeds',len(records),'selectors',16*len(records),'gap4 witnesses',len(witnesses),'runtime',summary['runtime_seconds'])
print('max ratio',summary['max_H_over_I'])
if witnesses:print('first witness',witnesses[0])
