import json,numpy as np
from scipy.optimize import linprog
from fractions import Fraction
from math import lcm
from pathlib import Path
from collections import Counter
rows=json.loads(Path('six_truth_tables.json').read_text());X=np.array([[1 if x>>i&1 else -1 for i in range(6)] for x in range(64)])
positive=[];negative=[];counts=Counter()
for j,row in enumerate(rows):
 A=X[row['positive_masks']]
 lp=linprog(np.ones(6),A_ub=-A,b_ub=-np.ones(len(A)),bounds=[(None,None)]*6,method='highs')
 if lp.success:
  w=[Fraction(float(v)).limit_denominator(100000) for v in lp.x];d=lcm(*(v.denominator for v in w));w=[int(v*d) for v in w]
  assert all(sum(int(v)*wi for v,wi in zip(a,w))>0 for a in A)
  positive.append(dict(table_index=j,weights=w,spectrum=row['spectrum']));counts[tuple(row['spectrum'])]+=1
 else:
  dual=linprog(np.zeros(len(A)),A_eq=np.vstack((A.T,np.ones(len(A)))),b_eq=[0]*6+[1],bounds=[(0,None)]*len(A),method='highs');assert dual.success
  c=[Fraction(float(v)).limit_denominator(100000) for v in dual.x];d=lcm(*(v.denominator for v in c));c=[int(v*d) for v in c]
  assert all(v>=0 for v in c) and sum(c)>0
  assert all(sum(c[k]*int(A[k,i]) for k in range(len(A)))==0 for i in range(6))
  negative.append(dict(table_index=j,trade=[dict(mask=x,multiplicity=v) for x,v in zip(row['positive_masks'],c) if v],spectrum=row['spectrum']))
result=dict(threshold_count=len(positive),nonthreshold_count=len(negative),threshold_spectra={str(k):v for k,v in sorted(counts.items())},positive_certificates=positive,negative_certificates=negative)
Path('six_full_threshold_certificates.json').write_text(json.dumps(result,indent=2),encoding='utf8');print('thresholds',len(positive),'nonthresholds',len(negative));print(result['threshold_spectra'])
