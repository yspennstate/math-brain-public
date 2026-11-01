from itertools import permutations
from bisect import bisect_right
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
out=[]
def tops(p):
 t=[]
 for x in p:
  i=bisect_right(t,x)
  if i==len(t):t.append(x)
  else:t[i]=x
 return t
for B in [(1,2),(1,3),(1,2,3),(1,3,4),(1,2,4),(1,3,5)]:
 n=B[-1];count=sum(tops(p)[:len(B)]==list(B) for p in permutations(range(1,n+1)))
 r=Q(count,factorial(n));out.append({'B':B,'n':n,'permutations':factorial(n),'count':count,'probability':str(r)})
assert [a['probability'] for a in out]==['1/2','1/3','1/6','1/8','1/8','11/120']
D=Q(1,6)*Q(11,120)-Q(1,8)**2
assert D==-Q(1,2880)
result={'enumeration':out,'mixed_coefficient_determinant':str(D),'mixed_log_derivative_at_origin':str(D/Q(1,6)**2),'conditional_gap_density_derivative_at_origin':str((Q(1,8)*Q(1,2)-Q(1,6)*Q(1,3))/Q(1,2)**2)}
Path('checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
Path('STATUS.md').write_text('STATE: WORKING\nNEXT: Write the continuous non-Markov proof, formally check its finite certificate, and finish literature reconciliation.\nVERDICT: PARTIAL\n\n2026-10-11: Source and 1993 representation verified. Prior Bessel/Schur work read. Exact permutation counts give a nonzero mixed-density determinant -1/2880, obstructing independent consecutive gaps. The continuous non-Markov implication is being written and checked.\n',encoding='utf8')
