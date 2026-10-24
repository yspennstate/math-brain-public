from pathlib import Path
from itertools import combinations
from collections import Counter
import json
rows=json.loads(Path('six_truth_tables.json').read_text());certs=json.loads(Path('six_full_threshold_certificates.json').read_text())
N=64;X=[[1 if x>>i&1 else -1 for i in range(6)] for x in range(N)]
functions={tuple(r['positive_masks']) for r in rows};assert len(functions)==2646
# Independent direct definition of Fourier coefficient, without Walsh transform.
spectra=Counter();covered=set();threshold_w1=[]
for sign,records in [('positive',certs['positive_certificates']),('negative',certs['negative_certificates'])]:
 for c in records:
  j=c['table_index'];assert j not in covered;covered.add(j);r=rows[j];pos=set(r['positive_masks']);f=[1 if x in pos else -1 for x in range(N)]
  assert all(f[x]==-f[63-x] for x in range(N))
  assert all(f[x]<=f[x|(1<<i)] for x in range(N) for i in range(6))
  if sign=='positive':
   w=c['weights'];assert all(sum(w[i]*X[x][i] for i in range(6))>0 for x in pos)
  else:
   trade=c['trade'];assert trade and all(v['mask'] in pos and v['multiplicity']>0 for v in trade)
   assert all(sum(v['multiplicity']*X[v['mask']][i] for v in trade)==0 for i in range(6))
  W=[0]*7
  for s in range(N):
   a=sum(f[x]*(-1)**((x&s).bit_count()) for x in range(N));W[s.bit_count()]+=a*a
  assert W==r['spectrum']==c['spectrum'];spectra[tuple(W)]+=1
  if sign=='positive':assert W[1]>=2752 and W[1]-W[5]>=2304;threshold_w1.append(W[1])
assert covered==set(range(2646));assert min(threshold_w1)==2752
# Independent completeness construction: enumerate all choices of middle-layer winners
# and then all subsets of pair masks consistent with those triple winners.
triples=[x for x in range(N) if x.bit_count()==3 and x<63-x];pairs=[x for x in range(N) if x.bit_count()==2]
independent=set()
for flags in range(1024):
 winning_triples={a if flags>>i&1 else 63-a for i,a in enumerate(triples)}
 allowed=[p for p in pairs if all(t in winning_triples for t in range(N) if t.bit_count()==3 and p&t==p)]
 for bits in range(1<<len(allowed)):
  E={p for i,p in enumerate(allowed) if bits>>i&1}
  if any(a&b==0 for a,b in combinations(E,2)):continue
  pos=tuple(x for x in range(N) if x.bit_count()>=5 or x.bit_count()==4 and 63-x not in E or x.bit_count()==3 and x in winning_triples or x.bit_count()==2 and x in E)
  independent.add(pos)
for i in range(6):independent.add(tuple(x for x in range(N) if x>>i&1))
assert independent==functions
result=dict(independent_complete_count=len(independent),thresholds=len(threshold_w1),nonthresholds=len(certs['negative_certificates']),spectral_classes=len(spectra),all_integer_certificates='PASS',all_direct_fourier_sums='PASS',minimum_threshold_W1='43/64',polynomial_dominance='PASS')
Path('six_independent_check.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result,indent=2))
