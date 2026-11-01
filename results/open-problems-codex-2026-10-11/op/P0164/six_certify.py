import json,numpy as np
from pathlib import Path
from scipy.optimize import linprog
from fractions import Fraction
from math import lcm,gcd
from functools import reduce
rows=json.loads(Path('six_truth_tables.json').read_text())
X=np.array([[1 if x>>i&1 else -1 for i in range(6)] for x in range(64)],dtype=int)
rejections=[];feasible=[];counts={}
for j,row in enumerate(rows):
 pos=row['positive_masks'];w=row['spectrum']
 if w[1]>=2624:continue
 A=X[pos]
 # A convex combination of positive cube vectors equalling zero contradicts strict threshold separation.
 lp=linprog(np.zeros(len(pos)),A_eq=np.vstack((A.T,np.ones(len(pos)))),b_eq=np.array([0]*6+[1]),bounds=[(0,None)]*len(pos),method='highs')
 if not lp.success:feasible.append(j);continue
 coeff=[Fraction(float(v)).limit_denominator(100000) for v in lp.x]
 if any(sum(coeff[k]*int(A[k,i]) for k in range(len(pos)))!=0 for i in range(6)):raise RuntimeError('rational reconstruction failed')
 assert sum(coeff)==1 and all(c>=0 for c in coeff)
 den=lcm(*(c.denominator for c in coeff));ints=[int(c*den) for c in coeff];d=reduce(gcd,ints);ints=[c//d for c in ints]
 trade=[dict(mask=x,multiplicity=c) for x,c in zip(pos,ints) if c]
 assert all(sum(v['multiplicity']*int(X[v['mask'],i]) for v in trade)==0 for i in range(6))
 rejections.append(dict(table_index=j,spectrum=w,trade=trade));counts[str(w)]=counts.get(str(w),0)+1
result=dict(rejected=len(rejections),unresolved=feasible,counts=counts,certificates=rejections)
Path('six_rejection_certificates.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print('exactly certified nonthreshold',len(rejections),'unresolved',feasible,'counts',counts)
print('first certificate',rejections[0])
# An exact rational lower estimate pi/4 > sum_{j=0}^{63} (-1)^j/(2j+1) > 25/32.
s=sum((Fraction((-1)**j,2*j+1) for j in range(64)),Fraction(0))
assert s>Fraction(25,32);print('pi bound rational slack',s-Fraction(25,32))
