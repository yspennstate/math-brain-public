"""Close finite-grid maximum using certified nonbinary bounds and all 20 binary cases."""
import biased_grid as bg
import numpy as np,json
from fractions import Fraction as F
OUT=bg.OUT
cert=json.loads((OUT/'grid_certificate.json').read_text()); assert cert['complete']
logs=json.loads((OUT/'log_intervals.json').read_text()); scale=logs['scale']
low=np.array([x[0] for x in logs['entries']],dtype=np.int64)
high=np.array([x[1] for x in logs['entries']],dtype=np.int64)
targetlo=F(26)-12*F(int(high[3]),scale); targethi=F(26)-12*F(int(low[3]),scale)
checks=0
for row in cert['records']:
 if row['n']>=3: assert F(row['upper'])<targetlo; checks+=1
masks,T=bg.prime_tables(2)
winning=[]
for bm in range(4):
 A,ks,deg,D,_=bg.moments(2,T,bm); b=bm.bit_count()
 weights=A*A*3**(b-ks); delta=(weights[:,1:]*(deg[1:]-1)).sum(axis=1)
 c=(2*(D.bit_length()-1)-2*ks)*scale
 Hup=(weights[:,1:]*(c[1:]+2*ks[1:]*high[3]-2*low[np.abs(A[:,1:])])).sum(axis=1)
 for j,m in enumerate(masks):
  if bm==3 and int(m)==14:
   assert A[j].tolist()==[-2,18,18,-18]
   assert weights[j].tolist()==[36,972,972,324]
   assert int(delta[j])==324
   winning.append({'n':2,'mask':14,'biasmask':3})
  else: assert F(int(Hup[j]),scale*int(delta[j]))<targetlo
  checks+=1
assert len(winning)==1
data={'exact_grid_maximum':'26-12*log2(3)','maximum_lower':str(targetlo),'maximum_upper':str(targethi),'canonical_winner':winning[0],'proof':'all nonbinary upper certificates strictly below candidate lower; all remaining binary cases checked exactly; candidate has two singleton masses 27/64 and pair mass 9/64','assertions':checks,'full_grid_cases':4639338,'representatives':458356,'continuous_bias_supremum':'NOT_CERTIFIED'}
(OUT/'exact_winner.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps(data,indent=2))
